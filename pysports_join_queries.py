import mysql.connector


connection = mysql.connector.connect(
  host="localhost",
  user="stok414",
  password="YourRootPassword",
  database = "pysports"
)


cursor = connection.cursor()

query = 'SELECT p.player_id, p.first_name, p.last_name, t.team_name FROM player p JOIN team t ON t.team_id = p.team_id'

cursor.execute(query)
results = cursor.fetchall()

connection.close()

print("--- DISPLAYING PLAYER RECORDS ---")

for i in results:
    print(f'Player ID: {i[0]}')
    print(f'First Name: {i[1]}')
    print(f'Last Name: {i[2]}')
    print(f'Team Name: {i[3]}')
    print()