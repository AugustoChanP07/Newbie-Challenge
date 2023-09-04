import sqlite3

file = open("AuthorBooklist.txt", "w")

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT Name from bookinfo")
for x in cursor.fetchall():
    print(x)

Select = input("""
Enter an author's name: """)

cursor.execute("SELECT * FROM books WHERE Author=?", [Select])
for x in cursor.fetchall():
    newrecord = str(x[0]) + "-" + x[1]+ "-" + x[2]+ "-" + str(x[3]) + "\n"
    file.write(newrecord)

file.close()
db.close()
