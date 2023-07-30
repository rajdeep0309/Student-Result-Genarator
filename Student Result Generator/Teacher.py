from tkinter import *
from turtle import width
from PIL import ImageTk
from tkinter import messagebox
from InputPage import *


class teacher:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Generator")
        self.root.geometry("1535x800+0+0")
        self.root.config(bg="white")
        self.root.focus_force()

        # Background
        self.bg = ImageTk.PhotoImage(file="images/teacher.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # mainheading
        # title=Label(self.root,text="Teacher Login Page",font=("times new roman",40,"bold"),bg="#607B8B",fg="white").place(x=0,y=0,relwidth=1)

        # loginframe
        login = Frame(self.root, bg="#607B8B")
        login.place(x=150, y=300, height=380, width=500)

        title = Label(login, text="Login Here", font=(
            "Impact", 30, "bold"), bg="#607B8B", fg="white").place(x=50, y=30)
        desc = Label(login, text="Teacher/Evaluator Login Area", font=(
            "goudy old style", 17, "bold"), bg="#607B8B", fg="white").place(x=50, y=90)

        user = Label(login, text="Username", font=(
            "goudy old style", 15, "bold"), bg="#607B8B", fg="black").place(x=50, y=140)
        self.txt_user = Entry(login, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_user.place(x=50, y=170, width=350, height=35)

        password = Label(login, text="Password", font=(
            "goudy old style", 15, "bold"), bg="#607B8B", fg="black").place(x=50, y=210)
        self.txt_password = Entry(login, font=(
            "times new roman", 15), bg="lightgray", show="*")
        self.txt_password.place(x=50, y=240, width=350, height=35)

        forget_btn = Button(login, text="Forgot Password?", cursor="hand2", bg="#607B8B",
                            fg="white", bd=0, font=("times new roman", 12)).place(x=50, y=295)
        login_btn = Button(self.root, command=self.login_function, cursor="hand2", text="Login",
                           bg="white", fg="#607B8B", font=("times new roman", 20)).place(x=300, y=650, width=180)

        # footer
        footer = Label(self.root, text="Result Generator Project by IT Students\n-Rifa Akhter Mullick, Shreya Sen, Rajdeep Ghosh, Shoal Koley",
                       font=("times new roman", 15,), bg="#262626", fg="white").pack(side="bottom", fill="x")

    def add_InputPage(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def login_function(self):
        if self.txt_password.get() == "" or self.txt_user.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)

        elif self.txt_user.get() != "Admin" or self.txt_password.get() != "1234":
            messagebox.showerror(
                "Error", "Invalid Username/Password", parent=self.root)

        else:
            messagebox.showinfo(
                "Welcome!", "Welcome Admin!\nYou are now ready to work.")
            self.add_InputPage()
            # login_btn = Button(self.root, command=self.add_InputPage, cursor="hand2", text="Login",
            #                    bg="white", fg="#607B8B", font=("times new roman", 20)).place(x=300, y=650, width=180)
            # add_InputPage(root)

            # messagebox.showinfo(
            #     "Welcome!", "Welcome Admin!\nYou are now ready to work.", parent=self.root)
            # COMMAND = self.add_InputPage


if __name__ == "__main__":
    root = Tk()
    obj = teacher(root)
    root.mainloop()
