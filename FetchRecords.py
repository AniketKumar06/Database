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

print("Enter Fetech Query")
sqlquery = str(input())

cursorObject.execute(sqlquery)

print(f'Data Fetch from table {tableName} : ')
result = cursorObject.fetchall()
for x in result:
    print(x)
conn.close()