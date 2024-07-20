from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import re
import mysql.connector


    

# # password




            
# def register_user():
#     x=y=0
#     if id.get() == "":
#         messagebox.showinfo("Alert","Enter your id first")
#     elif user_name.get() =="" :
#         messagebox.showinfo("Alert","Enter Name")
#     elif user_email.get() == "":
#         messagebox.showinfo("Alert","Enter Email ")
#     elif gender.get() ==0:
#         messagebox.showinfo("Alert","Select Gender")
#     elif password.get() == "":
#         messagebox.showinfo("Alert","Enter password")
#     elif  repeat_password.get()=="":
#         messagebox.showinfo("Alert","Enter Repeat Password")

class register_window:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title('Register')
        self.root.minsize(1280,720)
        backgroundImage = Image.open(r"images/bg2.png")
        backgroundImage=backgroundImage.resize((2000,2000))
        self.bgImage=ImageTk.PhotoImage(backgroundImage)
        bg_lbl=Label(self.root,image=self.bgImage)
        bg_lbl.place(x=0,y=0, relheight=1,relwidth=1)

        frame=Frame(self.root,bg='#e6f4f9',pady=25)
        frame.place(x=370,y=100,width=770,height=580)

        self.id=StringVar()
        self.user_name=StringVar()
        self.user_email=StringVar()
        self.gender=StringVar()
        self.password=StringVar()
        self.repeat_password=StringVar()

        # title
        title_label=Label(frame,text="Register" ,bg='#e6f4f9',fg="black",font=("arial",25,"bold"))
        title_label.place(x=320,y=30)

        # Unique ID
        id=Label(frame,text='ID :',bg='#e6f4f9',fg="black",font=("arial",15,"bold"))
        id.place(x=25,y=110)

        self.id_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.id)
        self.id_entry.place(x=25,y=140,width=350,height=40)


        # username
        user_name=Label(frame,text='Name :',bg='#e6f4f9',fg="black",font=("arial",15,"bold"))
        user_name.place(x=400,y=110)

        self.name_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.user_name)
        self.name_entry.place(x=400,y=140,width=350,height=40)

        # Email
        user_email=Label(frame,text='Email :',bg='#e6f4f9',fg="black",font=("arial",15,"bold"))
        user_email.place(x=25,y=200)

        self.email_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.user_email)
        self.email_entry.place(x=25,y=230,width=350,height=40)


        # Gender
        user_name=Label(frame,text='Gender :',bg='#e6f4f9',fg="black",font=("arial",15,"bold"))
        user_name.place(x=400,y=200)

        sub_frame=Frame(frame,bg='#e6f4f9')
        sub_frame.place(x=400,y=230,width=350,height=40)

        gender_male=Radiobutton(sub_frame,text="Male",bg='#e6f4f9',activebackground='white',font=("arial",12,"bold"),value="male",variable=self.gender)
        gender_male.place(x=0,y=4)

        gender_female=Radiobutton(sub_frame,text="Female",bg='#e6f4f9',activebackground='white',font=("arial",12,"bold"),value="female",variable=self.gender)
        gender_female.place(x=100,y=4)

        gender_others=Radiobutton(sub_frame,text="Others",bg='#e6f4f9',activebackground='white',font=("arial",12,"bold"),value="others",variable=self.gender)
        gender_others.place(x=200,y=4)


        # password
        password=Label(frame,text='Password :',bg='#e6f4f9',fg="black",font=("arial",15,"bold"))
        password.place(x=25,y=290)

        self.password_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.password)
        self.password_entry.place(x=25,y=320,width=350,height=40)


        # repeat password
        repeat_password=Label(frame,text='Repeat Password :',bg='#e6f4f9',fg="black",font=("arial",15,"bold"))
        repeat_password.place(x=400,y=290)

        self.repeat_password_entry=ttk.Entry(frame,font=("arial",15,"bold"),textvariable=self.repeat_password)
        self.repeat_password_entry.place(x=400,y=320,width=350,height=40)
        # Create in btn

        create_btn=Button(frame,text='Create',font=("arial",15,"bold"),bg='blue',fg='white',activeforeground='white',activebackground='green', borderwidth=0,cursor="hand2",command=self.register_user)
        create_btn.place(x=330,y=400,height=40,width=120)
        
        #registration page

        page_link=Button(frame,text='Already Have An Account',font=("arial",15,"bold"),fg='green',bg='#e6f4f9',cursor="hand2",borderwidth=0,activeforeground='red',activebackground='#e6f4f9')
        page_link.place(x=250,y=460,height=40,width=260)


    # function
    def register_user(self):
        if self.id.get()=="":
            messagebox.showerror("Alert","Enter Your ID")
        elif self.user_name.get()=="":
            messagebox.showerror("Alert","Enter Your Name")
        elif self.user_email.get()=="":
            messagebox.showerror("Alert","Enter Your Email")
        elif self.gender.get()=="":
            messagebox.showerror("Alert","Select Your Gender")
        elif self.password.get()=="":
            messagebox.showerror("Alert","Select Your Password")
        elif (self.repeat_password.get()==""):
            messagebox.showerror("Alert","Select Your Repeat Password")
        elif self.user_email.get()!=0:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",self.user_email.get()):
                if len(self.password.get()) >=6:
                    if(self.password.get()==self.repeat_password.get()):

                        # connect database
                        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="admin_info")
                        my_cursor=conn.cursor()
                        query=("select * from user_info where id=%s")
                        value=(self.id.get(),)
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()
                        if row!=None:
                            messagebox.showerror("Error","Account Already exist")
                        else:
                            my_cursor.execute("insert into user_info values(%s,%s,%s,%s,%s)",(
                                                                                                 self.id.get(),
                                                                                                 self.user_name.get(),
                                                                                                 self.user_email.get(),
                                                                                                 self.gender.get(),
                                                                                                 self.password.get()
                                                                                            ))
                            conn.commit()
                            conn.close()
                            messagebox.showerror("Error","tune karliya sahise")
                    else:
                         messagebox.showerror("Alert","Password and repeat password must be same")
                else:
                    messagebox.showerror("Alert","Password must be 6 digit long")
            else:
                messagebox.showerror("Alert","Enter Valid Email")
        else:
            messagebox.showerror("Alert","All Field Required")
        # elif self.password.get()!="":
           



             

if __name__ == "__main__":
    root=Tk()
    app=register_window(root)
    root.mainloop()