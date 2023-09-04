import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS bookinfo (
    Name TEXT NOT NULL,
    PlaceOfBirth TEXT NOT NULL);""")

cursor.execute("""INSERT INTO bookinfo (Name, PlaceOfBirth)
               VALUES('Agatha Christie', 'Torquay')""")
db.commit()

cursor.execute("""INSERT INTO bookinfo (Name, PlaceOfBirth)
               VALUES('Cecelia Ahern', 'Dublin')""")
db.commit()

cursor.execute("""INSERT INTO bookinfo (Name, PlaceOfBirth)
               VALUES('J.K. Rowling', 'Bristol')""")
db.commit()

cursor.execute("""INSERT INTO bookinfo (Name, PlaceOfBirth)
               VALUES('Oscar Wilde', 'Dublin')""")
db.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,
    Author TEXT NOT NULL,
    DatePublished INTEGER NOT NULL);""")

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(1, 'De Profundis', 'Oscar Wilde', 1905)""")
db.commit()

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(2, 'Harry Potter and the chamber of secrets', 'J.K. Rowling', 1998)""")
db.commit()

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(3, 'Harry Potter and the prisoner of Azkaban', 'J.K. Rowling', 1999)""")
db.commit()

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(4, 'Lyrebird', 'Cecelia Ahern', 2017)""")
db.commit()

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(5, 'Murder on the Orient Express', 'Agatha Christie', 1934)""")
db.commit()

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(6, 'Perfect', 'Cecelia Ahern', 2017)""")
db.commit()

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(7, 'The marble collector', 'Cecelia Ahern', 2016)""")
db.commit()

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(8, 'The murder on the links', 'Agatha Christie', 1923)""")
db.commit()

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(9, 'The picture of Dorian Gray', 'Oscar Wilde', 1890)""")
db.commit()

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(10, 'The secret adversary', 'Agatha Christie', 1921)""")
db.commit()

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(11, 'The seven dials mystery', 'Agatha Christie', 1929)""")
db.commit()

cursor.execute("""INSERT INTO books (id, Title, Author, DatePublished)
               VALUES(12, 'The year i met you', 'Cecelia Ahern', 2014)""")
db.commit()
