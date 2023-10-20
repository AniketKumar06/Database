import mysql.connector as dbConnection
print("Enter Database")
database = input().lower()

connectionDB = {
    "user":"root",
    "host":"localhost",
    "password":"Text@12345",
    "database":database
}


conn = dbConnection.connect(**connectionDB)

cursorObject = conn.cursor()

print("Enter Table Name")
tableName = str(input()).lower()

rowInsert = 0
while True:
    print("Enter  Value separated by comma ")
    val = str(input())
    value = tuple(val.split(','))

    insertQuery = f"INSERT INTO {tableName} VALUES {value}; "

    cursorObject.execute(insertQuery)
    conn.commit()

    rowInsert += cursorObject.rowcount
    n = input("Want more data Insert, Type Y for 'yes' or Type N for n")
    if(n == 'N' or n =='n'):
        break

print(rowInsert,"details inserted")

print(conn)
conn.close()