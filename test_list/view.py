# Author: Thomas Sweetman

import tkinter as tk
import templates.ui as ui
import test_.view as test_view
import shelve

def main():

    row = 0
    window = tk.Tk()
    window.title("Studybook | Test List")

    store = shelve.open('lesson/store')
    lessons = [(lesson._id, lesson.name) for lesson in store.values() if lesson.published]
    store.close()

    ui.margin_y(window, px=20, row=row)
    row += 1

    ui.title(window, text="Test List", row=row)
    row += 1

    ui.margin_y(window, px=2, row=row)
    row += 1

    for lesson in lessons:

    	store = shelve.open('lesson/store')
    	temp = store[lesson[0]]
    	store.close()

    	_id     = lesson[0]
    	name    = lesson[1]
    	command = lambda _id = _id : test_view.main(_id)

    	ui.pair(window, label_text=name, button_text="Take Test", command=command, row=row)
    	row += 1

    ui.pair(window, label_text='', button_text="Close", command=window.destroy, row=row)
    row += 1
    ui.margin_y(window, px=30, row=row)
    window.mainloop()
