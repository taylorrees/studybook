# Author: Wiliam Goalie Thomas

import tkinter as tk
import templates.ui as ui
import dashboard.view as dashboard
from user.user import User

class Login:

    def __init__(self, root, window):
        self.root = root
        self.window = window
        self.user = User()
        self.build()


    def login(self):
        self.user.login(self.username.get(), self.password.get())
        login_status = self.user.login_status

        if login_status == 1:
            self.window.destroy()
            dashboard.main(self.user.user_id, login_status)

        if login_status == 2:
            self.window.destroy()
            dashboard.main(self.user.user_id, login_status)


    def build(self):
        row = 0
        user = User()

        ui.margin_y(self.root, px=20, row=row)
        row += 1

        ui.title(self.root, text='Login', row=row)
        row += 1
        ui.margin_y(self.root, px=10, row=row)
        row += 1

        tk.Label(self.root, text='Username').grid(row=row)
        row += 1
        self.username = tk.Entry(self.root)
        self.username.grid(row=row)
        row += 1

        tk.Label(self.root, text='Password').grid(row=row)
        row += 1
        self.password = tk.Entry(self.root, show="*")
        self.password.grid(row=row)
        row += 1

        ui.margin_y(self.root, px=20, row=row)
        command = lambda : self.login()
        tk.Button(self.root, text='Login', command=command).grid(row=row)

        row += 1
        ui.margin_y(self.root, px=20, row=row)
        row += 1


def main():
    window = tk.Tk()
    window.title('Studybook | Login')
    centered_frame = tk.Frame(window)

    app = Login(centered_frame, window)

    centered_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    window.geometry(ui.center(window))
    window.mainloop()
