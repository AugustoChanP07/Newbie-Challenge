from tkinter import *


def Add_Name():
    Name = TextBox1.get()
    Gender = selectGender.get()
    Name_list.insert(END, Name + "," + Gender)
    TextBox1.delete(0,END)
    TextBox1.focus()

def Clear():
    Name_list.delete(0,END)
    Name_list.focus()

def Save():
    file = open("NamesGender_137.txt", "w")
    tmp_list = Name_list.get(0,END)
    item = 0
    for x  in tmp_list:
        newrecord = tmp_list[item] + "\n"
        file.write(str(newrecord))
        item = item + 1
    file.close()
    Name_list.delete(0,END)
    Name_list.focus()


window = Tk()
window.title("TKC_137")
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
Name_list.place(x = 110, y = 80, width= 200, height= 100)

selectGender = StringVar(window)
selectGender.set("Select Gender")
namesList = OptionMenu(window,selectGender,"Boy","Girl","No-Binary")
namesList.place(x = 110, y = 50, width= 200, height=25) 

clear_btn = Button(text = "Clear", command=Clear)
clear_btn.place(x=320, y = 50, width=120, height=25)

clear_btn = Button(text = "Save", command=Save)
clear_btn.place(x=320, y = 80, width=120, height=25)


window.mainloop()