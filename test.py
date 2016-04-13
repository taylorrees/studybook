import tkinter as tk
import templates.ui as ui

window = tk.Tk()
window.title("Studybook | Lesson Viewer")
img = tk.PhotoImage(file="lesson/img/lorem.gif")
tk.Label(window, image=img).grid(row=3, column=1)
window.mainloop()
