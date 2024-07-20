from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import base64
import re
root= Tk()
root.geometry("1200x700+140+40")
root.title("Register")
root.resizable(False,False)

id=StringVar()
user_name=StringVar()
user_email=StringVar()
gender=StringVar()
security_q=StringVar()
security_a=StringVar()
password=StringVar()
repeat_password=StringVar()

#main_frame
main_frame=Frame(root,bg="white")
main_frame.place(x=0,y=0, relheight=1,relwidth=1)

# side image
side_bg=Image.open(r"images/side.png")
side_bg=side_bg.resize((440,440))
sideImage=ImageTk.PhotoImage(side_bg)

side_image=Label(main_frame,image=sideImage,borderwidth=0)
side_image.place(x=0,y=120)

# input fields frame
input_frame=Frame(main_frame,bg="white")
input_frame.place(x=450,y=0,width=730,height=720)

title=Label(input_frame,text="Register",font=("Comfortaa",26,"bold"),bg="white",fg="blue")
title.place(x=0,y=50)


id_user=Label(input_frame,text='ID :',fg="black",bg="white",font=("Comfortaa",15))
id_user.place(x=0,y=150)

id_entry=ttk.Entry(input_frame,font=("Comfottaa",15),textvariable=id)
id_entry.place(x=0,y=180,width=350,height=40)

 # username
user_name_lbl=Label(input_frame,text='Name :',bg='white',fg="black",font=("Comfottaa",15))
user_name_lbl.place(x=370,y=150)

user_name_entry=ttk.Entry(input_frame,font=("Comfottaa",15),textvariable=user_name)
user_name_entry.place(x=370,y=180,width=350,height=40)

 # Gender
user_gender=Label(input_frame,text='Gender :',bg='white',fg="black",font=("Comfottaa",15))
user_gender.place(x=0,y=230)

sub_frame=Frame(input_frame,bg='white')
sub_frame.place(x=0,y=260,width=350,height=40)

gender_male=ttk.Radiobutton(sub_frame,text="Male",value="male",variable=gender)
gender_male.place(x=0,y=4)

gender_female=ttk.Radiobutton(sub_frame,text="Female",value="female",variable=gender)
gender_female.place(x=100,y=4)

gender_others=ttk.Radiobutton(sub_frame,text="Others",value="others",variable=gender)
gender_others.place(x=200,y=4)

# email
email_lbl=Label(input_frame,text='Email :',bg='white',fg="black",font=("Comfottaa",15))
email_lbl.place(x=0,y=300)

email_entry=ttk.Entry(input_frame,font=("arial",15,"bold"),textvariable=user_email)
email_entry.place(x=0,y=330,width=350,height=40)



# security 

user_security=Label(input_frame,text='Select Your Security Question',bg='white',fg="black",font=("Comfottaa",15))
user_security.place(x=370,y=230)

combo_security=ttk.Combobox(input_frame,font=("Comfottaa",15),state="readonly",textvariable=security_q)
combo_security["values"]=("Select","Your Birth City","Your Pet name","Others")
combo_security.place(x=370,y=260,width=350,height=40)
combo_security.current(0)

security_Q=Label(input_frame,text='Security Answer :',bg='white',fg="black",font=("Comfottaa",15))
security_Q.place(x=275,y=300,width=350,height=40)

security_Q=ttk.Entry(input_frame,textvariable=security_a,font=("Comfottaa",15))
security_Q.place(x=370,y=330,width=350,height=40)


# password
password_lbl=Label(input_frame,text='Password :',bg='white',fg="black",font=("Comfottaa",15))
password_lbl.place(x=0,y=380)

password_entry=ttk.Entry(input_frame,font=("arial",15,"bold"),textvariable=password)
password_entry.place(x=0,y=410,width=350,height=40)


# repeat password
repeat_password_lbl=Label(input_frame,text='Repeat Password :',bg='white',fg="black",font=("Comfottaa",15))
repeat_password_lbl.place(x=370,y=380)

repeat_password_entry=ttk.Entry(input_frame,font=("Comfottaa",15),textvariable=repeat_password)
repeat_password_entry.place(x=370,y=410,width=350,height=40)

# btn
def register_form():
    if id.get()=="":
        messagebox.showerror("Alert","Enter Your ID")
    elif user_name.get()=="":
        messagebox.showerror("Alert","Enter Your Name")
    elif user_email.get()=="":
        messagebox.showerror("Alert","Enter Your Email")
    elif gender.get()=="":
        messagebox.showerror("Alert","Select Your Gender")
    elif security_q.get()=="":
        messagebox.showerror("Alert","Select Your Security Question")
    elif security_a.get()=="":
        messagebox.showerror("Alert","Select Your Security Answer")
    elif password.get()=="":
        messagebox.showerror("Alert","Select Your Password")
    elif (repeat_password.get()==""):
        messagebox.showerror("Alert","Select Your Repeat Password")
    elif user_email.get()!=0:
        if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",user_email.get()):
            if len(password.get()) >= 6:
                if(password.get()==repeat_password.get()):
                    # connect database
                    conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
                    my_cursor=conn.cursor()
                    # Password Encryption
                    encrypt_password = base64.b85encode((password.get()).encode("utf-8")) 
                    query=("select * from user_info where id=%s")
                    value=(id.get(),)
                    my_cursor.execute(query,value)
                    row=my_cursor.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","Account Already exist")
                    else:
                        my_cursor.execute("insert into user_info values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                id.get(),
                                                                                                user_name.get(),
                                                                                                user_email.get(),
                                                                                                security_q.get(),
                                                                                                security_a.get(),
                                                                                                gender.get(),
                                                                                                encrypt_password
                                                                                            ))
                        conn.commit()
                        conn.close()
                    root.destroy()
                    import login
                        
                else:
                    messagebox.showerror("Alert","Password and repeat password must be same")
            else:
                messagebox.showerror("Alert","Password must be 6 digit long")
        else:
            messagebox.showerror("Alert","Enter Valid Email")
    else:
        messagebox.showerror("Alert","All Field Required")  

btn_frame=Frame(input_frame,bg="white")
btn_frame.place(x=0,y=480,width=550,height=50)

submit_btn=Button(btn_frame,command=register_form,text="Create",font=("Comfortaa",14),bg="blue",fg="white",activebackground='green',activeforeground="white",borderwidth=0,padx=20,pady=5,cursor="hand2")
submit_btn.grid(row=0,column=1,)
def got_to_log():
    
    root.destroy()
    import login

register_btn=Button(btn_frame,command=got_to_log,text="Log in",font=("Comfortaa",14),bg="orange",fg="white",activebackground='red',activeforeground="white",borderwidth=0,padx=20,pady=5,cursor="hand2")
register_btn.grid(row=0,column=2,)



root.mainloop()