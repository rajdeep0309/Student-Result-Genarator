#from cProfile import label
from PIL import Image, ImageTk  # pip install pillow
from tkinter import *
from turtle import width
import PIL.Image
import os
from tkinter import ttk, messagebox
from Teacher import teacher
from student import student


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Generator")
        self.root.geometry("1525x800+0+0")
        self.root.config(bg="white")
        # icons
        self.logo_dash = ImageTk.PhotoImage(file="images/result.png")
        # self.logo_dash=Image.open("images/result.png")
        # self.logo_dash=self.logo_dash.resize((50,50))
        # self.logo_dash=ImageTk.PhotoImage(self.logo_dash)

        # self.lbl_logo=Label(self.root,image=self).place(x=200,y=10)

        # Background
        self.bg = ImageTk.PhotoImage(file="images/results.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(
            x=0, y=65, relwidth=1, relheight=1)

        # mainheading
        title = Label(self.root, text="  Result Generator", compound="left", image=self.logo_dash, font=(
            "times new roman", 40, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1)
        # menu
        M_Frame = LabelFrame(self.root, text="Menus", font=(
            "times new roman", 15, "bold"), bg="#033054", fg="white")
        M_Frame.place(x=80, y=130, width="350", height="360")

        b1 = Button(M_Frame, text="Teacher", font=("times new roman", 20, "bold"), bg="#607B8B",
                    fg="white", cursor="hand2", command=self.add_teacher).place(x=34, y=20, width=275, height=70)
        b2 = Button(M_Frame, text="Student", font=("times new roman", 20, "bold"), bg="#607B8B",
                    fg="white", cursor="hand2", command=self.add_student).place(x=34, y=120, width=275, height=70)
        b3 = Button(M_Frame, text="Logout", font=("times new roman", 20, "bold"), bg="#607B8B",
                    fg="white", cursor="hand2", command=self.logout).place(x=34, y=220, width=275, height=70)

        # mainpic
        # update details
        count = 0
        self.lbl_visit = Label(self.root, text="Total Visits\n[0]", font=(
            "times new roman", 20), bd=10, relief="ridge", bg="#033054", fg="white")
        self.lbl_visit.place(x=710, y=580, width=300, height=100)

        self.lbl_students = Label(self.root, text="Total Students\n[0]", font=(
            "times new roman", 20), bd=10, relief="ridge", bg="#033054", fg="white")
        self.lbl_students.place(x=1125, y=580, width=300, height=100)

        # footer
        footer = Label(self.root, text="Result Generator Project by IT Students\n-Rifa Akhter Mullick, Shreya Sen, Rajdeep Ghosh, Shoal Koley",
                       font=("times new roman", 15,), bg="#262626", fg="white").pack(side="bottom", fill="x")

    def add_teacher(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = teacher(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = student(self.new_win)

    def logout(self):
        op = messagebox.askyesno(
            "Confirm", "Are you sure you want to Logout?", parent=self.root)
        if op == True:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
