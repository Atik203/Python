import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="atik"
)

print(mydb)
    