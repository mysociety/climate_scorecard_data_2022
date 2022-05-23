from pathlib import Path

import pandas as pd

from climate_scorecard_data_2022.la_processing import *

source_file = Path("data", "raw", "individual_answers.csv")

data_package_folder = Path("data", "data_packages", "scorecard_data")

split_data_package_folder = Path("data", "data_packages", "scorecards_by_council_group")

labels = {
    "s1_gov": "Governance, development and funding",
    "s2_m&a": "Mitigation and adaptation",
    "s3_c&a": "Commitment and intergration",
    "s4_coms": "Community, engagement and communications",
    "s5_mset": "Measuring and setting emissions targets",
    "s6_cb": "Co-benefits",
    "s7_dsi": "Diversity and inclusion",
    "s8_est": "Education, skills and training",
    "s9_ee": "Ecological emergency",
    "total": "Overall score",
}

weights = {
    "s1_gov": 0.15,
    "s2_m&a": 0.15,
    "s3_c&a": 0.15,
    "s4_coms": 0.15,
    "s5_mset": 0.10,
    "s6_cb": 0.05,
    "s7_dsi": 0.10,
    "s8_est": 0.10,
    "s9_ee": 0.05,
}


def questions_list():
    df = pd.read_csv(Path("data", "raw", "questions.csv"))
    df.to_csv(Path(data_package_folder, f"questions_list.csv"), index=False)


def section_weighting():
    """
    Create section weighting csvs
    """

    df = pd.DataFrame(list(labels.items()), columns=["section_id", "section_name"])
    df["section_weight"] = df["section_id"].map(weights)
    df.to_csv(Path(data_package_folder, f"section_labels_and_weights.csv"), index=False)


def individual_answers():
    """
    Smallest possible version of scores for each question
    """

    df = pd.read_csv(Path("data", "raw", "individual_answers.csv"))
    df = df[
        [
            "answer_id",
            "local-authority-code",
            "question_id",
            "audited_answer",
            "score",
            "max_score",
        ]
    ]

    df = df.sort_values("local-authority-code")

    df.to_csv(Path(data_package_folder, f"individual_answers.csv"), index=False)


def create_x_y_file():
    """
    Get score and max score for each local authority and each section
    """
    df = pd.read_csv(source_file)
    df["local-authority-code"] = df["answer_id"].str.split("_").str[0]
    pt = df.pivot_table(
        ["max_score", "score"], index=["local-authority-code", "section"], aggfunc="sum"
    ).reset_index()

    pt["section_name"] = pt["section"].map(labels)

    pt.to_csv(Path(data_package_folder, f"section_scores.csv"), index=False)


def create_weighted_totals():
    def score_row(row: pd.Series) -> float:
        value = 0
        for section, weight in weights.items():
            value += row[section] * weight
        return value

    def df_to_score_columns(df, index="section"):
        pt = df.pivot_table(["score", "max_score"], index=[index], aggfunc="sum")
        pt.loc["raw_total"] = pt.sum()
        pt["percentage"] = pt["score"] / pt["max_score"]
        pt = pt[["percentage"]].transpose().reset_index(drop=True).fillna(0)
        pt.columns = list(pt.columns)
        return pt.iloc[0]

    df = pd.read_csv(Path("data", "raw", "individual_answers.csv"))

    df = df.groupby("local-authority-code").apply(df_to_score_columns)
    # rdf = df[df["total"] > 0]
    df["weighted_total"] = df.apply(score_row, axis="columns")
    df = (df.round(2) * 100).astype(int)

    d = (
        df.sort_values("weighted_total", ascending=False)
        .reset_index()
        .la.get_council_info(["local-authority-type-name", "official-name"])
    )
    new_order = [x for x in d.columns if x != "official-name"]
    d = d[["official-name"] + new_order]

    filters = pd.read_csv(Path("data", "raw", "all_filters.csv")).drop(
        columns=["local-authority-type-name"]
    )

    d = (
        d.merge(filters, on="local-authority-code")
        .fillna("")
        .drop(columns=["raw_total", "la_deprivation_score"])
    )

    unitaries = [
        "Welsh unitary authority",
        "Scottish unitary authority",
        "Unitary authority",
        "Metropolitan district",
        "London borough",
        "City corporation",
    ]

    league_map = {x: "Single tier" for x in unitaries}
    league_map["NI district"] = "Northern Ireland"
    league_map["County"] = "County councils"
    league_map["Non-metropolitan district"] = "District councils"
    league_map["Combined authority"] = "Combined/strategic authorities"
    league_map["Strategic Regional Authority"] = "Combined/strategic authorities"

    d["group"] = d["local-authority-type-name"].apply(lambda x: league_map.get(x, x))

    d.to_csv(Path(data_package_folder, f"authority_scores.csv"), index=False)


def slugify(v: str) -> str:
    return v.lower().strip().replace(" ", "_").replace("-", "_").replace("/", "_")


def create_split_file():
    df = pd.read_csv(Path(data_package_folder, f"authority_scores.csv"))

    for g, d in df.groupby("group"):
        d.sort_values("weighted_total", ascending=False)
        print(g, slugify(g))
        d.to_csv(split_data_package_folder / f"{slugify(g)}.csv", index=False)


def create_files():
    """
    Create different csvs files for the datapackage
    """
    section_weighting()
    create_x_y_file()
    create_weighted_totals()
    individual_answers()
    questions_list()
    create_split_file()


if __name__ == "__main__":
    create_files()
