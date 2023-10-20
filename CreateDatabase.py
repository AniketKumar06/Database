import mysql.connector 


conn = mysql.connector.connect(host="localhost",user="root",password="Text@12345");



# print(conn)
# conn.close()

print("Enter Database Name")
database = input()

#preparation of cursor object
cursorObject = conn.cursor()

# Creating database 

cursorObject.execute("CREATE DATABASE "+ database +";")


conn.close()
