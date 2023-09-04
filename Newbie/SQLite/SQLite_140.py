import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()


def View_PhoneBook():
    cursor.execute("SELECT * FROM employees")
    for x in cursor.fetchall():
        print(x) 


def Add_PhoneBook():
    newID = input("Enter ID number: ")
    First_Name = input("Enter FirstName: ")
    Sur_Name = input("Enter Surname: ")
    Phone_Number = int(input("Enter PhoneNumber: "))

    cursor.execute("""INSERT INTO employees(id, FirstName, Surname, PhoneNumber)
                    VALUES(?,?,?,?)""", (newID, First_Name, Sur_Name, Phone_Number))

    db.commit()


def Search_Surname():
    FindSurname = input("Enter a Surname: ")
    cursor.execute("SELECT * FROM employees WHERE Surname=?", [FindSurname])
    for x in cursor.fetchall():
        print(x)


def Delete_PhoneBook():
    Delete_id = input("Enter the id you want to delete: ")
    cursor.execute(f"DELETE FROM employees WHERE id={Delete_id}")
    
    cursor.execute("SELECT * FROM employees")
    for x in cursor.fetchall():
        print(x)



def main():

    Again = True

    while Again == True:
        print("""
    1) View phone book
    2) Add to phone book
    3) Search for  surname
    4) Delete person from phone book
    5) Quit
    """)
        Select = int(input("Enter your Selection: "))
        if Select == 1:
            View_PhoneBook()
        
        elif Select == 2:
            Add_PhoneBook()
        
        elif Select == 3:
            Search_Surname()
        
        elif Select == 4:
            Delete_PhoneBook()
        
        elif Select == 5:
            Again == False
            break

main()