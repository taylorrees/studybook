import tkinter as tk
import templates.ui as ui
import lesson_list.view as lesson_list_view
import lesson_create.view as lesson_create_view

def main():
    row = 0
    window = tk.Tk()
    window.title('Studybook | Dashboard')

    # Interface

    ui.margin_y(window, px=20, row=row)
    row += 1
    ui.title(window, text='Dashboard', row=row)
    row += 1
    ui.margin_y(window, px=10, row=row)
    row += 1
    tk.Button(window, text='Create Lesson', command=lesson_create_view.main).grid(row=row)
    row += 1
    tk.Button(window, text='View Lessons', command=lesson_list_view.main).grid(row=row)
    row += 1
    tk.Button(window, text='Quit', command=window.destroy).grid(row=row)
    row += 1
    ui.margin_y(window, px=20, row=row)
    row += 1

    window.mainloop()
