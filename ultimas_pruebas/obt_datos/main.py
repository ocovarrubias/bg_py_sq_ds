import os
from google.cloud import bigquery

os.environ['GOOGLE_APPLIACTION_CREDENTIALS'] = 'input2insight-338823-816106ec13f2'

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the model to fetch.
# table_id = 'your-project.your_dataset.your_table'


sql= """
SELECT first_name, last_name, email
FROM `input2insight-338823.external_processing.users_basics`
WHERE state = 'Oaxaca' AND fav_color = 'Red'
LIMIT 20
"""

query_job = client.query(
    sql
)

for row in query_job.result():
    print(row)
