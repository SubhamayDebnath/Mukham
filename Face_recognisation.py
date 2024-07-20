from tkinter import *
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import os
import numpy as np


class Face_recognisation:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Mukham")
        self.root.minsize(1280, 720)
        self.root.iconbitmap('images/icon.ico')

        main_frame = Frame(self.root, bg="white")
        main_frame.place(x=0, y=0, relheight=1, relwidth=1)

        # side image
        side_bg = Image.open(r"images/2499052.jpg")
        side_bg = side_bg.resize((550, 550))
        self.sideImage = ImageTk.PhotoImage(side_bg)

        side_image = Label(main_frame, image=self.sideImage)
        side_image.place(x=500, y=150)
        titleLabel = Label( self.root,text = "MUKHAM", font = ("arial", 25, "bold"), fg = "darkblue", bg = "white",
                              pady=20, padx=15).pack()

        #backgroundImage = Image.open(r"images/face-recognition-ar-hologram-screen-smart-technology.jpg")
        #backgroundImage = backgroundImage.resize((2000, 2000), Image.ANTIALIAS)
        #self.bgImage = ImageTk.PhotoImage(backgroundImage)
        #bg_lbl = Label(self.root, image=self.bgImage)
        #bg_lbl.place(x=0, y=0, relheight=1, relwidth=1)
       # titleLabel = Label(, text="FACE RECOGNITION ", font=("arial", 25, "bold"), fg="GREEN", bg="black",
        #                   pady=20, padx=15).pack()

        b1_1 = Button(self.root, text="Recognition", cursor="hand2", command=self.face_recog, width=37,bd=5,border=5,
                      font=("times new roman", 13, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=605,y=650)

    ############==========ATTANDENCE=============#############
    def mark_attendence(self, i, r, n, d):
        with open("mukham.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")

            dtString = now.strftime("%H:%M:%S")

            name_list = []
            for line in myDataList:
                entry = line.split((","))
                if ((entry[5])==d1):
                    name_list.append(entry[0])


            if ((i not in name_list)):
                if (dtString > "09:29:00") and (dtString < "11:00:00"):

                    f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")

    ###########===========FACE RECOGNISATION=========##########
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="1234",
                                               database="Face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 82:
                    cv2.putText(img, f"Student_id:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255))
                    self.mark_attendence(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255))

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognisation(root)
    root.mainloop()
