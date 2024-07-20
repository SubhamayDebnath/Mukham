from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import base64
from datetime import datetime

root= Tk()
root.geometry("1200x700+140+40")
root.title("Login")
root.resizable(False,False)

id_entry=StringVar
password_entry=StringVar  


# main_frame
main_frame=Frame(root,bg="white")
main_frame.place(x=0,y=0, relheight=1,relwidth=1)

# side image
side_bg=Image.open(r"images/side.png")
side_bg=side_bg.resize((740,740))
sideImage=ImageTk.PhotoImage(side_bg)

side_image=Label(main_frame,image=sideImage)
side_image.place(x=0,y=0)

# input fields
input_frame=Frame(main_frame,bg="white")
input_frame.place(x=700,y=0,width=550,height=720)

# title

title=Label(input_frame,text="LOG IN",font=("Comfortaa",26,"bold"),bg="white",fg="blue")
title.place(x=0,y=120)

# user id input

user_id=Label(input_frame,text="Unique ID:",font=("Comfortaa",14),bg="white")
user_id.place(x=0,y=210)

id_entry=ttk.Entry(input_frame,font=("Comfortaa",14),textvariable=id_entry)
id_entry.place(x=0,y=250,width=340,height=40)

# password input
def show_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

user_password=Label(input_frame,text="Password :",font=("Comfortaa",14),bg="white")
user_password.place(x=0,y=320)

password_entry=ttk.Entry(input_frame,font=("Comfortaa",14),show="*",textvariable=password_entry)
password_entry.place(x=0,y=360,width=340,height=40)
# for show password 

 # Show password checkbox
check_btn=Checkbutton(input_frame,text=" Show Password" , command=show_password,bg='white',activebackground='white')
check_btn.place(x=0,y=400)

# btn

def login_func():
        global id_entry
        if id_entry.get()=="":
            messagebox.showerror("Error","Enter ID")
        elif password_entry.get() == "":
            messagebox.showerror("Error","Enter Password")
        else:
            # password decryption

            decrypt_password = base64.b85encode((password_entry.get()).encode("utf-8")) 

            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from user_info where id=%s and password=%s",(id_entry.get(),decrypt_password))
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Invalid","Invalid ID/Password")
            else:
              
                root.destroy()
                import dashboard
                


def got_to_reg():
    root.destroy()
    import register
    
btn_frame=Frame(input_frame,bg="white")
btn_frame.place(x=0,y=440,width=550,height=150)

login_btn=Button(btn_frame,command=login_func,text="LOG IN",font=("Comfortaa",14),bg="blue",fg="white",activebackground='green',activeforeground="white",borderwidth=0,padx=20,pady=5,cursor="hand2")
login_btn.grid(row=0,column=1,)


reg_btn=Button(btn_frame,command=got_to_reg,text="Create Account",font=("Comfortaa",14),bg="orange",fg="white",activebackground='red',activeforeground="white",borderwidth=0,padx=20,pady=5,cursor="hand2")
reg_btn.grid(row=0,column=2,)

def forget_password_window():
    if id_entry.get()=="":
        messagebox.showerror("Error","Please Enter The ID For Reset Password")
    else:

        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
        my_cursor=conn.cursor()
        query=("select * from user_info where id=%s")
        value=(id_entry.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        
        if row==None:
            messagebox.showerror("Error","Please Enter Valid ID")
        else:
            conn.close()
            root2=Toplevel()
            root2.title("Forget Password")
            root2.geometry("400x500+500+100")
            root2.resizable(False,False)
            root2['bg']='white'


            security_q=StringVar()
            security_a=StringVar()
            new_password=StringVar()

            title2=Label(root2,text="Forget Password",font=("Comfortaa",18),bg="white",pady=30,fg="blue")
            title2.place(x=110,y=20)

            user_security=Label(root2,text='Select Your Security Question',bg='white',fg="black",font=("Comfottaa",15))
            user_security.place(x=22,y=130)
            combo_security=ttk.Combobox(root2,font=("Comfottaa",15),state="readonly",textvariable=security_q)
            combo_security["values"]=("Select","Your Birth City","Your Pet name","Others")
            combo_security.place(x=22,y=180,width=350,height=40)
            combo_security.current(0)

            security_Q=ttk.Entry(root2,textvariable=security_a)
            security_Q.place(x=22,y=230,width=350,height=40)

            # password
            password_lbl=Label(root2,text='New Password :',bg='white',fg="black",font=("Comfottaa",15))
            password_lbl.place(x=22,y=280)

            password_entry2=ttk.Entry(root2,font=("arial",15,"bold"),textvariable=new_password)
            password_entry2.place(x=22,y=310,width=350,height=40)

            def reset_pass():

                if security_q.get() =="Select":
                    messagebox.showerror("Alert","Select Your Security Question")
                elif security_a.get()=="":
                    messagebox.showerror("Alert","Select Your Security Answer")
                elif new_password.get()=="":
                    messagebox.showerror("Alert","Select Your Password")
                elif new_password.get()!="":
                    if len(new_password.get())>=6:
                        new_decrypt_password = base64.b85encode((new_password.get()).encode("utf-8")) 

                        conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
                        my_cursor=conn.cursor()
                        query=("select * from user_info where id=%s and security_q=%s and security_a=%s")
                        value=(id_entry.get(),security_q.get(),security_a.get())
                        my_cursor.execute(query,value)
                        row=my_cursor.fetchone()

                        if(row==None):
                            messagebox.showerror("error","PLease Enter Correct Answer")
                        else:
                          user_id_new=id_entry.get()
                          query=("update user_info set password=%s where id=%s")
                          value=(new_decrypt_password,user_id_new)
                          my_cursor.execute(query,value)
                          conn.commit()
                          conn.close()
                          msg=messagebox.showinfo("Info","Your Password Has Been reset,Please Login")
                          if msg!="":
                              root2.destroy()

                    else:
                        messagebox.showerror("Alert","Password must be 6 digit long")
                else:
                    messagebox.showwarning("warning","Something Went wrong")
            reset_btn=Button(root2,command=reset_pass,text="Save",font=("Comfortaa",14),bg="red",fg="white",activebackground='green',activeforeground="white",borderwidth=0,padx=20,pady=5,cursor="hand2")
            reset_btn.place(x=160,y=400)
            root2.mainloop()

      



for_pass_btn=Button(input_frame,command=forget_password_window,text="Forgotten Password",font=("Comfortaa",14),bg="green",fg="white",activebackground='orange',activeforeground="white",borderwidth=0,padx=20,pady=5,cursor="hand2")
for_pass_btn.place(x=0,y=490)



                

  


root.mainloop()