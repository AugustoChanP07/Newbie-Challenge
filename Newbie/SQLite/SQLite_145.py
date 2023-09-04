import sqlite3
from tkinter import * 


#===================TKINTER====================#
window = Tk()
window.title("SQLite_145")
window.geometry("450x200")

#====================SQLite======================#
with sqlite3.connect("TestScores.db") as db:
    cursor = db.cursor()


#==================FUNCTIONS===================#
def Add ():
    Name = NameBox1.get()
    Grade = GradeBox1.get()
    cursor.execute("""INSERT INTO Test (Name,Grade)
                    VALUES(?,?)""", (Name,Grade))
    db.commit()
    
    NameBox1.delete(0, END)
    GradeBox1.delete(0, END)
    NameBox1.focus()
    print("Data has been added")
    
def Clear():
    NameBox1.delete(0, END)
    GradeBox1.delete(0, END)
    NameBox1.focus()



#================STUDENTS NAME=================#
Label_Name = Label(text = "Enter student's name: ")
Label_Name.place(x = 30, y = 20)

NameBox1 = Entry(text = 0)
NameBox1.place(x = 150, y = 20, width= 250, height=25)
NameBox1["justify"] = "center"
NameBox1.focus()


#================STUDENTS GRADE=================#
Label_Grade = Label(text = "Enter student's grade: ")
Label_Grade.place(x = 30, y = 50)

GradeBox1 = Entry(text = 1)
GradeBox1.place(x = 150, y = 50, width= 250, height=25)
GradeBox1["justify"] = "center"
GradeBox1.focus()

#====================BUTTONS======================#
Button_Add = Button(text = "Add", command= Add)
Button_Add.place(x = 160, y = 80, width= 100, height=25)

Button_Clear = Button(text = "Clear", command= Clear)
Button_Clear.place(x = 290, y = 80, width= 100, height=25)



mainloop()