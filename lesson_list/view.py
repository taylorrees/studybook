# Author: Taylor Rees

import tkinter as tk
import templates.ui as ui
import lesson.view as lesson_view
import shelve

def main():
    """
    Display the take lesson view.
    This view displays a list of
    published lessons.

    @return {void}
    """

    row = 0
    window = tk.Tk()
    window.title("Studybook | Lesson List")

    # Storage

    store = shelve.open('lesson/store')
    # Store a list of published lesson (id, name)
    # attributes in a tuple in the order above.
    #
    lessons = [(lesson._id, lesson.name) for lesson in store.values() if lesson.published]
    store.close()

    # Interface

    ui.margin_y(window, px=20, row=row)
    row += 1

    ui.title(window, text="Lesson List", row=row)
    row += 1

    ui.margin_y(window, px=2, row=row)
    row += 1

    for lesson in lessons:
        # Loop through all lesson _ids and names
        # generating the appropriate label and button
        # pair to display.
        #
        _id     = lesson[0]
        name    = lesson[1]
        command = lambda _id = _id : lesson_view.main(_id)

        ui.pair(window, label_text=name, button_text="Take Lesson", command=command, row=row)
        row += 1

    ui.pair(window, label_text='', button_text="Close", command=window.destroy, row=row)
    row += 1
    ui.margin_y(window, px=30, row=row)
    window.mainloop()
