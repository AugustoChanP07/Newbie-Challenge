import random 


def Main():
    Answers = Colors()
    Game(Answers)


def Colors():
    Color_List = ["red","blue","yellow","green"]

    Color1 = random.choice(Color_List)
    Color2 = random.choice(Color_List)
    Color3 = random.choice(Color_List)
    Color4 = random.choice(Color_List)

    Answers = [Color1,Color2,Color3,Color4]


    return Answers


def Game(Answers):
    
    Score = 0

    Again = True
    while Again == True:
        guess1 = input("Enter the first color: ")
        guess1 = guess1.lower()
        
        if guess1 != Answers[0] and guess1 in Answers:
            print("Incorrect but is in the Color list")
        
        elif guess1 != Answers[0] and guess1 not in Answers:
            print("Incorrect and is not in the color list")
        
        elif guess1 == Answers[0]:
            print("Answer Correct")
            Score = Score + 1
            Again == False
            break

    Again = True
    while Again == True:
        guess2 = input("Enter the Second color: ")
        guess2 = guess2.lower()
        
        if guess2 != Answers[1] and guess2 in Answers:
            print("Incorrect but is in the Color list")
        
        elif guess2 != Answers[1] and guess2 not in Answers:
            print("Incorrect and is not in the color list")
        
        elif guess2 == Answers[1]:
            print("Answer Correct")
            Score = Score + 1
            Again == False
            break

    Again = True
    while Again == True:
        guess3 = input("Enter the Third color: ")
        guess3 = guess3.lower()
        
        if guess3 != Answers[2] and guess3 in Answers:
            print("Incorrect but is in the Color list")
        
        elif guess3 != Answers[2] and guess3 not in Answers:
            print("Incorrect and is not in the color list")
        
        elif guess3 == Answers[2]:
            print("Answer Correct")
            Score = Score + 1
            Again == False
            break

    Again = True
    while Again == True:
        guess4 = input("Enter the fourth color: ")
        guess4 = guess4.lower()
        
        if guess4 != Answers[3] and guess4 in Answers:
            print("Incorrect but is in the Color list")
        
        elif guess4 != Answers[3] and guess4 not in Answers:
            print("Incorrect and is not in the color list")
        
        elif guess4 == Answers[3]:
            print("Answer Correct")
            Score = Score + 1
            Again == False
            break
            
    if Score == 4:
        print("YOU DID IT!!!")

    else:
        print("You Lose")
                        

Main()