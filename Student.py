from tkinter import *
from tkinter import ttk
from tkinter.ttk import Entry

import cv2
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import re


class Student:
    def __init__(self, root):

        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Mukham")
        self.root.minsize(1280, 720)
        self.root.iconbitmap('images/icon.ico')

        # ============variables=================

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.va_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_search = StringVar()


        # bg image

        # img3 = Image.open("C:\\Users\\uchch\\PycharmProjects\\pythonProject1\\Images\\face-recognition-ar-hologram-screen-smart-technology.jpg")
        # img3 = img3.resize((1920,1080), Image.ANTIALIAS)
        # self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, bg="white")
        bg_img.place(x=0, y=0, width=1920, height=1080)

        title_lbl = Label(self.root, text="Student Management System", font=("times new roman", 35, "bold"), bg="white",
                          fg="red", padx=15, pady=20).pack()
        # title_lbl.place(x=0,y=0)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=20, y=90, width=1480, height=600)

        # left label frame

        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 21, "bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)

        # current course info
        current_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course information",
                                   font=("times new roman", 21, "bold"))
        current_frame.place(x=5, y=15, width=720, height=150)

        # department

        dep_label = Label(current_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_frame, textvariable=self.var_dep, font=("times new roman", 13, "bold"),
                                 state="readonly")
        dep_combo["values"] = ("Select Department", "School of Computer", "School of managment", "Bca")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_label = Label(current_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)
        course_combo = ttk.Combobox(current_frame, textvariable=self.var_course, font=("times new roman", 13, "bold"),
                                    state="readonly")
        course_combo["values"] = ("Select Course", "EE", "CSE", "IT", "BCA","MCA")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year

        year_label = Label(current_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"),
                                  state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2024-25","2025-26","2026-27","2027-28","2028-29","2029-30","2030-2031","2031-32")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        semester_label = Label(current_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_frame, textvariable=self.var_semester,
                                      font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "Semester1", "semester2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)
        # student information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student information",
                                         font=("times new roman", 21, "bold"))
        class_Student_frame.place(x=5, y=180, width=720, height=300)

        # student id

        studentId_label = Label(class_Student_frame, text="Student ID: ", font=("times new roman", 13, "bold"),
                                bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.va_std_id,
                                    font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # student name
        studenName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 13, "bold"),
                                 bg="white")
        studenName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_std_name,
                                      font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # class division

        class_div_label = Label(class_Student_frame, text="Class Division: ", font=("times new roman", 13, "bold"),
                                bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # class_div_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_div,font=("times new roman", 13,"bold"))
        # class_div_entry.grid(row = 1, column = 1, padx = 10, pady = 5,sticky =W)

        div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div, font=("times new roman", 13, "bold"),
                                 state="readonly")
        div_combo["values"] = ("Select Division","A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        # ROLL NO

        roll_no_label = Label(class_Student_frame, text="Roll No: ", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_roll,
                                  font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender

        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender,
                                    font=("times new roman", 13, "bold"), state="readonly")
        gender_combo["values"] = ("Select Gender","Male", "Female", "Others", "not interested")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        # Dob

        dob_label = Label(class_Student_frame, text="DOB: ", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_dob,
                              font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # email

        email_label = Label(class_Student_frame, text="Email: ", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_email,
                                font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # phone no

        phone_label = Label(class_Student_frame, text="Phone No: ", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_phone,
                                font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address

        address_label = Label(class_Student_frame, text="Address: ", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame, width=20, textvariable=self.var_address,
                                  font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # radio

        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="Take photo Sample",
                                    value="yes")
        radiobtn1.grid(row=5, column=0, padx=10, pady=5, sticky=W)

        radiobtn2 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="No photo Sample", value="no")
        radiobtn2.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # btn frame

        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=70)

        # bbuttons frame

        save_btn = Button(btn_frame, text="Save", width=17, command=self.add_date, font=("times new roman", 13, "bold"),
                          bg="green", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", width=17, command=self.update_data,
                            font=("times new roman", 13, "bold"), bg="darkblue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17,
                            font=("times new roman", 13, "bold"), bg="red", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17, command=self.reset_data,
                           font=("times new roman", 13, "bold"), bg="orange", fg="white")
        reset_btn.grid(row=0, column=3)

        leftframe1 = LabelFrame(main_frame, bd=0, bg="white", relief=RIDGE)
        leftframe1.place(x=20, y=500, width=715, height=40)

        take_photo_btn = Button(leftframe1, text="Take Photo Sample", command=self.genarate_dataset, width=22,
                                font=("times new roman", 13, "bold"), bg="red", fg="white")
        take_photo_btn.pack()



        # Right label frame

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Search Student Details",
                                 font=("times new roman", 21, "bold"))
        Right_frame.place(x=780, y=10, width=660, height=580)
        # frame
        search_frame = LabelFrame(Right_frame, bd=2, bg="whitesmoke", relief=RIDGE)
        search_frame.place(x=5, y=15, width=620, height=75)

        search_label = Label(search_frame, text="Search: ", font=("times new roman", 13, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=17, state="readonly")
        search_combo["values"] = ("NAME")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry =ttk.Entry(search_frame, width=34,textvariable=self.var_search,font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=15, pady=5,sticky=W)
        search_entry.bind("<Key>",self.search)


        ####################table frame##############

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=115, width=620, height=375)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            "dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address",
            "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("photo", width=100)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    ##################===function declaration================
    def add_date(self):
        if self.var_radio1.get() == "no":

            if self.var_dep.get() == "Select Depeartment" or self.var_std_name.get() == "" or self.va_std_id.get() == "" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_gender.get() == "Select Gender" or self.var_address.get() == "" or self.var_phone.get() == "" or self.var_roll.get() == "" or self.var_email.get() == "" or self.var_dob.get() == "" :

                messagebox.showerror("Error", "All Fields Are required", parent=self.root)
            else:
                try:
                    if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", self.var_email.get()):
                        if(len(self.var_phone.get())==10):
                            conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                           database="Face_recognizer")
                            my_cursor = conn.cursor()
                            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.va_std_id.get(),
                                self.var_std_name.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_radio1.get()
                            ))
                            conn.commit()
                            self.fetch_data()
                            conn.close()
                            messagebox.showinfo("Sucess", "Student details has been added Sucessfully", parent=self.root)
                        else:
                            messagebox.showerror("Error", "please enter valid phone no.", parent=self.root)
                    else:
                        messagebox.showerror("Error", "Please enter valid Email", parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
        else:
            messagebox.showerror("Error",
                                 "you can save Data upter 'take photo only' otherwise select 'No photo sample' ",
                                 parent=self.root)

    # ====== == == fetchdata == == == == == == == ==

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="Face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")

        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ============get cursor===========#
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_radio1.set(data[13])

    # ================update===============
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_gender.get() == "Select Gender" or self.var_address.get() == "" or self.var_phone.get() == "" or self.var_roll.get() == "" or self.var_email.get() == "" or self.var_dob.get() == "" :
            messagebox.showerror("Error", "All Fields Are required", parent=self.root)
        else:
            try:
                if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", self.var_email.get()):
                    if (len(self.var_phone.get()) == 10):
                        Update = messagebox.askyesno("Update", "Do you want update this student details", parent=self.root)
                        if Update > 0:
                            conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                           database="Face_recognizer")
                            my_cursor = conn.cursor()
                            my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",
                                (
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_std_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_radio1.get(),
                                    self.va_std_id.get(),
                                ))
                        else:
                            if not Update:
                                return
                        messagebox.showinfo("Sucess", "Student details sucessfylly updated", parent=self.root)
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                    else:
                        messagebox.showerror("Error", "please enter valid phone no.", parent=self.root)
                else:
                    messagebox.showerror("Error", "Please enter valid Email", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To{str(es)}", parent=self.root)

    # ======deleate function==========#
    def delete_data(self):

        if self.va_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)

        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student",
                                             parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                   database="Face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.va_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Sucessfully Deleated Students details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To{str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")
        self.var_search.set("")
    #search function
    def search(self, ev):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                       database="Face_recognizer")
        my_cursor = conn.cursor()

        try:
            my_cursor.execute("SELECT * FROM student where Name LIKE '%"+self.var_search.get()+"%'")
            row = my_cursor.fetchall()
            # print(row)
            if len(row) > 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in row:
                    self.student_table.insert('', END, values=i)
            else:
                self.student_table.delete(*self.student_table.get_children())
        except Exception as ex:
             messagebox.showerror("Error", f"Error due{str(ex)}")

    # ============genarate data Or take photo sample=========
    def genarate_dataset(self):
        if self.var_radio1.get() == "no":
            messagebox.showerror("Error", "At first select take_photo_sample option", parent=self.root)
        else:
            if self.var_dep.get() == "Select Depeartment" or self.var_std_name.get() == "" or self.va_std_id.get() == "" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_gender.get() == "Select Gender" or self.var_address.get() == "" or self.var_phone.get() == "" or self.var_roll.get() == "" or self.var_email.get() == "" or self.var_dob.get() == "":
                messagebox.showerror("Error", "All Fields Are required", parent=self.root)
            else:
                try:
                    if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", self.var_email.get()):
                        if (len(self.var_phone.get()) == 10):
                            conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                           database="Face_recognizer")
                            my_cursor = conn.cursor()
                            id = (self.va_std_id.get())
                            print(id)
                            query = ("select * from student where Student_id=%s")
                            value = (self.va_std_id.get(),)
                            my_cursor.execute(query, value)
                            row = my_cursor.fetchone()

                            if row != None:

                                # =====================updated======================
                                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_address.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        self.va_std_id.get()
                                                                                                                    ))
                            else:

                                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.va_std_id.get(),
                                    self.var_std_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_email.get(),
                                    self.var_phone.get(),
                                    self.var_address.get(),
                                    self.var_radio1.get()
                                ))

                            conn.commit()
                            self.fetch_data()
                            self.reset_data()
                            conn.close()
                        else:
                            messagebox.showerror("Error", "please enter valid phone no.", parent=self.root)
                    else:
                        messagebox.showerror("Error", "Please enter valid Email", parent=self.root)

                    # =========load predifined data on face========

                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                        # scaling factor-1.3

                        # Minimum Neighbor-5

                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y + h, x:x + w]
                            return face_cropped

                    cap = cv2.VideoCapture(0)
                    img_id = 0






                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path =("data/user."+str(id)+"."+str(img_id)+".jpg")
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)



                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data set compiled!!!!")

                except Exception as es:
                    messagebox.showerror("Error", f"Due To{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
