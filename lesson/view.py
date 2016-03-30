import tkinter as tk
import templates.ui as ui
import shelve

class LessonView:
    def __init__(self, root, lesson):
        self.root = root
        self.lesson = lesson
        self.current_slide_index = -1
        # Interface
        self.title = ui.title(self.root, text=lesson.name, row=1)
        self.body = tk.Label(self.root, text='Click next to begin.')
        self.previous_button = tk.Button(self.root, text="Previous Slide", command=self.previous)
        self.next_button = tk.Button(self.root, text="Next Slide", command=self.next)
        self.complete_button = tk.Button(self.root, text="Finish Lesson", command=self.complete)

        self.build()

    # Actions

    def previous(self):
        if self.current_slide_index - 1 > -1:
            self.current_slide_index -= 1
        slide = self.lesson.slides[self.current_slide_index]
        self.title.destroy()
        self.body.destroy()
        self.title = ui.title(self.root, text=slide.title, row=1)
        self.body = tk.Label(self.root, text=slide.body)
        self.build()


    def next(self):
        if self.current_slide_index + 1 < len(self.lesson.slides):
            self.current_slide_index += 1
        slide = self.lesson.slides[self.current_slide_index]
        self.title.destroy()
        self.body.destroy()
        self.title = ui.title(self.root, text=slide.title, row=1)
        self.body = tk.Label(self.root, text=slide.body)
        self.build()


    def complete(self):
        # Set lesson status
        self.root.destroy()


    # Title

    def make_title(self):
        ui.margin_y(self.root, px=20, row=0)
        self.title
        ui.margin_y(self.root, px=2, row=2)


    # Body

    def make_body(self):
        self.body.grid(row=3)


    # Navigation

    def make_nav(self):
        """
        Create a lesson navigation bar in
        the view lesson window. The navigation
        bar contains a previous, next and finish
        lesson button.
        """
        padx = 20
        ui.margin_y(self.root, px=20, row=4)

        # If the user is not on the first slide
        # show the previous slide button.
        #
        if self.current_slide_index > 0:
            self.previous_button.grid(sticky=tk.W, row=5, padx=padx)
        else:
            self.previous_button.grid_forget()

        # Next slide button
        #
        self.next_button.grid(sticky=tk.E, row=5, padx=padx)

        # If the user is on the last slide
        # forget the next button and replace
        # with the finish lesson button.
        #
        if self.current_slide_index == (len(self.lesson.slides) - 1):
            self.next_button.grid_forget()
            self.complete_button.grid(sticky=tk.E, row=5, padx=padx)
        else:
            self.complete_button.grid_forget()
            self.next_button.grid(sticky=tk.E, row=5, padx=padx)

        ui.margin_y(self.root, px=0, row=8)


    def build(self):
        self.make_title()
        self.make_body()
        self.make_nav()


def main(_id):
    # Storage
    store = shelve.open('lesson/store')
    lesson = store[_id]
    store.close()

    window = tk.Tk()
    window.title("Studybook | Lesson Viewer")
    app = LessonView(window, lesson)
    window.mainloop()
