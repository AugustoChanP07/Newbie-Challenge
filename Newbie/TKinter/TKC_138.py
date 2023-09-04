from tkinter import * 



#============TKINTER=============#
window = Tk()
window.title("TKC_138")
window.geometry("500x500")
window.configure(background= "light blue")

def Select_GIF (Select):    
    if Select == "Pikachu":
        photo = PhotoImage(file = "Pikachu.gif")
        photobox = Label(window, image = photo)
        photobox.image = photo
        photobox.place(x = 40, y = 30, width = 300, height = 300)
    
    else: 
        photo = PhotoImage(file = "Chicken_Little.gif")
        photobox = Label(window, image = photo)
        photobox.image = photo
        photobox.place(x = 40, y = 30, width = 300, height = 300)



#===========SELECTBOX============#
selectGender = StringVar(window)
selectGender.set("Select your GIF!")
namesList = OptionMenu(window,selectGender,"Pikachu","Chicken little", command= Select_GIF)
namesList.place(x = 110, y = 400, width= 300, height=25) 


window.mainloop()


