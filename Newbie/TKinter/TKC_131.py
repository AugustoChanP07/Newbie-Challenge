from tkinter import *
import csv

def Save_data():
    file = open("NameAge_131.csv" , "a")
    Name = TextBox1.get()
    Age = TextBox2.get()
    Newrecord = Name + ',' + Age + "\n"
    file.write(str(Newrecord))
    file.close()
    TextBox1.delete(0, END)
    TextBox2.delete(0, END)


#=============TKINTER================
window = Tk()
window.title("NUMBERS")
window.geometry("450x200")

#===========ENTER A NAME=============
Label_1 = Label(text = "Enter a name: ")
Label_1.place(x = 20, y = 20)

TextBox1 = Entry(text = 1)
TextBox1.place(x = 110, y = 20, width= 300, height=25)
TextBox1["justify"] = "center"
TextBox1.focus()

#===========ENTER AN AGE=============
Label_2 = Label(text = "Enter an age: ")
Label_2.place(x = 20, y = 50)

TextBox2 = Entry(text = 0)
TextBox2.place(x = 110, y = 50, width= 300, height=25)
TextBox2["justify"] = "center"
TextBox2.focus()

#===============BUTTON================
Save_btn = Button(text="Save", command= Save_data)
Save_btn.place(x = 110, y=80, width=300, height=25)

window.mainloop()
