import mysql.connector as connection
print("Enter Database")
database = input().lower()

connectionDB = {
    "host":"localhost",
    "user":"root",
    "password":"Text@12345",
    "database": database
}
conn = connection.connect(**connectionDB)
cursorObject = conn.cursor()

print("Enter Table Name")
tableName = str(input()).lower()

print("Enter  Value separated by comma ")
val = str(input())
value = tuple(val.split(','))

insertQuery = f"INSERT INTO {tableName} VALUES {value}; "

cursorObject.execute(insertQuery)
conn.commit()

print(cursorObject.rowcount,"details inserted")


conn.close()