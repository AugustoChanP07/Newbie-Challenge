from tkinter import * 

def Press():
    name = TextBox1.get()
    msg = Label(window, text = "hello" + name)
    msg.place(x = 50, y=100)
    TextBox2["bg"] = "blue"
    TextBox2["fg"] = "white"
    TextBox2["text"] = msg


window = Tk()
window.title("Window")
window.geometry("750x200")

Label_1 = Label(text = "Enter you name: ")
Label_1.place(x = 30, y = 20)

TextBox1 = Entry(text = "")
TextBox1.place(x = 150, y = 20, width= 200, height=25)
TextBox1["justify"] = "center"
TextBox1.focus()

Button1 = Button(text = "Press to print", command= Press)
Button1.place(x = 30, y = 50, width= 120, height=25)

TextBox2 = Message(text="")
TextBox2.place(x = 150, y = 50, width= 200, height=25)
TextBox2["bg"] = "white"
TextBox2["fg"] = "black"

window.mainloop()


