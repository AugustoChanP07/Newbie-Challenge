from tkinter import * 

#===========TKINTER============#
window = Tk()
window.title("CODE CHALLENGE 133")
window.geometry("400x400")

window.configure(background = "black") 

logo = PhotoImage(file = "/Logo.gif")
logoimage = Label(image = logo)
logoimage.place(x = 30, y = 20, width = 200, height = 120) 



#===========FUNCTIONS===========#
def Print_Hello():
    Name = NameBox1.get()
    total = str("Hello" + " " + Name)
    output_txt.config(text=total)


#=============NAME==============#
Label_1 = Label(text = "Enter a Name: ")
Label_1.place(x = 20, y = 300)

NameBox1 = Entry(text = 0)
NameBox1.place(x = 110, y = 300, width= 275, height=25)
NameBox1["justify"] = "center"
NameBox1.focus()

#============PRINT=============#
Label_print = Button(text = "Print", command=Print_Hello)
Label_print.place(x = 20, y = 330, width=100, height=25)

output_txt = Message(text = "")
output_txt.place(x = 110, y = 330, width= 275, height=25)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"


window.mainloop()