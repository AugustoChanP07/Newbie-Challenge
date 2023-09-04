
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]



def main():
    Again = True
    while Again == True:
        print("""
    1) Make a code
    2) Decode a Message
    3) Quit
        """)
        
        try:
            Selection = int(input("Enter your Selection: "))

            if Selection == 1:
                def Main_Make_Code():
                    Userinput_Word, Userinput_Number = Get_Data()
                    Make_Code(Userinput_Word, Userinput_Number)
                
                Main_Make_Code()
            
            elif Selection == 2:
                def Main_Decode():
                    Userinput_Word, Userinput_Number = Get_Data()
                    Decode(Userinput_Word, Userinput_Number)
                
                Main_Decode()
            
            elif Selection ==3:
                print("Good Bye")
                break
            
            else:
                print("Enter a valid Number")
        
        except ValueError:
            print("Please enter a valid Number, text is not allowed")

def Get_Data():
    Userinput_Word = input("Enter your word: ")
    Userinput_Word = Userinput_Word.lower()

    Userinput_Number = int(input("Enter a number (1-26): "))
    
    if Userinput_Number > 26 or Userinput_Number == 0:
        while Userinput_Number > 26 or Userinput_Number == 0:
            Userinput_Number = int(input("Enter a number (1-26): "))

    return Userinput_Word, Userinput_Number

def Make_Code(Userinput_Word, Userinput_Number):
    New_Word = ""
    for letter in Userinput_Word:
        N = alphabet.index(letter)
        N = N + Userinput_Number
        if N > 26:
            N = N - 27
        New_Letter = alphabet[N]
        New_Word = New_Word + New_Letter
    print(f"The new word is: {New_Word}")

def Decode(Userinput_Word, Userinput_Number):
    New_Word = ""
    for letter in Userinput_Word:
        N = alphabet.index(letter)
        N = N - Userinput_Number
        if N > 26:
            N = N - 27
        New_Letter = alphabet[N]
        New_Word = New_Word + New_Letter
    print(f"The new word is: {New_Word}")
        

main()

    