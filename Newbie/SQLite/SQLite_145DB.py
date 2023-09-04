import sqlite3

with sqlite3.connect("TestScores.db") as db:
    cursor = db.cursor()

#cursor.execute("""CREATE TABLE IF NOT EXISTS Test (
#    Name TEXT NOT NULL,
#    Grade INTEGER NOT NULL);""")

cursor.execute("SELECT * FROM Test")
for x in cursor.fetchall():
    print(x)