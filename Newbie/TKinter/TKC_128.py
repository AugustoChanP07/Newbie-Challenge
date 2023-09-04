from tkinter import * 

def km_M ():
    km = TextBox1.get()
    km = int(km)
    answer = output_txt["text"]
    answer = int(answer)
    total = km * 0.6214
    output_txt["text"] = total


window = Tk()
window.title("Distance")
window.geometry("450x100")

#Labels 

Label_1 = Label(text = "Kilometers:")
Label_1.place(x = 30, y = 20)

Label_2 = Label(text = "Miles:")
Label_2.place(x = 60, y = 50)

#text
TextBox1 = Entry(text = 0)
TextBox1.place(x = 110, y = 20, width= 200, height=25)
TextBox1["justify"] = "center"
TextBox1.focus()

#Output
output_txt = Message(text = 0)
output_txt.place(x = 110, y = 50, width= 200, height=25)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"

#Button
Button1 = Button(text = "Convert", command= km_M)
Button1.place(x = 320, y = 20, width= 120, height=25)


window.mainloop()