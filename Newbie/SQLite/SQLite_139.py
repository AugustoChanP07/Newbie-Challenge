import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

#=============CREAR TABLA=============#
# cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
#     id integer PRIMARY KEY,
#     FirstName text NOT NULL,
#     Surname text NOT NULL,
#     PhoneNumber integer);""")

newID = input("Enter ID number: ")
First_Name = input("Enter FirstName: ")
Sur_Name = input("Enter Surname: ")
Phone_Number = int(input("Enter PhoneNumber: "))

cursor.execute("""INSERT INTO employees(id, FirstName, Surname, PhoneNumber)
                  VALUES(?,?,?,?)""", (newID, First_Name, Sur_Name, Phone_Number))

db.commit()
