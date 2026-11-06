
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

      INSERT INTO Students (Roll , Name)
      VALUES 
      (5, "Rahim"),
      (2, "Atik"),
      (3, "Sakib")

"""

mycursor.execute(query)
mydbConnection.commit()