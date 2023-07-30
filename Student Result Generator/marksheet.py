# from InputPage import *
from tkinter import *
from PIL import ImageGrab
import webbrowser
# import pyautogui
from pymongo import *
from PIL import Image, ImageTk
from PIL import Image
from tkinter import ttk, messagebox
# from InputPage import *
# from  pyautogui import *


# db = MongoClient("mongodb://localhost:27017")['Student']


def method(data):
    return data


class result:
    # Take Screenshot.

    # x = CourseClass.sub1_total
    # data=

    # print(name, roll, sgpa)

    def __init__(self, root, data, sem):
        self.root = root
        self.root.title("Result Generator")
        self.root.geometry("1535x800+0+0")
        self.root.config(bg="white")
        self.root.focus_force()
        self.data = data
        self.sem = sem

        db = MongoClient("mongodb://localhost:27017")['Student']
        a = db.StudentTheory.find_one({'roll': data, 'sem': sem})
        b = a.items()
        c = list(b).pop(1)
        self.name = list(c).pop(1)

        c = list(b).pop(2)
        self.roll = list(c).pop(1)

        c = list(b).pop(3)
        self.dept = list(c).pop(1)

        c = list(b).pop(4)
        self.sem = list(c).pop(1)

        c = list(b).pop(5)
        self.ca_1 = list(c).pop(1)

        c = list(b).pop(6)
        self.marks_1 = list(c).pop(1)

        c = list(b).pop(7)
        self.att_1 = list(c).pop(1)
        c = list(b).pop(8)
        self.ca_2 = list(c).pop(1)

        c = list(b).pop(9)
        self. marks_2 = list(c).pop(1)

        c = list(b).pop(10)
        self.att_2 = list(c).pop(1)

        c = list(b).pop(11)
        self.ca_3 = list(c).pop(1)

        c = list(b).pop(12)
        self.marks_3 = list(c).pop(1)

        c = list(b).pop(13)
        self.att_3 = list(c).pop(1)

        c = list(b).pop(14)
        self.ca_4 = list(c).pop(1)

        c = list(b).pop(15)
        self.marks_4 = list(c).pop(1)

        c = list(b).pop(16)
        self.att_4 = list(c).pop(1)

        c = list(b).pop(17)
        self.pca_1 = list(c).pop(1)

        c = list(b).pop(18)
        self.pcamarks_1 = list(c).pop(1)

        c = list(b).pop(19)
        self.pca_2 = list(c).pop(1)

        c = list(b).pop(20)
        self.pcamarks_2 = list(c).pop(1)

        c = list(b).pop(21)
        self.credit_1 = list(c).pop(1)

        c = list(b).pop(22)
        self.points_1 = list(c).pop(1)

        c = list(b).pop(23)
        self.creditpoints_1 = list(c).pop(1)

        c = list(b).pop(24)
        self.credit_2 = list(c).pop(1)

        c = list(b).pop(25)
        self.points_2 = list(c).pop(1)

        c = list(b).pop(26)
        self.creditpoints_2 = list(c).pop(1)

        c = list(b).pop(27)
        self.credit_3 = list(c).pop(1)

        c = list(b).pop(28)
        self.points_3 = list(c).pop(1)

        c = list(b).pop(29)

        self.creditpoints_3 = list(c).pop(1)

        c = list(b).pop(30)

        self.credit_4 = list(c).pop(1)

        c = list(b).pop(31)

        self.points_4 = list(c).pop(1)

        c = list(b).pop(32)

        self.creditpoints_4 = list(c).pop(1)

        c = list(b).pop(33)
        self.credit_5 = list(c).pop(1)

        c = list(b).pop(34)
        self.points_5 = list(c).pop(1)

        c = list(b).pop(35)
        self.creditpoints_5 = list(c).pop(1)

        c = list(b).pop(36)
        self.credit_6 = list(c).pop(1)

        c = list(b).pop(37)
        self.points_6 = list(c).pop(1)

        c = list(b).pop(38)
        self.creditpoints_6 = list(c).pop(1)

        c = list(b).pop(39)
        self.sgpa = list(c).pop(1)

        # dp
        self.bg_image = Image.open("images/studentdp.png")
        self.bg_image = self.bg_image.resize((150, 150))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.lbl_bg = Label(self.root, image=self.bg_image).place(x=1320, y=70)

        # title
        title = Label(self.root, text="  Result", font=(
            "times new roman", 30, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1)

        # Student Information
        name = Label(self.root, text="Student Name: ", font=(
            "times new roman", 20), bg="white", fg="black").place(x=30, y=70)

        roll = Label(self.root, text="Roll Number: ", font=(
            "times new roman", 20), bg="white", fg="black").place(x=30, y=110)
        course = Label(self.root, text="Course Name: ", font=(
            "times new roman", 20), bg="white", fg="black").place(x=30, y=150)
        sem = Label(self.root, text="Semester: ", font=(
            "times new roman", 20), bg="white", fg="black").place(x=30, y=190)

        # student information put
        name_final = Label(self.root, text=self.name, font=("times new roman",
                                                            12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        name_final.place(x=250, y=70, width=300, height=40)

        roll_final = Label(self.root, text=self.roll, font=("times new roman",
                                                            12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        roll_final.place(x=250, y=110, width=125, height=40)

        course_final = Label(self.root, text=self.dept, font=("times new roman",
                                                              12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        course_final.place(x=250, y=150, width=125, height=40)

        sem_final = Label(self.root, text=self.sem, font=("times new roman",
                                                          12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        sem_final.place(x=250, y=190, width=125, height=40)

        # Table
        #theory=Label(self.root,text="Theory",font=("times new roman",15),bg="white",fg="black",bd=1,relief="solid").place(x=35,y=250,width=770,height=50)
        #prac=Label(self.root,text="Practical",font=("times new roman",15),bg="white",fg="black",bd=1,relief="solid").place(x=771,y=250,width=737,height=50)

        # Table heading
        sl = Label(self.root, text="SL.", font=("times new roman", 15, "bold"), bg="#607B8B",
                   fg="white", bd=1, relief="solid").place(x=35, y=250, width=75, height=50)
        sub = Label(self.root, text="SUBJECTS", font=("times new roman", 15, "bold"),
                    bg="#607B8B", fg="white", bd=1, relief="solid").place(x=110, y=250, width=625, height=50)
        ca = Label(self.root, text="CA/ PCA", font=("times new roman", 15, "bold"), bg="#607B8B",
                   fg="white", bd=1, relief="solid").place(x=735, y=250, width=125, height=50)
        marks = Label(self.root, text="MARKS", font=("times new roman", 15, "bold"), bg="#607B8B",
                      fg="white", bd=1, relief="solid").place(x=860, y=250, width=125, height=50)
        attendance = Label(self.root, text="ATTENDANCE", font=("times new roman", 13, "bold"),
                           bg="#607B8B", fg="white", bd=1, relief="solid").place(x=985, y=250, width=125, height=50)
        credit = Label(self.root, text="CREDIT", font=("times new roman", 15, "bold"), bg="#607B8B",
                       fg="white", bd=1, relief="solid").place(x=1110, y=250, width=125, height=50)
        point = Label(self.root, text="POINTS", font=("times new roman", 15, "bold"), bg="#607B8B",
                      fg="white", bd=1, relief="solid").place(x=1235, y=250, width=125, height=50)
        crpt = Label(self.root, text="CREDIT\nPOINTS", font=("times new roman", 11, "bold"),
                     bg="#607B8B", fg="white", bd=1, relief="solid").place(x=1360, y=250, width=125, height=50)

        # serial column
        serial1 = Label(self.root, text="1.", font=("times new roman", 12, "bold"), bg="white",
                        fg="black", bd=1, relief="solid").place(x=35, y=300, width=75, height=50)
        serial2 = Label(self.root, text="2.", font=("times new roman", 12, "bold"), bg="white",
                        fg="black", bd=1, relief="solid").place(x=35, y=350, width=75, height=50)
        serial3 = Label(self.root, text="3.", font=("times new roman", 12, "bold"), bg="white",
                        fg="black", bd=1, relief="solid").place(x=35, y=400, width=75, height=50)
        serial4 = Label(self.root, text="4.", font=("times new roman", 12, "bold"), bg="white",
                        fg="black", bd=1, relief="solid").place(x=35, y=450, width=75, height=50)
        serial5 = Label(self.root, text="5.", font=("times new roman", 12, "bold"), bg="white",
                        fg="black", bd=1, relief="solid").place(x=35, y=500, width=75, height=50)
        serial6 = Label(self.root, text="6.", font=("times new roman", 12, "bold"), bg="white",
                        fg="black", bd=1, relief="solid").place(x=35, y=550, width=75, height=50)

        # subject column
        sub1 = Label(self.root, text="Subject 1", font=("times new roman", 12, "bold"),
                     bg="white", fg="black", bd=1, relief="solid").place(x=110, y=300, width=625, height=50)
        sub2 = Label(self.root, text="Subject 2", font=("times new roman", 12, "bold"),
                     bg="white", fg="black", bd=1, relief="solid").place(x=110, y=350, width=625, height=50)
        sub3 = Label(self.root, text="Subject 3", font=("times new roman", 12, "bold"),
                     bg="white", fg="black", bd=1, relief="solid").place(x=110, y=400, width=625, height=50)
        sub4 = Label(self.root, text="Subject 4", font=("times new roman", 12, "bold"),
                     bg="white", fg="black", bd=1, relief="solid").place(x=110, y=450, width=625, height=50)
        sub5 = Label(self.root, text="Lab 1", font=("times new roman", 12, "bold"), bg="white",
                     fg="black", bd=1, relief="solid").place(x=110, y=500, width=625, height=50)
        sub6 = Label(self.root, text="Lab 2", font=("times new roman", 12, "bold"), bg="white",
                     fg="black", bd=1, relief="solid").place(x=110, y=550, width=625, height=50)

        # CA column
        ca1 = Label(self.root, text=self.ca_1, font=("times new roman", 12),
                    bg="white", fg="black", bd=1, relief="solid")
        ca1.place(x=735, y=300, width=125, height=50)
        ca2 = Label(self.root, text=self.ca_2, font=("times new roman", 12),
                    bg="white", fg="black", bd=1, relief="solid")
        ca2.place(x=735, y=350, width=125, height=50)
        ca3 = Label(self.root, text=self.ca_3, font=("times new roman", 12),
                    bg="white", fg="black", bd=1, relief="solid")
        ca3.place(x=735, y=400, width=125, height=50)
        ca4 = Label(self.root, text=self.ca_4, font=("times new roman", 12),
                    bg="white", fg="black", bd=1, relief="solid")
        ca4.place(x=735, y=450, width=125, height=50)
        ca5 = Label(self.root, text=self.pca_1, font=("times new roman", 12),
                    bg="white", fg="black", bd=1, relief="solid")
        ca5.place(x=735, y=500, width=125, height=50)
        ca6 = Label(self.root, text=self.pca_2, font=("times new roman", 12),
                    bg="white", fg="black", bd=1, relief="solid")
        ca6.place(x=735, y=550, width=125, height=50)

        # marks column
        marks1 = Label(self.root, text=self.marks_1, font=(
            "times new roman", 12), bg="white", fg="black", bd=1, relief="solid")
        marks1.place(x=860, y=300, width=125, height=50)
        marks2 = Label(self.root, text=self.marks_2, font=(
            "times new roman", 12), bg="white", fg="black", bd=1, relief="solid")
        marks2.place(x=860, y=350, width=125, height=50)
        marks3 = Label(self.root, text=self.marks_3, font=(
            "times new roman", 12), bg="white", fg="black", bd=1, relief="solid")
        marks3.place(x=860, y=400, width=125, height=50)
        marks4 = Label(self.root, text=self.marks_4, font=(
            "times new roman", 12), bg="white", fg="black", bd=1, relief="solid")
        marks4.place(x=860, y=450, width=125, height=50)
        marks5 = Label(self.root, text=self.pcamarks_1, font=(
            "times new roman", 12), bg="white", fg="black", bd=1, relief="solid")
        marks5.place(x=860, y=500, width=125, height=50)
        marks6 = Label(self.root, text=self.pcamarks_2, font=(
            "times new roman", 12), bg="white", fg="black", bd=1, relief="solid")
        marks6.place(x=860, y=550, width=125, height=50)

        # Attendance column
        attendance1 = Label(self.root, text=self.att_1, font=(
            "times new roman", 12), bg="white", fg="black", bd=1, relief="solid")
        attendance1.place(x=985, y=300, width=125, height=50)
        attendance2 = Label(self.root, text=self.att_2, font=(
            "times new roman", 12), bg="white", fg="black", bd=1, relief="solid")
        attendance2.place(x=985, y=350, width=125, height=50)
        attendance3 = Label(self.root, text=self.att_3, font=(
            "times new roman", 12), bg="white", fg="black", bd=1, relief="solid")
        attendance3.place(x=985, y=400, width=125, height=50)
        attendance4 = Label(self.root, text=self.att_4, font=(
            "times new roman", 12), bg="white", fg="black", bd=1, relief="solid")
        attendance4.place(x=985, y=450, width=125, height=50)
        attendance5 = Label(self.root, text="-", font=("times new roman",
                            25, "bold"), bg="white", fg="black", bd=1, relief="solid")
        attendance5.place(x=985, y=500, width=125, height=50)
        attendance6 = Label(self.root, text="-", font=("times new roman",
                            25, "bold"), bg="white", fg="black", bd=1, relief="solid")
        attendance6.place(x=985, y=550, width=125, height=50)

        # Credit column
        credit1 = Label(self.root, text=self.credit_1, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        credit1.place(x=1110, y=300, width=125, height=50)
        credit2 = Label(self.root, text=self.credit_2, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        credit2.place(x=1110, y=350, width=125, height=50)
        credit3 = Label(self.root, text=self.credit_3, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        credit3.place(x=1110, y=400, width=125, height=50)
        credit4 = Label(self.root, text=self.credit_4, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        credit4.place(x=1110, y=450, width=125, height=50)
        credit5 = Label(self.root, text=self.credit_5, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        credit5.place(x=1110, y=500, width=125, height=50)
        credit6 = Label(self.root, text=self.credit_6, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        credit6.place(x=1110, y=550, width=125, height=50)
        s = 12
        # Points column
        point1 = Label(self.root, text=self.points_1, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        point1.place(x=1235, y=300, width=125, height=50)
        point2 = Label(self.root, text=self.points_2, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        point2.place(x=1235, y=350, width=125, height=50)
        point3 = Label(self.root, text=self.points_3, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        point3.place(x=1235, y=400, width=125, height=50)
        point4 = Label(self.root, text=self.points_4, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        point4.place(x=1235, y=450, width=125, height=50)
        point5 = Label(self.root, text=self.points_5, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        point5.place(x=1235, y=500, width=125, height=50)
        point6 = Label(self.root, text=self.points_6, font=(
            "times new roman", 12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        point6.place(x=1235, y=550, width=125, height=50)

        # credit Points
        crpt1 = Label(self.root, text=self.creditpoints_1, font=("times new roman",
                      12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        crpt1.place(x=1360, y=300, width=125, height=50)
        crpt2 = Label(self.root, text=self.creditpoints_2, font=("times new roman",
                      12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        crpt2.place(x=1360, y=350, width=125, height=50)
        crpt3 = Label(self.root, text=self.creditpoints_3, font=("times new roman",
                      12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        crpt3.place(x=1360, y=400, width=125, height=50)
        crpt4 = Label(self.root, text=self.creditpoints_4, font=("times new roman",
                      12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        crpt4.place(x=1360, y=450, width=125, height=50)
        crpt5 = Label(self.root, text=self.creditpoints_5, font=("times new roman",
                      12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        crpt5.place(x=1360, y=500, width=125, height=50)
        crpt6 = Label(self.root, text=self.creditpoints_6, font=("times new roman",
                      12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        crpt6.place(x=1360, y=550, width=125, height=50)

        # sgpa
        sgpa = Label(self.root, text="Sgpa:", font=(
            "times new roman", 20), bg="white", fg="black").place(x=35, y=650)

        # sgpa put
        sgpa_final = Label(self.root, text=self.sgpa, font=("times new roman",
                                                            12, "bold"), bg="white", fg="black", bd=1, relief="solid")
        sgpa_final.place(x=150, y=650, width=125, height=50)

        # footer
        footer = Label(self.root, text="Result Generator Project by IT Students\n-Rifa Akhter Mullick, Shreya Sen, Rajdeep Ghosh, Shoal Koley",
                       font=("times new roman", 15,), bg="#262626", fg="white").pack(side="bottom", fill="x")
        # function of pdf generator

        def pdf():
            #
            snapshot = ImageGrab.grab()
            save_path = "C:\\Users\\rajdeep ghosh\\OneDrive\\Desktop\python\project_1\\resukt\\MyResult.pdf"
            snapshot.save(save_path)
            webbrowser.open_new_tab(
                "C:\\Users\\rajdeep ghosh\\OneDrive\\Desktop\\python\\project_1\\resukt\\MyResult.pdf")
        # Generate pdf

        btn_del = Button(self.root, text="Generate PDF", command=pdf, font=("times new roman", 15, "bold"),
                         bg="red", fg="white", cursor="hand2").place(x=1340, y=695, width=150, height=35)


if __name__ == "__main__":
    root = Tk()
    obj = result(root)
    root.mainloop()
