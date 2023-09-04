from tkinter import *

#=============FUNCTIONS=============#
def Clear():
    Num_list.delete(0,END)
    NumberBox1.delete(0,END)
    Num_list.focus()
    NumberBox1.focus()

def Time_Table():
    Num_Loop = 0
    User_Num = NumberBox1.get()
    User_Num = int(User_Num)

    for x in range(0,12):
        Num_Loop = Num_Loop + 1
        Answer = User_Num * Num_Loop
        Num_list.insert(END,(User_Num, "x", Num_Loop, "=", Answer))
        




window = Tk()
window.title("Time Table Project")
window.geometry("500x300")

#=============NUMBER==============#
Label_1 = Label(text = "Enter a Number: ")
Label_1.place(x = 17, y = 20)

NumberBox1 = Entry(text = 0)
NumberBox1.place(x = 110, y = 20, width= 200, height=25)
NumberBox1["justify"] = "center"
NumberBox1.focus()

#============BUTTONS=============#
Button1 = Button(text = "View Time Table", command= Time_Table)
Button1.place(x = 320, y = 20, width= 120, height=25)

clear_btn = Button(text = "Clear", command=Clear)
clear_btn.place(x=320, y = 50, width=120, height=25)

#============LISTBOX==============#
Num_list = Listbox()
Num_list.place(x = 110, y = 55, width= 200, height= 200)



window.mainloop()