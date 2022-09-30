import pyodbc

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-A3BJ2GF;"
                      "Database=BasePrueba;"
                      "Trusted_Connection=yes;"
                      "MARS_Connection=yes")

cursor = cnxn.cursor()

# View table properties
def obt_props(cnxn):
    print("Aqui inicia obt_props")
    cursor = cnxn.cursor();
    #cursor.execute("select first_name,last_name, email from MOCK_DATA where state = 'Guerrero' and gender = 'Male'")
    cursor.execute("select first_name,last_name, email, gender from MOCK_DATA WHERE state = 'Guerrero' AND (gender = 'Male' OR (gender = 'Female' AND fav_color = 'Violet'))")
    #print("Got table '{}.{}.{}'.".format(table.project, table.dataset_id, table.table_id))
    #print("Table schema: {}".format(table.schema))
    #print("Table description: {}".format(table.description))
    #print("Table has {} rows".format(table.num_rows))
    #return 'Ok'
    for row in cursor:
        print(f'{row}')

obt_props(cnxn)