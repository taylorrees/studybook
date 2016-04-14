# Author: Thomas Sweetman

import tkinter as tk
import templates.ui as ui
import result.view as result_view
import shelve

def main():

    row = 0
    window = tk.Tk()
    window.title("Studybook | Results List")
    centered_frame = tk.Frame(window)

    store = shelve.open('lesson/store')
    lessons = [(lesson._id, lesson.name) for lesson in store.values() if lesson.published]
    store.close()

    ui.margin_y(centered_frame, px=20, row=row)
    row += 1

    ui.title(centered_frame, text="Results List", row=row)
    row += 1

    ui.margin_y(centered_frame, px=2, row=row)
    row += 1

    for lesson in lessons:

        store = shelve.open('test/store')
        test = store[lesson[0]]
        store.close()

        _id     = lesson[0]
        name    = lesson[1]
        command = lambda _id = _id : result_view.main(_id, name)

        ui.pair(centered_frame, label_text=name, button_text="View Results", command=command, row=row)
        row += 1

    ui.pair(centered_frame, label_text='', button_text="Close", command=window.destroy, row=row)
    row += 1
    ui.margin_y(centered_frame, px=30, row=row)

    centered_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    window.geometry(ui.center(window))
    window.mainloop()
