import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLIACTION_CREDENTIALS'] = 'input2insight-338823-816106ec13f2'

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the model to fetch.
# table_id = 'your-project.your_dataset.your_table'


sql= """
SELECT date 
FROM `input2insight-338823.covid_19_vaccination_search_insights.covid19_vaccination_search_insights`
WHERE sub_region_1 = 'England' AND sub_region_2 = 'Wycombe District'
LIMIT 20
"""

query_job = client.query(
    sql
)

for row in query_job.result():
    print(row)
