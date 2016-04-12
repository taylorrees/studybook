import tkinter as tk
import templates.ui as ui

def main():
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
    username = tk.Entry(window)
    username.grid(row=row)
    row += 1

    tk.Label(window, text='Password').grid(sticky=tk.W)
    password = tk.Entry(window)
    password.grid(row=row)
    row += 1

    tk.Button(window, text='Login', command=getLogIn(usernamein.get(), passwordin.get())).grid(row=row)
    row += 1
    ui.margin_y(window, px=20, row=row)
    row += 1

    window.mainloop()

main()
