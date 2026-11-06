
import mysql.connector

mydbConnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="atik"
)

db_name = "testdb"

mycursor = mydbConnection.cursor()

query = "CREATE DATABASE " + db_name

mycursor.execute(query)