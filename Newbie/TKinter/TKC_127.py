from tkinter import *



def Add_Name():
    Name = TextBox1.get()
    Name_list.insert(END, Name)
    TextBox1.delete(0,END)
    TextBox1.focus()

def Clear():
    Name_list.delete(0,END)
    Name_list.focus()


window = Tk()
window.title("Names")
window.geometry("450x200")

Label_1 = Label(text = "Enter a name: ")
Label_1.place(x = 30, y = 20)

TextBox1 = Entry(text = 0)
TextBox1.place(x = 110, y = 20, width= 200, height=25)
TextBox1["justify"] = "center"
TextBox1.focus()

Button1 = Button(text = "Add Name", command = Add_Name)
Button1.place(x = 320, y = 20, width= 120, height=25)

Name_list = Listbox()
Name_list.place(x = 110, y = 50, width= 200, height= 100)



clear_btn = Button(text = "Clear", command=Clear)
clear_btn.place(x=320, y = 50, width=120, height=25)

window.mainloop()