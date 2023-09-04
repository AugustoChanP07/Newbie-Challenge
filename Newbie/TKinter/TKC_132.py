from tkinter import *

#=============FUNCTIONS=============#
def Add_NameAge():
    Name = NameBox1.get()
    Age = AgeBox1.get()
    Num_list.insert(END, Name + ',' + Age)
    NameBox1.delete(0,END)
    AgeBox1.delete(0,END)
    NameBox1.focus()
    AgeBox1.focus()

def Clear():
    Num_list.delete(0,END)
    Num_list.focus()

def Save():
    file = open("NameAge_132.csv", "a")
    tmp_list = Num_list.get(0,END)
    item = 0
    for x  in tmp_list:
        newrecord = tmp_list[item] + "\n"
        file.write(str(newrecord))
        item = item + 1
    file.close()
    Num_list.delete(0,END)
    Num_list.focus()


window = Tk()
window.title("NAMES AND AGES")
window.geometry("500x200")



#=============NAME==============#
Label_1 = Label(text = "Enter a Name: ")
Label_1.place(x = 20, y = 20)

NameBox1 = Entry(text = 0)
NameBox1.place(x = 110, y = 20, width= 200, height=25)
NameBox1["justify"] = "center"
NameBox1.focus()



#==============AGE===============#
Label_2 = Label(text = "Enter an Age: ")
Label_2.place(x = 20, y = 55)

AgeBox1 = Entry(text = 1)
AgeBox1.place(x = 110, y = 50, width= 200, height=25)
AgeBox1["justify"] = "center"
AgeBox1.focus()



#============BUTTONS=============#
Button1 = Button(text = "Add", command = Add_NameAge )
Button1.place(x = 320, y = 20, width= 120, height=25)

save_btn = Button(text= "Save",command= Save)
save_btn.place(x = 320, y= 80, width=120, height=25)

clear_btn = Button(text = "Clear", command=Clear)
clear_btn.place(x=320, y = 50, width=120, height=25)


#============LISTBOX==============#
Num_list = Listbox()
Num_list.place(x = 110, y = 80, width= 200, height= 100)



window.mainloop()