import networkx as nx
import sqlite3

connection = sqlite3.connect("/media/crouton/aislam4/database.db")
cursor = connection.cursor()

cursor.execute("SELECT Hash FROM Contents;")
data = cursor.fetchall()
data = [x[0] for x in data]
print(len(data))

file_name = open('Hashes.txt','a')
for item in data:
    file_name.write(item+"\n")