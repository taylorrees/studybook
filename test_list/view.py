# Author: Thomas Sweetman

import tkinter as tk
import templates.ui as ui
import test.view as test_view
import shelve

def main(user_id):

    row = 0
    window = tk.Tk()
    window.title("Studybook | Test List")
    centered_frame = tk.Frame(window)

    store = shelve.open('lesson/store')
    lessons = [(lesson._id, lesson.name) for lesson in store.values() if lesson.published]
    store.close()

    ui.margin_y(centered_frame, px=20, row=row)
    row += 1

    ui.title(centered_frame, text="Test List", row=row)
    row += 1

    ui.margin_y(centered_frame, px=2, row=row)
    row += 1

    for lesson in lessons:

        store = shelve.open('test/store')
        test = store[lesson[0]]
        store.close()

        _id     = lesson[0]
        name    = lesson[1]
        command = lambda _id = _id : test_view.main(_id, user_id)

        if user_id not in test.results.keys():
            ui.pair(centered_frame, label_text=name, button_text="Take Test", command=command, row=row)
            row += 1

    ui.pair(centered_frame, label_text='', button_text="Close", command=window.destroy, row=row)
    row += 1
    ui.margin_y(centered_frame, px=30, row=row)

    centered_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    window.geometry(ui.center(window))
    window.mainloop()
