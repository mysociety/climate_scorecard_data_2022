---
name: scorecards_by_council_group
title: Scorecard data (by council group)
description: "Scorecards score information with seperate tables for each council type/group\n"
version: 1
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
- title: Combined/Strategic Authority Scorecards
  description: Scorecard scores for Combined or Strategic Authorities
  path: combined_strategic_authorities.csv
  name: combined_strategic_authorities
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
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
  download_id: scorecards-by-council-group-combined-strategic-authorities
- title: County Council Scorecards
  description: Scorecard scores for county councils
  path: county_councils.csv
  name: county_councils
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
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
  download_id: scorecards-by-council-group-county-councils
- title: District Council Scorecards
  description: Scorecard scores for district councils
  path: district_councils.csv
  name: district_councils
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
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
  download_id: scorecards-by-council-group-district-councils
- title: Northern Ireland Scorecards
  description: Scorecard scores for authorities in Northern Ireland
  path: northern_ireland.csv
  name: northern_ireland
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
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
  download_id: scorecards-by-council-group-northern-ireland
- title: Single Tier Scorecards
  description: Scorecard scores for single tier authorities
  path: single_tier.csv
  name: single_tier
  profile: tabular-data-resource
  scheme: file
  format: csv
  hashing: md5
  encoding: utf-8
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
  download_id: scorecards-by-council-group-single-tier
composite:
  xlsx: scorecards-by-council-group-xlsx
---
