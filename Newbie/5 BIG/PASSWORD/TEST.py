def Create_Password():
    SpecialList = ["!", "£", "$", "%", "&", "<", "*", "@", "(", ")", "#", "=", "¡", "¿", "?", "/"]
    Score = 0
    Password = input("Enter a password: ")

    if len(Password) >= 8:
        Score = Score + 1

    if any(Password.islower() for x in Password):
        Score = Score + 1

    if any(Password.isupper() for x in Password):
        Score = Score + 1

    if any(Password.isdigit() for x in Password):
        Score = Score + 1

    if any(x in SpecialList for x in Password):
        Score = Score + 1


    elif Score <= 2:
        print("Weak Password")
        Repeat = input("You want to repeat (y/n): ")

        if Repeat == "y":
            Create_Password()
        else:
            print("Ok")


    elif Score <= 4:
        print("Weak Password, need a little more")
        Repeat = input("You want to repeat (y/n): ")

        if Repeat == "y":
            Create_Password()
        else:
            print("Ok")
    
    if Score == 5:
        print("Well Done")

    
Create_Password()