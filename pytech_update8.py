import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pysports"
)

cursor = db.cursor()

query = "SELECT team_id, team_name, mascot FROM team"

cursor.execute(query)

for team in cursor:
    print(team)

cursor.close()

db.close()