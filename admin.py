from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import re
import mysql.connector
import base64
    


root=Tk()
root.geometry("1920x1080+0+0")
root.title('Admin Profile')
root.minsize(1280,720)
root.iconbitmap('images/icon.ico')
bg_lbl=Label(root,bg='white')
bg_lbl.place(x=0,y=0, relheight=1,relwidth=1)

frame=Frame(root,relief=RIDGE,border=1)
frame.place(x=370,y=150,width=770,height=480)

# title
frame_title=Label(frame,text="Admin Profile",font=("Comfortaa",18,"bold"),pady=25).pack()
sub_frame=Frame(frame,width=770,height=450).pack()

admin_id=StringVar()
admin_name=StringVar()
admin_email=StringVar()
gender=StringVar()
admin_password=StringVar()

# Unique ID
id=Label(frame,text='ID :',fg="black",font=("Comfortaa",15))
id.place(x=25,y=80)
id_entry=ttk.Entry(frame,font=("Comfortaa",15),textvariable=admin_id)
id_entry.place(x=25,y=110,width=350,height=40)

# user name
user_name=Label(frame,text='Name :',fg="black",font=("Comfortaa",15))
user_name.place(x=395,y=80)

name_entry=ttk.Entry(frame,font=("Comfortaa",15),textvariable=admin_name)
name_entry.place(x=395,y=110,width=350,height=40)

# Email
user_email=Label(frame,text='Email :',font=("Comfortaa",15))
user_email.place(x=25,y=160)

email_entry=ttk.Entry(frame,font=("Comfortaa",15),textvariable=admin_email)
email_entry.place(x=25,y=190,width=350,height=40)

# Gender
user_gender=Label(frame,text='Gender :',font=("Comfortaa",15))
user_gender.place(x=395,y=160)

sub_frame=Frame(frame,)
sub_frame.place(x=395,y=190,width=350,height=40)

gender_male=ttk.Radiobutton(sub_frame,text="Male",value="male",variable=gender)
gender_male.place(x=0,y=5)

gender_female=ttk.Radiobutton(sub_frame,text="Female",value="female",variable=gender)
gender_female.place(x=110,y=5)

gender_others=ttk.Radiobutton(sub_frame,text="Others",value="others",variable=gender)
gender_others.place(x=210,y=5)

# password
password=Label(frame,text='Password :',font=("Comfortaa",15))
password.place(x=25,y=240)

password_entry=ttk.Entry(frame,font=("Comfortaa",15),textvariable=admin_password)
password_entry.place(x=25,y=270,width=350,height=40)
        


 # btn      
btn_frame=Frame(frame)
btn_frame.place(x=150, y=375, width=500, height=70,)

 #def update_admin():
      #   if admin_id.get()=="":
     #            messagebox.showerror("error","Please Enter Id")
    #     elif admin_name.get()=="":
#                 messagebox.showerror("Error","Please Enter Your Name") 
#         elif admin_email.get()=="":
#                 messagebox.showerror("Error","Please Enter Your Gender")
#         elif gender.get()=="":
#                 messagebox.showerror("Error","Please Select Your Gender")
#         elif admin_password.get()=="":
#                 messagebox.showerror("Error","Please Enter Your Message")
#         else:
#                 if len(admin_password.get())>= 6:
#                         new_decrypt_password = base64.b85encode((admin_password.get()).encode("utf-8")) 
#                         Update=messagebox.askyesno("Update","Do you want update ?")
#                         if Update > 0:
#                                 conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="admin_info")
#                                 my_cursor=conn.cursor()
#                                 my_cursor.execute("update user_info set user_name=%s,user_email=%s,gender=%s,password=%s where id=%s ",(admin_name.get(),
#                                                                                                                                          admin_email,
#                                                                                                                                          gender.get(),
#                                                                                                                                          new_decrypt_password))
                                
#                                 conn.commit()
#                                 conn.close()
#                                 messagebox.showinfo("success","Update has been done successfully")
#                 else:
#                        messagebox.showerror("Alert","Password must be 6 digit long")
                  


update_btn = Button(btn_frame, text="Update", width=17, font=("Comfortaa", 15, "bold"),bg="blue",fg="white",cursor="hand2")
update_btn.grid(row=0, column=1)


# delete account

def delete_account():
    if admin_id.get()=="":
        messagebox.showwarning("Error","Please Enter your id")
    else:
        delete_warning_box=messagebox.askokcancel("Delete","Do you delete your account")
        if delete_warning_box > 0:
               conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
               my_cursor=conn.cursor()
               query ="delete from user_info where id=%s"
               value=(admin_id.get(),)
               my_cursor.execute(query, value)
               conn.commit()
               conn.close()
               root.destroy()
               import register


delete_btn = Button(btn_frame, command=delete_account,text="Delete", width=17, font=("Comfortaa", 15, "bold"),bg="red",fg="white",cursor="hand2")
delete_btn.grid(row=0, column=2)
# function
   


root.mainloop()