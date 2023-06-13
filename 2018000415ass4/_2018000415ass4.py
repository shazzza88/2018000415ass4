import pyodbc
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2018000415\OneDrive - Western Institute of Technology at Taranaki\python\Python ass 4\Database4.accdb;')
cursor = conn.cursor()
cursor.execute( 'select * from Company_Table WHERE Founded BETWEEN 01/01/1907 AND 01/01/1940;' )

for row in cursor.fetchall():
    print(row) 

