import random
from tkinter import * 

#===========TKINTER============#
window = Tk()
window.title("CODE CHALLENGE 134")
window.geometry("600x200")



def Random_Sum():
    global Number_randomONE, Number_randomTWO
    Number_randomONE = random.randint(10,50)
    Number_randomTWO = random.randint(10,50)
    msg = Label(window, text = f"{Number_randomONE} + {Number_randomTWO}" )
    msg.place(x = 160, y=50)
    

def Check():
    global Number_randomONE, Number_randomTWO
    Answer_Random = Number_randomONE + Number_randomTWO
    User_Answer = AnswerBox1.get()
    User_Answer = int(User_Answer)
    if User_Answer == Answer_Random:
        msg = Label(window, text = "Well done")
        msg.place(x = 150, y=120)
    else:
        msg = Label(window, text = "NOP" )
        msg.place(x = 150, y=120)




    
Button1 = Button(text = "Next", command= Random_Sum)
Button1.place(x = 30, y = 50, width= 120, height=25)

Button_Check = Button(text = "Check", command= Check)
Button_Check.place(x = 30, y = 80, width= 120, height=25)

AnswerBox1 = Entry(text = 0)
AnswerBox1.place(x = 150, y = 80, width= 275, height=25)
AnswerBox1["justify"] = "center"
AnswerBox1.focus()

window.mainloop()
