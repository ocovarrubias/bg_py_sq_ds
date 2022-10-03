from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

query = """
    SELECT date
    FROM `input2insight-338823.covid_19_vaccination_search_insights.covid19_vaccination_search_insights`
    WHERE sub_region_1 = 'England' AND sub_region_2 = 'Wycombe District'
    LIMIT 20
"""
query_job = client.query(query)  # Make an API request.

print("The query data:")
for row in query_job:
    # Row values can be accessed by field name or index.
    print("name={}, count={}".format(row[0], row["total_people"]))