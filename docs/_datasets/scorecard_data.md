---
name: scorecard_data
title: Scorecard data (all)
description: "Processed and raw data for the 2022 Council Climate Scorecards\n"
version: 1.0
licenses:
- name: CC-BY-NC-4.0
  path: https://creativecommons.org/licenses/by-nc/4.0/
  title: Creative Commons Attribution-NonCommercial 4.0 International License
sources:
- title: Council Climate Plan Scorecards
  path: https://councilclimatescorecards.uk/
contributors:
- title: Climate Emergency UK
  path: https://www.climateemergency.uk/
  role: author
- title: mySociety
  path: https://mysociety.org
  role: author
download_options:
  gate: hard
  survey: 6896293/CUK-data-feedback
  header_text: Before you can download this file
resources:
- title: Authority scores
  description: For each authority, percentage score for each section and the overall
    weighted total.
  path: authority_scores.csv
  name: authority_scores
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  sheet_order: 1
  schema:
    fields:
    - name: official-name
      type: string
      description: Long form name of local authority
      constraints:
        unique: true
      example: Somerset West and Taunton Council
    - name: local-authority-code
      type: string
      description: Three letter code of local authority
      constraints:
        unique: true
      example: SWT
    - name: s1_gov
      type: integer
      description: Rounded percentage score for 'Governance, development and funding'
      constraints:
        unique: false
      example: 81
    - name: s2_m&a
      type: integer
      description: Rounded percentage score for 'Mitigation and adaptation'
      constraints:
        unique: false
      example: 100
    - name: s3_c&a
      type: integer
      description: Rounded percentage score for 'Commitment and intergration'
      constraints:
        unique: false
      example: 100
    - name: s4_coms
      type: integer
      description: Rounded percentage score for 'Community, engagement and communications'
      constraints:
        unique: false
      example: 89
    - name: s5_mset
      type: integer
      description: Rounded percentage score for 'Measuring and setting emissions targets'
      constraints:
        unique: false
      example: 100
    - name: s6_cb
      type: integer
      description: Rounded percentage score for 'Co-benefits'
      constraints:
        unique: false
      example: 100
    - name: s7_dsi
      type: integer
      description: Rounded percentage score for 'Diversity and inclusion'
      constraints:
        unique: false
      example: 60
    - name: s8_est
      type: integer
      description: Rounded percentage score for 'Education, skills and training'
      constraints:
        unique: false
      example: 100
    - name: s9_ee
      type: integer
      description: Rounded percentage score for 'Ecological emergency'
      constraints:
        unique: false
      example: 100
    - name: weighted_total
      type: integer
      description: Rounded percentage overall score for authority (with weighting
        applied by section)
      constraints:
        unique: false
      example: 91
    - name: local-authority-type-name
      type: string
      description: The type of local authority
      constraints:
        unique: false
      example: Non-metropolitan district
    - name: council-quintile
      type: number
      description: Local authorities average IMD deprivation grouped into five deciles
        (1 is most deprived, 5 is least deprived)
      constraints:
        unique: false
      example: 2.0
    - name: pop_bucket
      type: string
      description: Local authorities grouped into different population sizes
      constraints:
        unique: false
      example: 140k - 160k
    - name: region
      type: string
      description: Nation or region of UK the local authority is in
      constraints:
        unique: false
      example: South West
    - name: ruc_cluster
      type: string
      description: Urban/Rural nature of the local authority
      constraints:
        unique: false
      example: Urban with rural areas
    - name: political_control
      type: string
      description: Political control at the time the plans were scored
      constraints:
        unique: false
      example: Liberal Democrat
    - name: group
      type: string
      description: Scorecard group (used for comparison purposes)
      constraints:
        unique: false
      example: District councils
  download_id: scorecard-data-authority-scores
- title: Individual answers
  description: The scored value for each question for each authority. If a Council
    had no plan publicly available then all boxes are blank.
  path: individual_answers.csv
  name: individual_answers
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: answer_id
      type: string
      description: Unique ID for an answer to a question by an authority
      constraints:
        unique: true
      example: ABC_s1_gov_q1_sp1
    - name: local-authority-code
      type: string
      description: 3 letter code for local authority
      constraints:
        unique: false
      example: ABC
    - name: question_id
      type: string
      description: ID for question
      constraints:
        unique: false
      example: s1_gov_q1_sp1
    - name: audited_answer
      type: string
      description: The result assigned to the question by the marker
      constraints:
        unique: false
      example: 'True'
    - name: score
      type: number
      description: The score the answer translate to
      constraints:
        unique: false
      example: 1.0
    - name: max_score
      type: integer
      description: The maximum score avaliable for the question.
      constraints:
        unique: false
      example: 1
  download_id: scorecard-data-individual-answers
- title: Questions list
  description: List of questions used, and the allowed values and scores
  path: questions_list.csv
  name: questions_list
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: question_id
      type: string
      description: Unique ID for a question
      constraints:
        unique: true
      example: s1_gov_q1
    - name: Question description
      type: string
      description: Full text description of the question
      constraints:
        unique: true
      example: Is the Plan led by a senior lead officer with a named individual, cabinet
        member or committee responsible for developing and delivering the Plan and
        are the actions assigned?
    - name: Options
      type: string
      description: The kind of response allowed to the question (generally checkbox).
        HEADER is used for grouping purposes.
      constraints:
        unique: false
      example: HEADER
    - name: Scores
      type: string
      description: Map of scores to different answers
      constraints:
        unique: false
      example: '0'
  download_id: scorecard-data-questions-list
- title: Section labels and weights
  description: Mapping of short section IDs to long labels, and the weighting used
    in the overall score
  path: section_labels_and_weights.csv
  name: section_labels_and_weights
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: section_id
      type: string
      description: ID for section (group of questions)
      constraints:
        unique: true
      example: s1_gov
    - name: section_name
      type: string
      description: Description of questions in sections.
      constraints:
        unique: true
      example: Governance, development and funding
    - name: section_weight
      type: number
      description: Weighting applied to the section percentage in the final result.
      constraints:
        unique: false
      example: 0.15
  download_id: scorecard-data-section-labels-and-weights
- title: Section Scores
  description: By authority, the scores received for each section and the total possible
    for that authority type.
  path: section_scores.csv
  name: section_scores
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
  schema:
    fields:
    - name: local-authority-code
      type: string
      description: 3 letter code for authority
      constraints:
        unique: false
      example: ABC
    - name: section
      type: string
      description: Section short ID (a section is a group of questions)
      constraints:
        unique: false
        enum:
        - s1_gov
        - s2_m&a
        - s3_c&a
        - s4_coms
        - s5_mset
        - s6_cb
        - s7_dsi
        - s8_est
        - s9_ee
      example: s1_gov
    - name: max_score
      type: integer
      description: Maximum score avaliable for section
      constraints:
        unique: false
      example: 21
    - name: score
      type: number
      description: Score this authority received for this section
      constraints:
        unique: false
      example: 0.0
    - name: section_name
      type: string
      description: Descriptive name for section (group of questions)
      constraints:
        unique: false
      example: Governance, development and funding
  download_id: scorecard-data-section-scores
composite:
  xlsx: scorecard-data-xlsx
---
