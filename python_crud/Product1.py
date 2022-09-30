import pyodbc

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-A3BJ2GF;"
                      "Database=BasePrueba;"
                      "Trusted_Connection=yes;"
                      "MARS_Connection=yes")


cursor = cnxn.cursor()
cursor.execute('SELECT * FROM ProductMasters')

def getData(cnxn):
    print("Read")
    cursor = cnxn.cursor();
    cursor.execute("select * from ProductMasters")
    for row in cursor:
        print(f'{row}')

def insertData(cnxn):
    print("Insert")
    cursor = cnxn.cursor();
    cursor.execute(
        'insert into ProductMasters (product,cost) values(?,?)',
        ('Laptop B', 370000.00)
    )
    #cnxn.commit()

def updateData(cnxn):
    print("Update")
    cursor = cnxn.cursor();
    cursor.execute(
        'update ProductMasters set cost = ? where id = ?', (49000,1))

    #cnxn.commit()

def deleteData(cnxn):
    print("Delete")
    cursor = cnxn.cursor();
    cursor.execute(
        'delete from ProductMasters where id = ?', (4))
    cnxn.commit()

#insertData(cnxn)
#updateData(cnxn)
deleteData(cnxn)
getData(cnxn)