import tkinter as tk
import templates.ui as ui
import lesson_list.view as lesson_list_view
import lesson_create.view as lesson_create_view

def login():
    row = 0
    window = tk.Tk()
    window.title('Studybook | Login')
    ui.margin_y(window, px=20, row=row)
    row += 1
    ui.title(window, text='Login', row=row)
    row += 1
    ui.margin_y(window, px=10, row=row)
    row += 1
    tk.Label(window, text='Username').grid(sticky=tk.W)
    usernamein = tk.Entry(window)
    usernamein.grid(row=row)
    row += 1
    tk.Label(window, text='Password').grid(sticky=tk.W)
    passwordin = tk.Entry(window)
    passwordin.grid(row=row)
    row += 1
    tk.Button(window, text='Login', command=getLogIn(usernamein.get(), passwordin.get())).grid(row=row)
    row += 1
    ui.margin_y(window, px=20, row=row)
    row += 1

    window.mainloop()

def getLogIn(Username, Password):
	return True

login()