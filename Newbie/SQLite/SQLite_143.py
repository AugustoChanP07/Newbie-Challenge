import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

Date = int(input("Enter a year: "))
cursor.execute("SELECT * FROM books WHERE DatePublished >= ? ORDER BY DatePublished", (Date,))
for x in cursor.fetchall():
    print(x) 
