"""
functions and pandas api to speed up working with
local authority data

"""
import string
from functools import lru_cache
from typing import Callable, List, Optional

import pandas as pd

la_lookup_url = "https://raw.githubusercontent.com/mysociety/uk_local_authority_names_and_codes/master/data/uk_local_authorities.csv"
name_lookup_url = "https://raw.githubusercontent.com/mysociety/uk_local_authority_names_and_codes/master/data/lookup_name_to_registry.csv"
gss_code = "https://raw.githubusercontent.com/mysociety/uk_local_authority_names_and_codes/master/data/lookup_gss_to_registry.csv"

import pandas.api as pd_api


@lru_cache
def get_la_df(include_historical: bool = False) -> pd.DataFrame:
    """
    retrieve the big grid of all local authority details from the repo
    """
    df = pd.read_csv(la_lookup_url)
    if include_historical is False:
        df = df.loc[df["end-date"].isnull()]
    return df


@lru_cache
def gss_registry_lookup(allow_none: bool = False) -> Callable:
    """
    retrieve a function that can be applied to convert gss codes to
    three letter codes
    """
    df = pd.read_csv(gss_code)
    df["gss-code"] = df["gss-code"].str.strip()
    lookup = df.set_index("gss-code")["local-authority-code"].to_dict()

    def convert(v):
        v = v.strip()
        result = lookup.get(v, None)
        if result is None and allow_none is False:
            raise ValueError(f"{v} not found in gss column")
        return result

    return convert


def remove_punctuations(text):
    for punctuation in string.punctuation + string.whitespace:
        text = text.replace(punctuation, "")
    return text


@lru_cache
def name_registry_lookup(allow_none: bool = False) -> Callable:
    """
    returns a function that will convert the name to 3-letter reg code
    """

    banned_words = ["council", "unitary"]

    df = pd.read_csv(name_lookup_url)
    df["la-name"] = df["la-name"].str.lower().str.strip()
    for b in banned_words:
        df["la-name"] = df["la-name"].str.replace(b, "", regex=False)
    df["la-name"] = df["la-name"].apply(remove_punctuations)
    lookup = df.set_index("la-name")["local-authority-code"].to_dict()

    def convert(v):
        if isinstance(v, str) is False:
            v = str(v)
        v_lower = v.lower().strip()
        for b in banned_words:
            v_lower = v_lower.replace(b, "")
        v_lower = remove_punctuations(v_lower)
        result = lookup.get(v_lower, None)
        if result is None and allow_none is False:
            raise ValueError(f"{v_lower} not found in name column")
        return result

    return convert


@pd_api.extensions.register_dataframe_accessor("la")
class LAPDAccessor(object):
    """
    extention to pandas dataframe
    """

    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def get_council_info(
        self,
        items: Optional[List[str]] = None,
        merge_type: str = "left",
        include_historical: bool = False,
    ) -> pd.DataFrame:
        """
        retrieve columns from comparison LA spreadsheet.
        Set merge_type to right to expand to include authorities not
        in the original dataset
        """

        df = self._obj
        if "local-authority-code" not in df.columns:
            df = df.la.create_code_column()
        adf = get_la_df(include_historical=include_historical)
        if items:
            adf = adf[["local-authority-code"] + items]
        return df.merge(adf, how=merge_type)

    def create_code_column(
        self, from_col: str = "name", code_col_name: str = "local-authority-code"
    ) -> pd.DataFrame:
        """
        Create registry code column
        """
        if str not in ["name", "gss"]:
            raise NotImplementedError("Invalid support tyle")
        if from_col == "gss":
            raise NotImplementedError("Add support for dataset based lookup from gss")
        return self.create_code_col_from_name(code_col_name)

    def create_code_col_from_name(
        self, code_col_name: str = "local-authority-code"
    ) -> pd.DataFrame:
        """
        try and detect the name column and create a registry code column
        """
        name_lookup = name_registry_lookup()
        df = self._obj

        name_col = None
        col = None
        for col in df.columns:
            first_value = df[col].iloc[0]
            try:
                name_lookup(first_value)
                name_col = col
                break
            except ValueError:
                pass
        if name_col is None:
            raise ValueError(
                "Could not find a column with a valid name in the first row"
            )

        df[code_col_name] = df[col].la.name_to_code()

        return df

    def gss_to_code(self) -> pd.Series:
        """
        convert a column of gss codes to local authority names
        """
        return self._obj.apply(gss_registry_lookup())


@pd_api.extensions.register_series_accessor("la")
class LASeriesAccessor(object):
    """
    extention to python series to more easily work with local authority data
    """

    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def name_to_code(self, allow_none=False) -> pd.Series:
        """
        convert a column of local authority names to 3 letter code
        """
        return self._obj.apply(name_registry_lookup(allow_none))

    def gss_to_code(self, allow_none=False) -> pd.Series:
        """
        convert a column of gss codes to local authority names
        """
        return self._obj.apply(gss_registry_lookup(allow_none))
