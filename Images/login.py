from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector


class login_window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title('login')
        self.root.minsize(1280,720)
        backgroundImage = Image.open(r"images/bg2.png")
        backgroundImage=backgroundImage.resize((2000,2000))
        self.bgImage=ImageTk.PhotoImage(backgroundImage)
        bg_lbl=Label(self.root,image=self.bgImage)
        bg_lbl.place(x=0,y=0, relheight=1,relwidth=1)

        frame=Frame(self.root,bg='white')
        frame.place(x=570,y=170,width=400,height=480)
        self.id_entry=StringVar
        self.password_entry=StringVar  
        # title
        title_label=Label(frame,text="LOG IN" ,bg='white',fg="black",font=("arial",25,"bold"))
        title_label.place(x=135,y=40)

        # input 1 (user unique id)
        Reg_id=Label(frame,text='ID :',bg='white',fg="black",font=("arial",15,"bold"))
        Reg_id.place(x=25,y=110)

        self.id_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.id_entry)
        self.id_entry.place(x=25,y=140,width=350,height=40)

        # input 2 (password)

        password=Label(frame,text='Password :',bg='white',fg="black",font=("arial",15,"bold"))
        password.place(x=25,y=210)

        self.password_entry=ttk.Entry(frame,font=("arial",15,"bold"),show="*",textvariable=self.password_entry)
        self.password_entry.place(x=25,y=240,width=350,height=40)
        # for show password 
        def show_password():
            if self.password_entry.cget('show') == '*':
                self.password_entry.config(show='')
            else:
                self.password_entry.config(show='*')

        # Show password checkbox
        check_btn=Checkbutton(frame,text=" Show Password" , command=show_password,bg='white',activebackground='white')
        check_btn.place(x=25,y=290)

        # log in btn

        login_btn=Button(frame,command=self.login,text='login',font=("arial",15,"bold"),bg='blue',fg='white',activeforeground='white',activebackground='green', borderwidth=0,cursor="hand2")
        login_btn.place(x=140,y=340,height=40,width=120)
        
        #registration page

        page_link=Button(frame,text='Create a New Account',font=("arial",15,"bold"),fg='green',bg="white",cursor="hand2",borderwidth=0,activeforeground='red',activebackground='white')
        page_link.place(x=90,y=400,height=40,width=220)

        

    def login(self):
        if self.id_entry.get()=="":
            messagebox.showerror("Error","Enter ID")
        elif self.password_entry.get() == "":
            messagebox.showerror("Error","Enter Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="admin_info")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from user_info where id=%s and password=%s",(self.id_entry.get(),self.password_entry.get()))
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Invalid","Invalid ID/Password")
            else:
                open_main=messagebox.askyesno("YES/NO","Access only admin")

          
    
if __name__ == "__main__":
    root=Tk()
    app=login_window(root)
    root.mainloop()