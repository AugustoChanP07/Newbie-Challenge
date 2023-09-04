from tkinter import *



def Check_Num():
    Num = TextBox1.get()
    if Num.isdigit():
        Num_list.insert(END, Num)
        TextBox1.delete(0,END)
        TextBox1.focus()
    else:
        TextBox1.delete(0,END)
        TextBox1.focus()

def Clear():
    Num_list.delete(0,END)
    Num_list.focus()

def Save():
    file = open("NUM_130.csv", "w")
    tmp_list = Num_list.get(0,END)
    item = 0
    for x  in tmp_list:
        newrecord = tmp_list[item] + "\n"
        file.write(str(newrecord))
        item = item + 1
    file.close()


window = Tk()
window.title("NUMBERS")
window.geometry("450x200")

Label_1 = Label(text = "Enter a number: ")
Label_1.place(x = 20, y = 20)

TextBox1 = Entry(text = 0)
TextBox1.place(x = 110, y = 20, width= 200, height=25)
TextBox1["justify"] = "center"
TextBox1.focus()

Button1 = Button(text = "Add Num", command = Check_Num)
Button1.place(x = 320, y = 20, width= 120, height=25)

Num_list = Listbox()
Num_list.place(x = 110, y = 50, width= 200, height= 100)

save_btn = Button(text= "Save",command= Save)
save_btn.place(x = 320, y= 80, width=120, height=25)

clear_btn = Button(text = "Clear", command=Clear)
clear_btn.place(x=320, y = 50, width=120, height=25)

window.mainloop()