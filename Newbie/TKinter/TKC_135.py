from tkinter import *

def clicked():
    sel = selectColour.get()
    window.configure(background = sel)

window = Tk()
window.title("TKC_135")
window.geometry("500x300")


selectColour = StringVar(window)
selectColour.set("Select Color")

namesList = OptionMenu(window,selectColour,"turquoise","red","light green","black", "white")
namesList.place(x = 150, y = 125, width= 200, height=25) 

Change = Button(text="Click Me", command=clicked)
Change.place(x = 150, y = 150, width=200, height=25)


window.mainloop()