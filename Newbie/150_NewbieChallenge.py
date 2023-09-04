

def C_001(): 
    Your_Name= input("Your name is: ")

    print(f"Hello {Your_Name}")

def C_002():
    FirstName = input("Whats your first name?")
    Surname = input("Whats your surname?")

    print(f"Hi {FirstName} {Surname}, its nice to meet you")

def C_003(): 
    input("What do you call a bear with no teeth?\nA Gummy bear")

def C_004():
    number_1 = int(input("Number 1 is: "))
    number_2 = int(input("Number 2 is: "))

    Sum = number_1 + number_2

    print(f"The sum of {number_1} and {number_2} is {Sum}")
    
def C_005():
    number_1 = int(input("Number 1 is: "))
    number_2 = int(input("Number 2 is: "))
    number_3 = int(input("Number 3 is: "))

    Sum = number_1 + number_2

    Answer = Sum * number_3

    print(Answer)

def C_006():
    Original_Slices = int(input("How many slices were in the begining?"))
    Eaten_slices = int(input("How many slices you ate?"))

    Left_Slices = Original_Slices - Eaten_slices

    print(f"there are {Left_Slices} slices left")

def C_007():
    Name = input("What's your name?")
    Age = int(input("What's your age?"))
    NewAge = Age + 1

    print(f"{Name} next birthday you will be {NewAge}.")

def C_008 ():
    TotalBill = int(input("What's the price of the bill?"))

    Dinners = int(input("How many dinners are?"))

    Billper_Person = TotalBill / Dinners 

    print(f"Each person should pay {Billper_Person}")

def C_009():
    Number_ofdays = int(input("Number of Days:"))

    Hours= 24 * Number_ofdays
    Minutes = 1440 * Number_ofdays
    Seconds = 86400 * Number_ofdays

    print(f"In {Number_ofdays} days, there are {Hours} hours, {Minutes} minutes and {Seconds} seconds")

def C_010(): 
    Kilograms =  int(input("Convert Kilograms to pounds: "))

    Pounds = 2204

    Result = int(Kilograms * Pounds)

    print(f"{Kilograms} kilograms equals to {Result} pounds")

def C_011():
    Number1 = int(input("Enter a number above 100: ")) 
    Number2 = int(input("Enter a number under 10: "))

    answer = Number1/Number2
    
    print(answer)

def C_012():
    number1 = int(input("Enter number 1: "))
    number2 = int(input("Enter number 2: "))
    if number1 > number2: 
        print(number2, number1)
    else: 
        print(number1, number2)

def C_013():
    Number = int(input("Enter a number under 20: "))
    if Number > 20:
        print("Too High")
    else: 
        print("Thank you")

def C_014(): 
    Number = int(input("Enter a number: "))

    if Number > 10 and Number < 20:  
        print("Thank you")

    else: 
        print("Incorrect answer")

def C_015(): 
    Favourite_Color = str(input("Favourite colors: "))

    if Favourite_Color == ["red", "RED", "Red"]:
        print("I like Red too")
    else: 
        print(f"I dont like {Favourite_Color} color")

def C_016(): 
    User_Input = str(input("It's rainny outside? "))
    User_Input = str.lower(User_Input)
    if User_Input == "yes":
        Windy = input("its windy? ")
        Windy = str.lower(Windy)
        if Windy == "yes":
            print("It is too windy for an umbrella")
        else: 
            print("Take an umbrella")
    else: 
        print("Enjoy your day")

def C_017():
    UserAge = int(input("How old are you? "))

    if UserAge >= 18: 
        print("You can vote")
    elif UserAge == 17: 
        print("You can learn to drive")
    elif UserAge == 16: 
        print("You can buy a lottery ticket")
    else: 
        print("You can go Trick- or -Treating")

def C_018(): 
    Number = int(input("Please enter a number: "))

    if Number < 10: 
        print("Too Low")
    elif Number >= 10 and Number <= 20:
        print("Correct")
    else: 
        print("Too High")

def C_019():
    Number = int(input("Please enter 1, 2 or 3: "))

    if Number == 1: 
        print("Thank You")
    elif Number == 2: 
        print("Well Done")
    elif Number == 3: 
        print("Correct")
    else: 
        print("Error Message")

def C_020(): 
    Name = str(input("Enter first Name: "))
    print(len(Name))

def C_021():
    FirstName = str(input("Enter your first Name: "))
    SecondName = str(input("Enter your second Name: "))

    FullName= FirstName + " " + SecondName 
    Length = len(FullName)

    print(f"Your name is {FullName} and the lenght is {Length}")

def C_022(): 
    FirstName = input("Enter your first name in lower case: ")
    SecondName = input("Enter your surname in lower case: ")

    FirstName = FirstName.title()
    SecondName = SecondName.title()

    FullName = FirstName + " " + SecondName
    print(FullName)

def C_023(): 
    First_Line = input("Enter the first line of a nursery rhyme: ")
    Length = len(First_Line)
    print(f"The legnth is {Length}")
    StartingNumber = int(input("Enter a staring Number: "))
    EndingNumber = int(input("Enter an ending Number: "))

    Part= (First_Line [StartingNumber:EndingNumber])
    print(Part)

def C_024(): 
    Word = input("Enter a word: ")
    print(Word.upper())

def C_025():
    FirstName = input("PLease enter your First Name: ")
    Length_FirstName = len(FirstName)

    if Length_FirstName <= 5: 
        Surname = input("Enter your surname: ")
        FullName = FirstName + Surname
        print(FullName.upper())
    else: 
        print(FirstName.lower())

def C_026():
    word = input("Enter a word: ")
    first = word[0]
    length = len(word)
    rest = word[1:length]
    if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
        newword = rest + first + "ay"
    else:
        newword = word + "way"
    print(newword.lower())

def C_027():
    Number = float(input("Enter a number with lots of decimals: "))

    New_Number = Number * 2 

    print(New_Number)

def C_028(): 
    Number = float(input("Enter a number with lots of decimals: "))

    New_Number = round(Number * 2, 2) 

    print(New_Number)

def C_029():
    import math 

    Number = float(input("Enter a number over 500: "))
    Sqrt = math.sqrt(Number)
    Output = round(Sqrt,2)
    print(Output)

def C_030():
    import math
    print(round(math.pi,5))

def C_031():
    import math

    RadiusCircle = float(input("Enter the radius of a circle: "))
    AreaCircle = (RadiusCircle**2) * math.pi
    print(AreaCircle)

def Empezastedebesterminar52C_032():
    import math

    RadiusCircle =int(input("Enter the radius of the circle: "))
    Depth = int(input("Enter the depth: "))
    AreaCircle = (RadiusCircle**2) * math.pi
    Volume = AreaCircle * Depth
    print(round(Volume, 3))

def C_033():
    Number1 = int(input("Enter a number: "))
    Number2 = int(input("Enter the divider: "))
    Result = Number1 / Number2
    Remainder = Number1 % Number2
    print(f"{Number1} divided by {Number2} is {Result} with {Remainder} remaining")

def C_034():
    print("""
    1) Square
    2) Triangle 
    """)

    Input = int(input("Enter a Number: "))
    if Input == 1: 
        side = int(input("Enter the side: "))
        Area = side * side
        print(Area)
    elif Input == 2: 
        Base = int(input("Enter the base: "))
        Height =  int(input("Enter the height: "))
        Area = Base * Height
        print(Area)
    else: 
        print("Error")
def C_035():
    Name = input("Enter your name: ")
    for name in range(3):
        print(Name)

def C_036():
    Name = input("Enter your name: ")
    Number = int(input("Enter number of times the name will repeat: "))
    for i in range(0,Number):
        print(Name)

def C_037():    
    Name = input("Enter your name: ")
    for i in Name:
        print(i)

def C_038():
    Name = input("Enter your name: ")
    Number = int(input("Enter number of times the name will repeat: "))
    for i in range(0,Number): 
        for i in Name:
            print(i)

def C_039(): 
    Number = int(input("Please enter a number between 1 and 12: "))
    for i in range(1,13):
        answer = i * Number
        print(f"{i} x {Number} = {answer}") 

def C_040(): 
    Input = int(input("Enter a numver below 50: "))
    for i in range(50,Input-1, -1):
        print(i)

def C_041():
    Name = input("Enter your name: ")
    Number = int(input("Enter a number: "))
    if Number < 10: 
        for i in range(0,Number):
            print(Name)
    else: 
        for i in range(0,3):
            print("Too High")

def C_042 ():
    Total = 0
    for x in range(0,5):
        Number = int(input("Enter a number: "))
        Add = input("Want to include: ")
        if Add == "Yes" or "yes":
            Total = Total + Number
    print(Total)

def C_043 ():
    User_Input = input("Up or Down: ")
    Number = int(input("enter a number: "))
    if User_Input == "Up":
        for x in range(1, Number + 1):
            print(x)
    elif User_Input == "Down":
        for x in range(Number,0,-1):
            print(x)
def C_044(): 
    Party = int(input("How many people you want to invite to the party: "))
    if Party <10: 
        for i in range(0,Party):
            Name = input("Enter the name: ")
            print(F"{Name} has been invited.")
    elif Party >= 10:
        print("Too many people")

def C_045():
    total = 0 
    while total <= 50:
        Number= int(input("Enter a number: "))
        total = total + Number
        print(f"The total is {total}")

def C_046():
    Number = 0
    while Number < 5:
        Number = int(input("Enter a number: "))
    print(f"The last number you entered was {Number}")

def C_047():
    #Improved version
    Number_1 = int(input("Enter number 1: "))
    Number_2 = int(input("Enter number 2: "))
    Total = Number_1 + Number_2

    Number_Add = input("You want to add another number? (y/n): ")

    while Number_Add == "y":
        New_Number = int(input("Enter new number: "))
        Number_Add = input("You want to add another number? (y/n): ")
        Total = Total + New_Number
    print(Total)

def C_048():
    Another = "yes"
    Party = 0 
    while Another == "yes":
        Name = input("The name: ")
        print(f"{Name} has been invited to the party")
        Party= Party + 1 
        Another =input("Do you wanto invite another: ")
    print(f"You have {Party} people coming to the party")

def C_048_Alternative():
    count = 0
    party = True
    while party == True: 
        Ask = input("enter the name: ")
        print(f"{Ask} has been invited")
        count = count + 1
        More = input("Do you want to enter a nother person? (y/n): ")
        if More == "y":
            party == True
        else: 
            print(f"you have {count} coming to your party")
            party == False
            break

def C_049():
    Compnum_Value = 50 
    Number = int(input("Enter a number: "))
    count = 1

    while  Number != Compnum_Value:
        
        if Number > Compnum_Value:
            print("Too high")
        else: 
            print("Too low")
        
        count = count + 1
        Number= int(input("Have another try: "))
        

    print(f"Well done, you took {count} tries")

def C_050():
    Number = int(input("Please enter a number between 10 and 20: "))
    while Number < 10 or Number > 20: 
        if Number < 10: 
            print("Too low")
        else:
            print("Too High")
        Number=int(input("Try again: "))
    print("Thank you")

def C_052():
    import random 
    num = random.randint(1,100)
    print(num)

def C_053():    
    import random 

    Fruit = random.choice(["Pera", "Banana", "Apple", "Dragonfruit", "Mango"])
    print(Fruit)

def C_054():
    import random 
    Heads_Tails =   random.choice(["Head", "Tails"])
    Choice = input("Enter Head or Tails: ")
    if Heads_Tails == Choice:
        print("You Win!")
    else: 
        print("You lose")

def C_055():
    import random 
    Random_Num = random.randint(1,5)
    User_Input = int(input("Enter a number: "))
    if User_Input == Random_Num:
        print("Well Done")

    elif  User_Input > Random_Num:
        print("Too High")
        User_Input = int(input("Enter a number: "))
        if User_Input == Random_Num:
            print("Correct")
        else:
            print("You Lose")

    elif User_Input < Random_Num:
        print("Too Low")
        User_Input = int(input("Enter a number: "))
        if User_Input == Random_Num:
            print("Correct")
        else:
            print("You Lose")

def C_056(): 
    import random 
    Random_Num = random.randint(1,10)
    Number= 0 
    while Number != Random_Num:
        Number = int(input("Enter a number: "))
        print("No...")
    print("You did it")

def C_057(): 
    import random 
    Random_Num = random.randint(1,10)
    correct = False
    while correct == False:
        guess = int(input("Enter a number: "))
        if guess == Random_Num:
            correct = True
            print("You did it!")
        elif guess > Random_Num: 
            print("Too High")
        else:
            print("Too low")

def C_058():
    import random

    points = 0

    for x in range(0,5):
        Random_1 = random.randint(1,10)
        Random_2= random.randint(1,10)
        total = Random_1 + Random_2
        print(f"{Random_1} + {Random_2} is= ")
        Question = int(input("Your Answer is: "))
        print()
        if Question == total:
            points = points + 1

    print(f"You have {points} out of 5")

def C_59():
    import random

    ColourRandom = random.choice(["red", "black", "white", "blue", "green"])
    print("Please choose one of these colors: red, black, white, blue, green")
    User = input("Please enter a colour: ")


    while ColourRandom != User:
        User = input("Have another try: ")
        if ColourRandom == User: 
            print("Well Done")
            break

        else: 
            if ColourRandom == "red": 
                print("I bet yout are seeing RED RIGHT NOW") 
            elif ColourRandom == "blue":
                print("Don't feel BLUE")
            elif ColourRandom == "black":
                print(".... and white")
            elif ColourRandom == "green":
                print("Don't like mowing the lawn? ")
            elif ColourRandom == "White":
                print("Black and ...")

def C_060():
    import turtle

    for i in range (0,4):
        turtle.forward(100)
        turtle.right(90)
def C_061():
    import turtle

    for i in range (0,3):
        turtle.forward(100)
        turtle.right(120)

def C_062():
    import turtle

    for i in range (0,360):
        turtle.forward(1)
        turtle.right(1)

def C_063():
    import turtle

    turtle.color("black", "red")
    turtle.begin_fill()

    for i in range (0,4):
        turtle.forward(100)
        turtle.right(90)
    turtle.penup()
    turtle.end_fill()
    turtle.forward(130)

    turtle.pendown()
    turtle.color("black", "green")
    turtle.begin_fill()

    for i in range (0,4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

    turtle.exitonclick()

def C_064():
    import turtle

    turtle.shape("turtle")

    for line in range(0,5):
        turtle.left(216)
        turtle.forward(200)
    turtle.exitonclick()

def C_065():
    import turtle
    #NUMBER ONE
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    #MOVE 
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()

    #NUMBER TWO
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward (70)

    #MOVE 
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()

    #NUMBER 3
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(70)
    turtle.right(180)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(70)


    turtle.exitonclick()

def C_066():
    import turtle 
    import random

    turtle.shape("turtle")
    turtle.pensize(4)


    for line in range(0,8):
        turtle.color(random.choice(["red", "blue", "black", "gray", "orange", "yellow"]))
        turtle.forward(70)
        turtle.right(45)

    turtle.exitonclick()

def C_067():
    import turtle 

    turtle.shape("turtle")

    for x in range(0,10):
        turtle.right(36)
        for line in range(0,8): 
            turtle.forward(70)
            turtle.right(45)

    turtle.exitonclick()

def C_068():
    import turtle 
    import random 

    turtle.shape("turtle")

    Random_Forward = random.randint(40,100)
    Random_Grades = random.randint(30,50)
    random_Num = random.randint(5,10)

    for x in range(0,random_Num):
        turtle.right(Random_Grades)
        for line in range(0,random_Num): 
            turtle.forward(Random_Forward)
            turtle.right(Random_Grades)

    turtle.exitonclick()

def C_069():
    Countries = ("México", "Japón", "Hungria", "Rusia", "Kenia")

    for i in Countries:
        print(i)

    User = input("Please select a country: ")
    print(Countries.index(User))

def C_070():
    Countries = ("México", "Japón", "Hungria", "Rusia", "Kenia")

    for i in Countries:
        print(i)

    User = int(input("Please enter a number: "))
    print(Countries[User])

def C_071():
    Sports = ["MMA", "Boxing"]

    Sports.append(input("What's your favorite Sport: "))

    print(sorted(Sports))

def C_072():
    Subjects = ["Math", "Spanish", "Physics", "Chemestry", "Finance", "Administration"]


    for x in Subjects:
        print(x)
        
    User = Subjects.remove(input("Select the one you dont like: "))

    print(Subjects)

def C_073():
    Food_Dictionary = {}
    Food1 = input("Enter a food you like: ")
    Food_Dictionary[1] = Food1

    Food2 = input("Enter a food you like: ")
    Food_Dictionary[2] = Food2

    Food3 = input("Enter a food you like: ")
    Food_Dictionary[3] = Food3

    Food4 = input("Enter a food you like: ")
    Food_Dictionary[4] = Food4

    print(Food_Dictionary)

    dislike = int(input("Which of these do you want to get rid of? "))

    del Food_Dictionary[dislike]
    print(sorted(Food_Dictionary.values()))


def C_074():
    Colors = ["Blanco", "Negro", "Azul", "Amarillo", "Naranja", "Verde", "Rosado", "Violeta", "Dorado", "Purpura"]
    Start = int(input("Enter a number between 0 an 4: "))
    Ending = int(input("Enter a number between 5 and 9: "))
    print(Colors[Start:Ending])

def C_075():
    Numbers = [34,56,78]
    for x in Numbers:
        print(x)

    User = int(input("Please enter a number: "))
    if User in Numbers:
        print(Numbers.index(User))
    else:
        print("That is not in the list")

def C_076(): 
    Party = []
    for x in range (0,3):
        Party.append(input("Add a person to the party: "))

    print(sorted(Party))

    More_Party = input("Do you want to invite other people: ")

    while More_Party == "y":
        Party.append(input("Ad a name: "))
        More_Party = input("Do you want to invite other people: ")

    print(Party)

def C_077():
    Party = []
    for x in range (0,3):
        Party.append(input("Add a person to the party: "))

    print(sorted(Party))

    More_Party = input("Do you want to invite other people: ")

    while More_Party == "y":
        Party.append(input("Ad a name: "))
        More_Party = input("Do you want to invite other people: ")

    print(Party)

    User = input("Please enter a person: ")
    print(Party.index(User))

    Remove_Party = input("Do you want that person in the party: ")
    if Remove_Party == "no":
        Remove_Party = Party.remove(User)
        print(Party)
    else:
        print(Party)

def C_078():
    Programmes = ["Avatar", "Moon Knight", "Iron Fist", "Black Mirror"]
    User = Programmes.append(input("Ad a TV programme: "))
    Position = int(input("In which position you want to put it: "))

    Programmes [Position] = User

    for x in range (Programmes):
        print(x)

def C_079():
    num = []
    for x in range(0,3):
        User = num.append(int(input("Enter a num: ")))
        print(num)

    Ask = input("Still want the last num? ")
    if Ask == "n":
        del num[2]
        print(num)

    else: 
        print(num)

def C_080():
    FirstName= input("Please enter your first Name: ")
    print(len(FirstName))

    SurName = input("Please enter your second Name: ")
    print(len(SurName))

    FullName = FirstName + " " + SurName

    print(FullName)
    print(len(FullName))


def C_081():
    User = input("Enter your favorite subject: ")

    for x in User:
        print (x, end="-") 

def C_082():
    Poem = "There's a bluebird in my heart that"
    print(Poem)

    Start = int(input("Please enter from a start: "))
    End = int(input("Please enter from a end: "))

    print(Poem[Start:End])

def C_083():
    User = input("Enter a word in upper case: ")
    tryagain = False

    while tryagain == False:
        if User.isupper():
            print("WELL DONE")
            tryagain = True
        else:
            print("Try again")
            User = input("Enter a word in upper case: ")

def C_084():
    post_Code = input("Enter your postcode: ")
    start = post_Code[0:2]
    print(start.upper())

def C_085():
    Name = input("Enter your name: ")
    count = 0 
    Vowels = ("a", "e", "i", "o", "u")
    Name = Name.lower()
    for x in Name: 
        if x in Vowels:
            count = count + 1
    print(f"There are {count} vowels")

def C_086():
    Psw_1 = input("Enter your Password: ")
    Psw_2 = input("Enter your Password again: ")

    if Psw_1 == Psw_2:
        print("Thank You")

    if Psw_1.lower() == Psw_2.lower():
        print("They must be in the same case")
    else:
        print("Enter Again")

def C_087():
    Word = input("Please enter a Word: ")
    lenght = len(Word)
    num = 1

    for x in Word:
        position = lenght - num
        letter = Word[position]
        print(letter)
        num = num + 1       

def C_088():
    from array import array

    Num = array('i', [])

    for x in range(0,5):
        NewValue = int(input("Enter a number: "))
        Num.append(NewValue)

    Num = sorted(Num)
    Num.reverse()

    print(Num)

def C_089():
    from array import array
    import random

    Num = array('i', [])

    for i in range (0,5):
        Rand_Num = random.randint(1,25)
        Num.append(Rand_Num)

    for x in Num:
        print(x)

def C_090():
    from array import array

    Array = array('i', [])

    while len(Array) < 5:
        User = int(input("Enter a number between 10 and 20: "))        
        if User >= 10 and User <= 20:
            Array.append(User)
        else: 
            print("Outside the range")

    print("Thank you")
    for x in Array:
        print(x)

def C_091():
    from array import array
    import random

    Num = array('i', [])

    for i in range (0,5):
        Rand_Num = random.randint(1,5)
        Num.append(Rand_Num)

    for x in Num:
        print(x)

    User = int(input("Enter a number from the array: "))
    Count = Num.count(User)

    print(f"That number repeats {Count} times")

def C_092():
    from array import array
    import random

    Random_Array = array('i', [])
    User_Array = array('i', [])

    while len(User_Array) < 3:
        User = int(input("Enter a number: "))
        User_Array.append(User)

    for i in range (0,5):
        Rand_Num = random.randint(1,25)
        Random_Array.append(Rand_Num)

    User_Array.extend(Random_Array)

    for x in User_Array:
        print(x)

def C_093():
    from array import array 

    Array = array('i', [])

    for x in range (0,5):
        User = int(input("Enter a number: "))
        Array.append(User)

    print(sorted(Array))

    Select = int(input("Select a number to remove: "))
    Array.remove(Select)

    print(sorted(Array))


def C_094():
    from array import array

    Array = array('i', [5,4,3,2,1])

    for i in Array:
        print(i)

    User = int(input("Enter a number: "))

    if User in Array:
        print(f"This is in position {Array.index(User)}")
    else: 
        print("Not in array")


def C_095():
    from array import array
    import math

    Array = array('f', [38.67, 67.67, 76.45, 45.76, 99.99])

    tryagain = True

    while tryagain== True:
        num = int(input("Enter a number between 2 and 5: "))
        if num<2 or num >5:
            print("Incorrect vale, try again")
        else:
            tryagain = False

    for i in range(0,5):
        ans = Array[i]/num
        print(round(ans, 2))

def C_096():
    Simple_Array = [[2,5,8], [3,7,4], [1,6,9], [4,2,0]]
    print(Simple_Array)

def C_097():
    Simple_Array = [[2,5,8], [3,7,4], [1,6,9], [4,2,0]]
    print(Simple_Array)
    User = int(input("Please enter a row to print: "))

    print(Simple_Array[User])

def C_098():
    Simple_Array = [[2,5,8], [3,7,4], [1,6,9], [4,2,0]]
    print(Simple_Array)

    Row = int(input("Please enter a row to print: "))

    print(Simple_Array[Row])

    User = int(input("Please enter a new value: "))
    Simple_Array[Row].append(User)

    print(Simple_Array[Row])
       
def C_099():
    Simple_Array = [[2,5,8], [3,7,4], [1,6,9], [4,2,0]]
    print(Simple_Array)

    Row = int(input("Please enter a row to print: "))

    print(Simple_Array[Row])

    Change = input("You want to change value from the row: ")

    if Change == "y":
        User = int(input("Please enter a new value: "))
        Simple_Array[Row].append(User)
    else: 
        print("Ok")
        
    print(Simple_Array[Row])

def C_100():
    Data_Set = {
    "John":{"N":3056, "S":8463, "E":8441, "W":2694}, 
    "Tom":{"N":4832, "S":6786, "E":4737, "W":3612}, 
    "Anne":{"N":5239, "S":4802, "E":5820, "W":1859}, 
    "Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}
    }

def C_101():
    Data_Set = {
    "John":{"N":3056, "S":8463, "E":8441, "W":2694}, 
    "Tom":{"N":4832, "S":6786, "E":4737, "W":3612}, 
    "Anne":{"N":5239, "S":4802, "E":5820, "W":1859}, 
    "Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}
    }

    Name = input("Enter a person name: ")
    Region = input("Select a region: ")

    print(Data_Set[Name][Region])

    NewData = int(input("Enter new data: "))
    Data_Set[Name][Region] = NewData
    #Estas diciendo que de la columna de nombre, y de esa region será la newdata
    print(Data_Set[Name])
    #Imprimes la columna del data set

def C_102():
    from array import array

    Data_set = {}

    for x in range(0,4):
        Name = input("Enter a name: ")
        Age = int(input("Enter the age: "))
        Shoe = int(input("Enter a shoe size: "))
        Data_set[Name] = {"Age": Age, "Shoe": Shoe}

    User = input("Enter a name to display the row: ")
    print(Data_set[User])

def C_103():
    
    Data_set = {}

    for x in range(0,4):
        Name = input("Enter a name: ")
        Age = int(input("Enter the age: "))
        Shoe = int(input("Enter a shoe size: "))
        Data_set[Name] = {"Age": Age, "Shoe": Shoe}

    for Name in Data_set: 
        print((Name), Data_set[Name]["Age"])

def C_104():
        
    Data_set = {}

    for x in range(0,4):
        Name = input("Enter a name: ")
        Age = int(input("Enter the age: "))
        Shoe = int(input("Enter a shoe size: "))
        Data_set[Name] = {"Age": Age, "Shoe": Shoe}

    Remove = input("Enter a Name you want to remove: ")
    del Data_set[Remove]

    for Name in Data_set:
        print((Name), Data_set[Name] ["Age"], Data_set[Name]["Shoe"])

def C_105():
    File = open("Numbers.txt", "w")

    File.write("2, ")
    File.write("4, ")
    File.write("6, ")
    File.write("8, ")
    File.write("10, ")

    File.close()

def C_106():
    File = open("Names.txt", "w")

    File.write("Ryu Narushima \n")
    File.write("Naoto Sugawara \n")
    File.write("Isaac \n")
    File.write("Julio Chavez \n")
    File.write("Maria Gil \n")

    File.close() 

def C_107():
    File = open("Names.txt", "r")
    print(File.read())

def C_108():
    File = open("Names.txt", "a")

    User = input("Enter a name: ")

    File.write(User)
    File.close()

    File = open("Names.txt", "r")
    print(File.read())

    File.close()

def C_109():
    MENU = int(input("""
    1) Create a new file
    2) Display the file
    3) Add a new item to the file 

    Make a selection 1, 2, or 3: """))

    if MENU == 1:
        File = open("Subject.txt", "w")
        User = input("Enter a school subject: ")
        File.write(User + "\n") 
        File.close()

    elif MENU == 2:
        File = open("Subject.txt", "r")
        print(File.read())

    elif MENU == 3:
        File = open("Subject.txt", "a")

        User = input("Enter a New school subject: ")

        File.write(User + "\n")
        File.close()

        File = open("Subject.txt", "r")
        print(File.read())

        File.close()

    else: 
        print("Invalid Option")

def C_110():
    file = open("Names.txt", "r")
    print(file.read())
    file.close()

    file = open("Names.txt", "r")
    selectedname = input("Enter a name from the list: ")
    selectedname = selectedname + "\n"

    for row in file: 
        if row != selectedname:
            file = open("Names2.txt", "a")
            newrecord = row
            file.write(newrecord)
            file.close()
    file.close() 

def C_111():
    import csv 

    file = open ("Books.csv", "w")
    NewRecord = "To Kill A Mocking Bird, Harper Lee, 1960\n"
    file.write(str(NewRecord))

    NewRecord = "A Brief History of Time, Stephen Hawking, 1988\n"
    file.write(str(NewRecord))

    NewRecord = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
    file.write(str(NewRecord))

    NewRecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
    file.write(str(NewRecord))

    NewRecord = "Pride and Prejudice, Jane Austen, 1813\n"
    file.write(str(NewRecord))

    file.close()

def C_112 ():
    import csv

    file  = open ("Books.csv", "a")

    Book = input("Enter a Book name: ")
    Author = input("Enter the autor: ")
    Year = str(input("Enter the year was released: "))

    New_record = Book + "," + Author + "," + Year + "\n"

    file.write(str(New_record))

    file.close()

    file  = open ("Books.csv", "r")
    for row in file: 
        print(row)

    file.close()

def C_113():
    import csv

    Append = int(input("Number of books you want to enter: "))
    file  = open ("Books.csv", "a")

    for x in range(0,Append):
        Book = input("Enter a Book name: ")
        Author = input("Enter the autor: ")
        Year = str(input("Enter the year was released: "))
        New_record = Book + "," + Author + "," + Year + "\n"
        file.write(str(New_record))

    file.close()


    file  = open ("Books.csv", "r")
    search = input("Enter the Name of the Book your want to search: ")
    reader = csv.reader(file)
    count = 0 

    for row in file: 
        if search in str(row):
            print(row)
            count = count + 1
    if count == 0:
            print("No Book in this Database")
    file.close()

def C_114():
    import csv 

    start = int(input("Enter a starting year: "))
    end = int(input("Enter an end year: "))

    file = list(csv.reader(open("Books.csv")))
    tmp = []

    for row in file: 
        tmp.append(row)

    x = 0
    for row in tmp:
        if int(tmp[x] [2]) >= start and int(tmp[x] [2]) <= end:
            print(tmp[x])
        x = x + 1

def C_115():
    import csv 

    file = open("Books.csv", "r")
    count = 0

    for row in file:
        print(f"Row: {str(count)} - {row}")
        count = count + 1

def C_116():
    import csv 

    file = list(csv.reader(open("Books.csv")))
    Booklist = []
    for row in file:
        Booklist.append(row)

    x = 0
    for row in Booklist:
        Display = x,Booklist[x]
        print(Display)
        x = x + 1
    getrid = int(input("Enter a row number to delete: "))
    del Booklist[getrid]

    x = 0
    for row in Booklist:
        Display = x,Booklist[x]
        print(Display)
        x = x + 1
    alter = int(input("Enter a row number to alter: "))
    del Booklist[alter]

    part = int(input("Which part do you want to change? "))
    newdata = input("Enter new data: ")
    Booklist[alter][part] = newdata
    print(Booklist[alter])

    file = open("Books.csv", "w")
    x = 0
    for row in Booklist:
        newrecord = Booklist[x][0] + ", " + Booklist[x][1] + ", " + Booklist[x][2] + "\n"
        file.write(newrecord)
        x = x + 1
    file.close()

def C_117():
    import csv 
    import random

    score = 0 
    name = input("What is your name: ")
    ql_num1 = random.randint(10,50)
    ql_num2 = random.randint(10,50)
    question1 = str(ql_num1) + " + "  + str(ql_num2) + " - "
    ans1 = int(input(question1))
    realans1 = ql_num1 + ql_num2
    if ans1 == realans1:
        score = score + 1


    q2_num1 = random.randint(10,50)
    q2_num2 = random.randint(10,50)
    question2 = str(q2_num1) + " + "  + str(q2_num2) + " - "
    ans2 = int(input(question2))
    realans2 = q2_num1 + q2_num2
    if ans2 == realans2:
        score = score + 1

    file = open("QuizScore.csv", "a")
    newrecord = name + " , " + question1 + "," + str(ans1) + "," + question2 + " , " + str(ans2) + "," + str(score) + "\n"
    file.write(str(newrecord))

    file.close()

def c_118():
    def Get_Num():
        Num = int(input("Enter a number: "))
        return Num

    def Loop(Num):
        for x in range(1,Num + 1):
            print(x)

    def Main ():
        Num = Get_Num()
        Loop(Num)

    Main()

def C_119():
    import random

    def Create_Comp():
        Number_Low = int(input("Enter a low number: "))
        Number_High = int(input("Enter a high number: "))
        Comp_Num = random.randint(Number_Low,Number_High)
        return Comp_Num

    def Instruction():
        print("I am thinking of a number...")
        guess = int(input("Enter the number i am thinking: "))
        return guess

    def Check (Comp_Num, guess):
        while guess != Comp_Num:
            guess = int(input("Have another try: "))
            if guess == Comp_Num:
                print("Correct, you win")
            
            elif guess < Comp_Num:
                print("Too Low")
            else: 
                print("Too High")

    def Main():
        Num  = Create_Comp()
        Ins = Instruction()
        Check(Num, Ins)

    Main()

def C_120():
    import random

    def Sub_Num1():
        Rand1 = random.randint(5,20)
        Rand2 = random.randint(5,20)
        Correct_Answer = Rand1 + Rand2
        User_Anser = int(input(f"Enter a sum of {Rand1} and {Rand2}: "))
        Answer = (Correct_Answer, User_Anser)
        return Answer

    def Sub_Num2():
        Rand1 = random.randint(25,50)
        Rand2 = random.randint(1,25)
        Correct_Answer = Rand1 - Rand2
        User_Anser = int(input(f"{Rand1} minus {Rand2} is: "))
        Answer = (Correct_Answer, User_Anser)
        return Answer

    def Check(Correct_Answer, User_Anser):
        if User_Anser == Correct_Answer:
            print("Correct")
        elif User_Anser != Correct_Answer:
            print(f"Incorrect the answer is {Correct_Answer}")

    def Main():
        print("""
    1) Addition 
    2) Substraction
            """)
        Selection = int(input("Enter 1 or 2: "))
        if Selection == 1:
            Correct_Answer, User_Anser = Sub_Num1()
            Check(Correct_Answer, User_Anser)
        elif Selection == 2:
            Correct_Answer, User_Anser = Sub_Num2()
            Check(Correct_Answer, User_Anser)
        else: 
            print("Incorrect Selection")

    Main()

def C_121():
    def Add_Name():
        Name = input("Enter a new Name: ")
        Name_List.append(Name)
        print(Name_List)
        return Name_List

    # View all the names 
    def View_Names():
        num = 0
        for x in Name_List:
            print(num, x)
            num= num + 1

    # Change Name
    def Change_Name():
        num = 0
        for x in Name_List:
            print(num, x)
            num= num + 1
        Select_num = int(input("Enter the number of the name you want to change: "))     
        Name = input("Enter new name: ")
        Name_List[Select_num] = Name
        return Name_List

    # Delete Name
    def Delete_Name():
        num = 0
        for x in Name_List:
            print(num, x)
            num= num + 1
        Delete = input("Enter the name want to delete: ")
        Name_List.remove(Delete)
        return Name_List

    # Main
    def main():
        repeat = "Y"
        while repeat == "Y":
            print("""
                1) Add a name
                2) Change a name
                3) Delete a name
                4) View names
                5) Quit       
                """)
            Selection = int(input("Enter an option: "))
            if Selection == 1:
                Name_List = Add_Name()
            elif Selection == 2:
                Name_List = Change_Name()
            elif Selection == 3:
                Name_List = Delete_Name()    
            elif Selection == 4:
                Name_List = View_Names()
            elif Selection == 5:
                repeat = "N"
            else: 
                print("Incorrect Option: ")
                main()
            data = (Name_List,repeat)

    Name_List = []
    main()

def C_122():
    import csv


    # add to file
    def add_files():
        file = open("Salaries.csv", "w")
        Name = input("Enter the name: ")
        Salary = input("Enter the salary: ")
        Newrecord = Name + ',' + str(Salary) + "\n"
        file.write(str(Newrecord))
        file.close()

    #View all records
    def view_records(): 
        file = open("Salaries.csv", "r")
        for row in file:
            print(row)
        file.close()

    def main():
        Repeat = True
        while Repeat == True:
            print("""
            1) Add to file
            2) View all records
            3) Quit program
            """)
            Selection = int(input("Enter the number of your selection: "))
            if Selection == 1:
                add_files()
            elif Selection == 2:
                view_records()
            elif Selection == 3: 
                Repeat = False
            else: 
                print("Incorrect option")

    main()

def C_123():
    import csv


    # add to file
    def add_files():
        file = open("Salaries.csv", "w")
        Name = input("Enter the name: ")
        Salary = input("Enter the salary: ")
        Newrecord = Name + ',' + str(Salary) + "\n"
        file.write(str(Newrecord))
        file.close()

    #View all records
    def view_records(): 
        file = open("Salaries.csv", "r")
        for row in file:
            print(row)
        file.close()

    def deleterecord():
        file = open("Salaries.csv")
        x = 0
        tmplist = []
        for row in file:
            tmplist.append(row)
        file.close()
        for row in tmplist:
            print(x,row)
            x = x + 1
        rowtodelete = int(input("Enter the row number to delete: "))
        del tmplist[rowtodelete]
        file = open("Salaries.csv","w")
        for row in tmplist:
            file.write(row)
        file.close()

    def main():
        Repeat = True
        while Repeat == True:
            print("""
            1) Add to file
            2) View all records
            3) Quit program
            """)
            Selection = int(input("Enter the number of your selection: "))
            if Selection == 1:
                add_files()
            elif Selection == 2:
                view_records()
            elif Selection == 3: 
                Repeat = False
            else: 
                print("Incorrect option")

    main()

