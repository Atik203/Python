
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

      UPDATE Students
      SET Name = "Karim"
      WHERE Roll = 1

"""

mycursor.execute(query)
mydbConnection.commit()