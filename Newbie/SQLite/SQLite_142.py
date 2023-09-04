import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

Place_Birth = input("Enter a place of birth: ")

cursor.execute("""SELECT books.Title, books.DatePublished, books.Author
               FROM books
               INNER JOIN bookinfo ON bookinfo.Name = books.Author
               WHERE bookinfo.PlaceOfBirth = ?""", [Place_Birth])

for x in cursor.fetchall():
    print(x)

db.close()
