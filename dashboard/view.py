import tkinter as tk
import templates.ui as ui
import lesson_list.view as lesson_list_view
import lesson_create.view as lesson_create_view

def main(login_status):

    # Quick and dirty dashboard.
    # Needs work once all views are
    # in place.
    #

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

    # If a lecturer is logged in
    # show them the lecturer specific actions
    if login_status == 1:
        tk.Button(window, text='Create Lesson', command=lesson_create_view.main).grid(row=row)
        row += 1

    tk.Button(window, text='View Lessons', command=lesson_list_view.main).grid(row=row)
    row += 1
    tk.Button(window, text='Quit', command=window.destroy).grid(row=row)
    row += 1
    ui.margin_y(window, px=20, row=row)
    row += 1

    window.mainloop()
