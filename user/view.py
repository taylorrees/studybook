# Author: Tom Wynne-Owen

import tkinter as tk
import templates.ui as ui
from user.user import User


class AddUser:

    def __init__(self, root, window):
        self.root = root
        self.window = window
        self.User = User()
        self.build()


    def add(self):
        userAdded = self.User.add_user(self.userID.get(), self.password.get()) 
        
        if (userAdded == True):
            self.window.destroy()
            print("Added user")
        else:
            #display message
            print("failed to add user")

    def build(self):
        row = 0
        user = User()

        ui.margin_y(self.root, px=20, row=row)
        row += 1

        ui.title(self.root, text='Add User', row=row)
        row += 1
        ui.margin_y(self.root, px=10, row=row)
        row += 1

        tk.Label(self.root, text='Username').grid(row=row)
        row += 1
        self.userID = tk.Entry(self.root)
        self.userID.grid(row=row)
        row += 1

        tk.Label(self.root, text='Password').grid(row=row)
        row += 1
        self.password = tk.Entry(self.root)
        self.password.grid(row=row)
        row += 1

        ui.margin_y(self.root, px=20, row=row)
        command = lambda : self.add()
        tk.Button(self.root, text='Add', command=command).grid(row=row)

        row += 1
        ui.margin_y(self.root, px=20, row=row)
        row += 1
        


def main():
    window = tk.Tk()
    window.title('Studybook | Add User')
    centered_frame = tk.Frame(window)

    app = AddUser(centered_frame, window)

    centered_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    window.geometry(ui.center(window))
    window.mainloop()


