from tkinter import * 
import random

def Dice():
    Number_random = random.randint(1,6)
    msg = Label(window, text = Number_random)
    msg.place(x = 160, y=50)
    
    


window = Tk()
window.title("Magic Dice")
window.geometry("450x100")

Button1 = Button(text = "Let's roll the dice", command= Dice)
Button1.place(x = 30, y = 50, width= 120, height=25)



window.mainloop()