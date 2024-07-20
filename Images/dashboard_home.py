from tkinter import *
from tkinter import Tk
from PIL import Image,ImageTk


class faceRecognitionSystem:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title('Maukam')
        self.root.minsize(1280,720)
        background_image = Image.open(r"images/bg2.png")
        background_image=background_image.resize((2000,2000))
        self.bgImage=ImageTk.PhotoImage(background_image)
        bg_lbl=Label(self.root,image=self.bgImage)
        bg_lbl.place(x=0,y=0, relheight=1,relwidth=1)
        titleLabel= Label(bg_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("arial",25,"bold"),fg="white",bg="black",pady=20,padx=15)
        titleLabel.place(x=400,y=40)

        
        # student btn
        icon_mage=Image.open("images/Student.png")
        icon_mage=icon_mage.resize((220,220))
        self.iconImg=ImageTk.PhotoImage(icon_mage)

        btn1=Button(bg_lbl,image=self.iconImg,cursor="mouse", borderwidth=0 )
        btn1.place(x=250,y=200)

        btn1=Button(bg_lbl,text="Student Details",cursor="mouse", borderwidth=0,font=("arial",10,"bold"),bg='orange')
        btn1.place(x=250,y=400,height=40,width=222)

        # face register
        icon_mage2=Image.open("images/faceicon.png")
        icon_mage2=icon_mage2.resize((220,220))
        self.iconImg2=ImageTk.PhotoImage(icon_mage2)

        btn2=Button(bg_lbl,image=self.iconImg2,cursor="mouse", borderwidth=0 )
        btn2.place(x=500,y=200)

        btn2=Button(bg_lbl,text="Face Register",cursor="mouse", borderwidth=0,font=("arial",10,"bold"),bg='orange')
        btn2.place(x=500,y=400,height=40,width=222)

         # attendance
        icon_mage3=Image.open("images/book.png")
        icon_mage3=icon_mage3.resize((220,220))
        self.iconImg3=ImageTk.PhotoImage(icon_mage3)

        btn2=Button(bg_lbl,image=self.iconImg3,cursor="mouse", borderwidth=0 )
        btn2.place(x=750,y=200)

        btn2=Button(bg_lbl,text="Attendance",cursor="mouse", borderwidth=0,font=("arial",10,"bold"),bg='orange')
        btn2.place(x=750,y=400,height=40,width=222)

        #time
        icon_mage4=Image.open("images/book.png")
        icon_mage4=icon_mage4.resize((220,220))
        self.iconImg4=ImageTk.PhotoImage(icon_mage4)

        btn2=Button(bg_lbl,image=self.iconImg4,cursor="mouse", borderwidth=0 )
        btn2.place(x=1000,y=200)

        btn2=Button(bg_lbl,text="Set Time",cursor="mouse", borderwidth=0,font=("arial",10,"bold"),bg='orange')
        btn2.place(x=1000,y=400,height=40,width=222)

if __name__ == "__main__":
    root=Tk()
    obj=faceRecognitionSystem(root)
    root.mainloop()