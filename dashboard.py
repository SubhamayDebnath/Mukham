import os
from tkinter import *
from tkinter import Tk

import self
from PIL import Image,ImageTk


root=Tk()
root.geometry("1920x1080+0+0")
root.title('Mukham')
root.minsize(1280,720)
root.iconbitmap('images/icon.ico')
# background_image = Image.open(r"images/bg.png")
# background_image=background_image.resize((2000,2000))
# bgImage=ImageTk.PhotoImage(background_image)
bg_lbl=Label(root,bg="white")
bg_lbl.place(x=0,y=0, relheight=1,relwidth=1)
titleLabel= Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Comfortaa",25,"bold"),fg="black",bg="white",pady=20,padx=15)
titleLabel.place(x=400,y=40)
 # student btn

def go_to_admin():
    import admin


icon_mage=Image.open("images/admin.png")
icon_mage=icon_mage.resize((220,220))
iconImg=ImageTk.PhotoImage(icon_mage)

btn1=Button(bg_lbl,image=iconImg,cursor="hand2", borderwidth=0,command=go_to_admin)
btn1.place(x=250,y=200)
        
      
btn1=Button(bg_lbl,text="Admin",cursor="hand2", borderwidth=0,font=("Comfortaa",10,"bold"),bg='orange',command=go_to_admin)
btn1.place(x=250,y=400,height=40,width=222)

        # face register
def Student():
    from Student import Student

    self.new_window=Toplevel(root)
    self.app=Student(self.new_window)


icon_mage2=Image.open("images/faceicon.png")
icon_mage2=icon_mage2.resize((220,220))
iconImg2=ImageTk.PhotoImage(icon_mage2)

btn2=Button(bg_lbl,image=iconImg2,cursor="hand2", borderwidth=0, command=Student)
btn2.place(x=500,y=200)
btn2=Button(bg_lbl,text="Face Register",cursor="hand2",command=Student,borderwidth=0,font=("Comfortaa",10,"bold"),bg='orange')
btn2.place(x=500,y=400,height=40,width=222)

 # attendance
def attendence():
    from Face_recognisation import Face_recognisation
    self.new_window=Toplevel(root)
    self.app=Face_recognisation(self.new_window)
icon_mage3=Image.open("images/face_scan.png")
icon_mage3=icon_mage3.resize((220,220))
iconImg3=ImageTk.PhotoImage(icon_mage3)

btn2=Button(bg_lbl,image=iconImg3,cursor="hand2", borderwidth=0,command=attendence )
btn2.place(x=750,y=200)

btn2=Button(bg_lbl,text="Mark Attendance",cursor="hand2", borderwidth=0,font=("Comfortaa",10,"bold"),bg='orange',command=attendence)
btn2.place(x=750,y=400,height=40,width=222)

#train data
def train():
    from Train import Train
    self.new_window=Toplevel(root)
    self.app=Train(self.new_window)
icon_mage4=Image.open("images/train.png")
icon_mage4=icon_mage4.resize((220,220))
iconImg4=ImageTk.PhotoImage(icon_mage4)

btn2=Button(bg_lbl,image=iconImg4,cursor="hand2", borderwidth=0,command=train )
btn2.place(x=1000,y=200)

btn2=Button(bg_lbl,text="Train Data",cursor="hand2", borderwidth=0,font=("Comfortaa",10,"bold"),bg='orange',command=train)
btn2.place(x=1000,y=400,height=40,width=222)




def data():
    os.startfile("data")
icon_mage5=Image.open("images/Student.png")
icon_mage5=icon_mage5.resize((220,220))
iconImg5=ImageTk.PhotoImage(icon_mage5)

btn2=Button(bg_lbl,image=iconImg5,cursor="hand2", borderwidth=0,command=data)
btn2.place(x=850,y=475)

btn2=Button(bg_lbl,text="Photos",cursor="hand2", borderwidth=0,font=("Comfortaa",10,"bold"),bg='orange',command=data)
btn2.place(x=850,y=650,height=40,width=222)

def csv():
   os.startfile("mukham.csv")
icon_mage7=Image.open("images/csv.png")
icon_mage7=icon_mage7.resize((220,220))
iconImg7=ImageTk.PhotoImage(icon_mage7)

btn2=Button(bg_lbl,image=iconImg7,cursor="hand2", borderwidth=0,command=csv)
btn2.place(x=400,y=475)

btn2=Button(bg_lbl,text="Attendence sheet",cursor="hand2", borderwidth=0,font=("Comfortaa",10,"bold"),bg='orange',command=csv)
btn2.place(x=400,y=650,height=40,width=222)


  #==============button function==================





root.mainloop()