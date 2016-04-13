import tkinter as tk
import templates.ui as ui
import lesson_list.view as lesson_list_view
import lesson_publish.view as lesson_publish_view
import lesson_create.view as lesson_create_view

def main(login_status):

    # Quick and dirty dashboard.
    # Needs work once all views are
    # in place.
    #

    row = 0
    window = tk.Tk()
    window.title('Studybook | Dashboard')
    centered_frame = tk.Frame(window)

    # Interface

    ui.title(centered_frame, text='Dashboard', row=row)
    row += 1
    ui.margin_y(centered_frame, px=10, row=row)
    row += 1

    # If a lecturer is logged in
    # show them the lecturer specific actions
    if login_status == 1:
        tk.Button(centered_frame, text='Create Lesson', command=lesson_create_view.main).grid(row=row)
        row += 1
        tk.Button(centered_frame, text='Publish Lessons', command=lesson_publish_view.main).grid(row=row)
        row += 1

    tk.Button(centered_frame, text='View Lessons', command=lesson_list_view.main).grid(row=row)
    row += 1
    tk.Button(centered_frame, text='Quit', command=window.destroy).grid(row=row)
    row += 1
    ui.margin_y(centered_frame, px=20, row=row)
    row += 1

    centered_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    window.geometry(ui.center(window))
    window.mainloop()
