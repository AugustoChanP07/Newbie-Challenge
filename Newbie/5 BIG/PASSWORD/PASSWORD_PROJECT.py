# PASSWORD --- PROJECT 
import csv

def menu():
    print("""
1) Create a new User ID
2) Change a password
3) Display all User IDs
4) Quit
""")
    again = True
    while again == True:
        try:
            Selection = int(input("Enter Selection: "))
            if Selection == 1:
                Create_NewUser_ID()
        
            elif Selection == 2:
                Change_password()
        
            elif Selection == 3:
                DisplayAll_ID()
            
            elif Selection == 4:
                again = False
                break

            else:
                print("Enter a value number")

        except ValueError:
            print("Not a Valid Number")
            

def Create_NewUser_ID():
    with open("PassWord.csv", "r") as file:
        existing_users = [line.strip().split(',')[0] for line in file]

    new_user_id = input("Enter a new User ID: ")
    if new_user_id in existing_users:
        print("User ID already exists")
    else:
        Create_Password(new_user_id)

def Create_Password(NewUser_ID):
    SpecialList = ["!", "£", "$", "%", "&", "<", "*", "@", "(", ")", "#", "=", "¡", "¿", "?", "/"]
    Score = 0
    Password = input("Enter a password: ")

    if len(Password) >= 8:
        Score = Score + 1

    if any(c.islower() for c in Password):
        Score = Score + 1

    if any(c.isupper() for c in Password):
        Score = Score + 1

    if any(c.isdigit() for c in Password):
        Score = Score + 1

    if any(c in SpecialList for c in Password):
        Score = Score + 1

    if Score <= 2:
        print("Weak Password")
    elif Score <= 4:
        print("Weak Password, need a little more")
    elif Score == 5:
        
        with open("PassWord.csv", "a") as file:
            Newrecord = NewUser_ID + ',' + Password + "\n"
            file.write(Newrecord)
        print("Has been Added!")


def DisplayAll_ID(): 
    file = open("PassWord.csv", "r")
    num = 1
    for row in file:
        print(num,row)
        num = num + 1
    file.close()

def Change_password():
    file = list(csv.reader(open("PassWord.csv")))
    tmp = []
    for x in file:
        tmp.append(x)
    
    ask_Name = True
    userID = ""
    while ask_Name == True:
        searchID = input("Enter the user ID you are looking for ")
        inlist = False
        row = 0
        for x in tmp:
            if searchID in tmp[row][0]:
                inlist = True
                break
            row = row + 1
        if inlist == True:
            userID = searchID
            ask_Name = False
        else:
            print(f"{searchID} is not in the list")
        
        if userID != "":
            password = Create_Password(userID)
            if password is not None:  # Verificar si la contraseña es válida antes de actualizarla
                password = str(password)
                ID = tmp[row].index(userID)
                tmp[row][1] = password
                with open("PassWord.csv", "w") as file:
                    for record in tmp:
                        newrecord = ",".join(record) + "\n"
                        file.write(newrecord)

menu()