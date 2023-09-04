from tkinter import * 

Num_List = []


def Add():
    Number = TextBox1.get()
    Number = int(Number)
    answer = output_txt["text"]
    answer = int(answer)
    total = Number + answer
    output_txt["text"] = total

def reset():
    total = 0
    output_txt["text"] = 0
    TextBox1.delete(0,END)
    TextBox1.focus()
    



window = Tk()
window.title("Numbers")
window.geometry("450x100")

Label_1 = Label(text = "Enter a num: ")
Label_1.place(x = 30, y = 20)

TextBox1 = Entry(text = 0)
TextBox1.place(x = 105, y = 20, width= 200, height=25)
TextBox1["justify"] = "center"
TextBox1.focus()

Button1 = Button(text = "Add Num", command=Add)
Button1.place(x = 310, y = 20, width= 120, height=25)

output_txt = Message(text = 0)
output_txt.place(x = 150, y = 50, width= 140, height=25)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"

clear_btn = Button(text = "Clear", command = reset)
clear_btn.place(x=300, y = 50, width=50, height=25)

window.mainloop()
