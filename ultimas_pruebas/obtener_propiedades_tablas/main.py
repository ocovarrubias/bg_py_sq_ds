
from google.cloud import bigquery

import os
os.environ["GCLOUD_PROJECT"] = "input2insight-338823"

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the model to fetch.
# table_id = 'your-project.your_dataset.your_table'

table = client.get_table('input2insight-338823.external_processing.example')  # Make an API request.

# View table properties
def obtener_propiedades_tablas(request):
    print("Hola aqui estoy")
    print("Got table '{}.{}.{}'.".format(table.project, table.dataset_id, table.table_id))
    print("Table schema: {}".format(table.schema))
    print("Table description: {}".format(table.description))
    print("Table has {} rows".format(table.num_rows))
    return 'Ok'