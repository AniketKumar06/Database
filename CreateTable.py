import mysql.connector

try:

    print("Enter database to use")
    database = input()
    connectionDB ={
        "host" : "localhost",
        "user" : "root",
        "password" :"Text@12345",
        "database": database
    }

    conn = mysql.connector.connect(**connectionDB)
    

except Exception as e:
    print("Database Not found")

else:
    tableName = str(input())
    cursorObject = conn.cursor()

    cursorObject.execute(tableName)

    print("Table create in database")

finally:
    conn.close()