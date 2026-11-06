
import mysql.connector

db_name = "testdb"
mydbConnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="atik",
    database=db_name

)

mycursor = mydbConnection.cursor()

query = """

      CREATE TABLE Students (
      Roll INT PRIMARY KEY,
      Name VARCHAR(50)

     )

"""

mycursor.execute(query)