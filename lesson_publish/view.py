# Author: Taylor Rees

import tkinter as tk
import templates.ui as ui
import lesson.view as lesson_view
import shelve


def publish(_id):
    """
    Open a requested lesson from the lesson store
    and changed its state from unpublished to
    published. Write these changes back to the
    datastore.

    @param {string} _id
    @return {void}
    """

    store = shelve.open('lesson/store')

    for lesson in store.values():
        if lesson._id == _id:
            lesson.publish()
            store[_id] = lesson

    store.close()


def main():
    """
    Display the take lesson view.
    This view displays a list of
    published lessons.

    @return {void}
    """

    row = 0
    window = tk.Tk()
    window.title("Studybook | Unpublished Lesson List")
    centered_frame = tk.Frame(window)

    # Storage

    store = shelve.open('lesson/store')
    # Store a list of published lesson (id, name)
    # attributes in a tuple in the order above.
    #
    lessons = [(lesson._id, lesson.name) for lesson in store.values() if not lesson.published]
    store.close()

    # Interface

    ui.margin_y(centered_frame, px=20, row=row)
    row += 1

    ui.title(centered_frame, text="Unpublished Lesson List", row=row)
    row += 1

    ui.margin_y(centered_frame, px=2, row=row)
    row += 1

    for lesson in lessons:
        # Loop through all lesson _ids and names
        # generating the appropriate label and button
        # pair to display.
        #
        _id     = lesson[0]
        name    = lesson[1]
        command = lambda _id = _id : publish(_id)

        ui.pair(centered_frame, label_text=name, button_text="Publish Lesson", command=command, row=row)
        row += 1

    ui.pair(centered_frame, label_text='', button_text="Close", command=window.destroy, row=row)
    row += 1
    ui.margin_y(centered_frame, px=30, row=row)

    centered_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    window.geometry(ui.center(window))
    window.mainloop()
