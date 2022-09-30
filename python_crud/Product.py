#Para realizar la conexión a la B.D.
import pyodbc 

#Se define la conexión
sqlDbConn = pyodbc.connect(
    "Driver = {SQL Server Native Client 11.0};"
    "Server = DESKTOP-A3BJ2GF;"
    "Database = BasePrueba;"
    "Trusted_Connection=yes;"
)

def getData(sqlDbConn):
    print("Read")
    cursor = sqlDbConn.cursor();
    cursor.execute("select * from ProductMaster")
    for row in cursor:
        print(f'{row}')

def insertData(sqlDbConn):
    print("Insert")
    cursor = sqlDbConn.cursor();
    cursor.execute(
        'insert into ProductMaster (product,cost) values(?,?)',
        ('Laptop', 20000.00)
    )
    sqlDbConn.commit()

insertData(sqlDbConn)
getData(sqlDbConn)