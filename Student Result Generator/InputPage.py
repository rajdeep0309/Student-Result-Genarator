from tkinter import *
from cProfile import label
from sub_lab import *
from sub_theory import *
from marksheet import *
from pymongo import *
db = MongoClient("mongodb://localhost:27017")['Student']


class CourseClass:

    def __init__(self, root):

        self.root = root

        self.root.geometry("1525x800+0+0")

        self.root.title("Resut Generator")

        self.root.config(bg="white")

        title = Label(self.root, text='Manage Details', font=(
            "times new roman", 30, "bold"), bg="#033054", fg="white").place(x=0, y=10, relwidth=1)

        self.root.focus_force()

        # ====title====

        # title=Label(self.root,text=" Manage Details",font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=50,y=70,relwidth=2000,height=10)

        # ====variables====

        self.var_subject1ca = IntVar()  # ca

        self.var_subject1marks = IntVar()

        self.var_subject1att = IntVar()

        self.var_subject2ca = IntVar()

        self.var_subject2marks = IntVar()

        self.var_subject2att = IntVar()

        self.var_subject3ca = IntVar()

        self.var_subject3marks = IntVar()

        self.var_subject3att = IntVar()

        self.var_subject4ca = IntVar()

        self.var_subject4marks = IntVar()

        self.var_subject4att = IntVar()

        self.var_labpca = IntVar()

        self.var_labpracmarks = IntVar()

        self.var_lab2pca = IntVar()

        self.var_lab2pracmarks = IntVar()

        self.var_name = StringVar()

        self.var_dept = StringVar()

        self.var_sem = IntVar()

        self.var_rollno = IntVar()

        # ====widgets-theory=====

        lbl_theory = Label(self.root, text="THEORY", font=(
            "goudy old style", 21, "bold"), bg="white").place(x=120, y=200)

        lbl_subject = Label(self.root, text="SUBJECT", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=30, y=280)

        lbl_ca = Label(self.root, text="  CA   ", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=180, y=280)

        lbl_marks = Label(self.root, text="MARKS", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=270, y=280)

        lbl_sttandance = Label(self.root, text="ATTENDANCE", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=380, y=280)

        lbl_subject1 = Label(self.root, text="SUBJECT-1", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=30, y=340)

        lbl_subject2 = Label(self.root, text="SUBJECT-2", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=30, y=380)

        lbl_subject3 = Label(self.root, text="SUBJECT-3", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=30, y=420)

        lbl_subject4 = Label(self.root, text="SUBJECT-4", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=30, y=460)

        # ====widgets-practical====

        lbl_practical = Label(self.root, text="PRACTICAL", font=(
            "goudy old style", 21, "bold"), bg="white").place(x=1050, y=200)

        lbl_lab = Label(self.root, text="LAB", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=1000, y=280)

        lbl_pca = Label(self.root, text="PCA", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=1100, y=280)

        lbl_markss = Label(self.root, text="MARKS", font=(
            "goudy old style", 18, "bold"), bg="white").place(x=1200, y=280)

        lbl_lab1 = Label(self.root, text="LAB-1", font=("goudy old style",
                         15, "bold"), bg="white").place(x=1000, y=340)

        lbl_lab2 = Label(self.root, text="LAB-2", font=("goudy old style",
                         15, "bold"), bg="white").place(x=1000, y=380)

        # ====footer====

        lbl_footer = Label(self.root, text="Result Generator Project by IT Students\n-Rifa Akhter Mullick, Shreya Sen, Rajdeep Ghosh, Shoal Koley",
                           font=("times new roman", 10,), bg="#262626", fg="white").pack(side="bottom", fill="x")

        # ====entry fields- theory====

        self.txt_subject1 = Entry(self.root, textvariable=self.var_subject1ca, font=(
            "goudy old style", 15, "bold"), bg="light yellow")

        self.txt_subject1.place(x=180, y=343, width=70, height=25)

        txt_subject11 = Entry(self.root, textvariable=self.var_subject1marks, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=270, y=343, width=70, height=25)

        txt_subject111 = Entry(self.root, textvariable=self.var_subject1att, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=380, y=343, width=70, height=25)

        txt_subject2 = Entry(self.root, textvariable=self.var_subject2ca, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=180, y=383, width=70, height=25)

        txt_subject22 = Entry(self.root, textvariable=self.var_subject2marks, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=270, y=383, width=70, height=25)

        txt_subject222 = Entry(self.root, textvariable=self.var_subject2att, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=380, y=383, width=70, height=25)

        txt_subject3 = Entry(self.root, textvariable=self.var_subject3ca, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=180, y=423, width=70, height=25)

        txt_subject33 = Entry(self.root, textvariable=self.var_subject3marks, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=270, y=423, width=70, height=25)

        txt_subject333 = Entry(self.root, textvariable=self.var_subject3att, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=380, y=423, width=70, height=25)

        txt_subject4 = Entry(self.root, textvariable=self.var_subject4ca, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=180, y=463, width=70, height=25)

        txt_subject44 = Entry(self.root, textvariable=self.var_subject4marks, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=270, y=463, width=70, height=25)

        txt_subject444 = Entry(self.root, textvariable=self.var_subject4att, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=380, y=463, width=70, height=25)

        # ====entry fields- practical====

        self.txt_lab1 = Entry(self.root, textvariable=self.var_labpca, font=(
            "goudy old style", 15, "bold"), bg="light yellow")

        self.txt_lab1.place(x=1100, y=343, width=70, height=25)

        txt_lab11 = Entry(self.root, textvariable=self.var_labpracmarks, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=1200, y=343, width=70, height=25)

        txt_lab2 = Entry(self.root, textvariable=self.var_lab2pca, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=1100, y=383, width=70, height=25)

        txt_lab22 = Entry(self.root, textvariable=self.var_lab2pracmarks, font=(
            "goudy old style", 15, "bold"), bg="light yellow").place(x=1200, y=383, width=70, height=25)

        # ====info- widgets======

        lbl_name = Label(self.root, text="NAME:", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=450, y=100)

        lbl_dept = Label(self.root, text="DEPARTMENT:", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=450, y=135)

        lbl_sem = Label(self.root, text="SEMESTER:", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=450, y=170)

        lbl_rollno = Label(self.root, text="ROLL NO:", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=450, y=205)

        # ====entry info=====

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=(
            "goudy old style", 15, "bold"), bg="light yellow")

        self.txt_name.place(x=550, y=100, width=250, height=25)

        self.txt_dept = Entry(self.root, textvariable=self.var_dept, font=(
            "goudy old style", 15, "bold"), bg="light yellow")

        self.txt_dept.place(x=630, y=135, width=171, height=25)

        self.txt_sem = Entry(self.root, textvariable=self.var_sem, font=(
            "goudy old style", 15, "bold"), bg="light yellow")

        self.txt_sem.place(x=590, y=170, width=70, height=25)

        self.txt_rollno = Entry(self.root, textvariable=self.var_rollno, font=(
            "goudy old style", 15, "bold"), bg="light yellow")

        self.txt_rollno.place(x=570, y=205, width=200, height=25)

        # ====buttons====

        self.btn_add = Button(self.root, text="Save", font=(
            "goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.save)

        self.btn_add.place(x=50, y=550, width=110, height=40)

        # self.btn_update = Button(self.root, text="Update", font=(
        #     "goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2")

        # self.btn_update.place(x=200, y=550, width=110, height=40)

        # self.btn_delete = Button(self.root, text="Delete", font=(
        #     "goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2")

        # self.btn_delete.place(x=350, y=550, width=110, height=40)

        self.btn_pdf = Button(self.root, text="Generate Result", font=(
            "goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2", command=self.navigate)

        self.btn_pdf.place(x=1100, y=550, width=200, height=40)

    def save(self):
        s1 = sub_theo(self.var_subject1marks.get(),
                      self.var_subject1ca.get(), self.var_subject1att.get())
        t1 = s1.total()
        cr1 = s1.return_creditPoint()
        returncredit1 = s1.return_credit()
        point1 = s1.return_points()

        s2 = sub_theo(self.var_subject2marks.get(),
                      self.var_subject2ca.get(), self.var_subject2att.get())
        t2 = s2.total()
        cr2 = s2.return_creditPoint()
        returncredit2 = s2.return_credit()
        point2 = s2.return_points()
        s3 = sub_theo(self.var_subject3marks.get(),
                      self.var_subject3ca.get(), self.var_subject3att.get())
        t3 = s3.total()
        cr3 = s3.return_creditPoint()
        returncredit3 = s3.return_credit()
        point3 = s3.return_points()
        s4 = sub_theo(self.var_subject4marks.get(),
                      self.var_subject4ca.get(), self.var_subject4att.get())
        t4 = s4.total()
        cr4 = s4.return_creditPoint()
        returncredit4 = s4.return_credit()
        point4 = s1.return_points()
        p1 = sub_lab(self.var_labpracmarks.get(), self.var_labpca.get())
        pt1 = p1.total()
        pcr1 = p1.return_creditPoint()
        returnp1 = p1.return_credit()
        pracpoint1 = p1.return_points()
        p2 = sub_lab(self.var_lab2pracmarks.get(), self.var_lab2pca.get())
        pt2 = p2.total()
        pcr2 = p2.return_creditPoint()
        returnp2 = p2.return_credit()
        pracpoint2 = p2.return_points()
        total_creditspoint = (cr1+cr2 + cr3+cr4+pcr1+pcr2)
        total_credit = (returncredit1+returncredit2 +
                        returncredit3 + returncredit4+returnp1+returnp2)

        if total_credit == 0:
            sgpa = 0

        else:
            sgpa = round(total_creditspoint/total_credit, 2)
            # print(total_creditspoint, ":", total_credit)

            db.StudentTheory.insert_one({
                "name": self.var_name.get(),
                "roll": self.var_rollno.get(),
                "department": self.var_dept.get(),
                "sem": self.var_sem.get(),
                "ca1": self.var_subject1ca.get(),
                "marks1": self.var_subject1marks.get(),
                "attendence1": self.var_subject1att.get(),
                "ca2": self.var_subject2ca.get(),
                "marks2": self.var_subject2marks.get(),
                "attendence2": self.var_subject2att.get(),
                "ca3":  self.var_subject3ca.get(),
                "marks3":  self.var_subject3marks.get(),
                "attendence3":  self.var_subject3att.get(),
                "ca4":  self.var_subject4ca.get(),
                "marks4":  self.var_subject4marks.get(),
                "attendence4":  self.var_subject4att.get(),
                "pca1": self.var_labpca.get(),
                "pcamarks1": self.var_labpracmarks.get(),
                "pca2": self.var_lab2pca.get(),
                "pcamarks2": self.var_lab2pracmarks.get(),
                "credit1": float(returncredit1),
                "points1": float(point1),
                "creditpoints1":  float(cr1),
                "credit2": float(returncredit2),
                "points2": float(point2),
                "creditpoints2": float(cr2),
                "credit3": float(returncredit3),
                "points3": float(point3),
                "creditpoints3": float(cr3),
                "credit4": float(returncredit4),
                "points4": float(point4),
                "creditpoints4": float(cr4),
                "credit5": float(returnp1),
                "points5": float(pracpoint1),
                "creditpoints5": float(pcr1),
                "credit6": float(returnp2),
                "points6": float(pracpoint2),
                "creditpoints6": float(pcr2),
                "sgpa": sgpa

            })

        # d=method(self.var_rollno.get())
        # print(d)

    def navigate(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = result(
            self.new_win, self.var_rollno.get(), self.var_sem.get())


if __name__ == "__main__":

    root = Tk()

    obj = CourseClass(root)

    root.mainloop()


# data base connect todo
# maksheet page data --> calculation done then
