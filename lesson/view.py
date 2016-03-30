import tkinter as tk
import templates.ui as ui
import shelve

class LessonView:
    def __init__(self, root, lesson):
        self.root = root
        self.lesson = lesson
        self.current_slide_index = -1

        # Interface elements
        self.title = ui.title(self.root, text=lesson.name, row=1)
        self.body = tk.Label(self.root, text='Click next to begin.')
        self.previous_button = tk.Button(self.root, text="Previous Slide", command=self.previous)
        self.next_button = tk.Button(self.root, text="Next Slide", command=self.next)
        self.complete_button = tk.Button(self.root, text="Finish Lesson", command=self.complete)

        self.build()

    # Actions

    def previous(self):
        """
        A method to change the slide
        content from its current state to
        its previous state.

        @return {void}
        """
        if self.current_slide_index - 1 > -1:
            # decrement slide index
            self.current_slide_index -= 1

        # load previous slide
        slide = self.lesson.slides[self.current_slide_index]
        # remove current slide title & body
        self.title.destroy()
        self.body.destroy()
        # set new title & body
        self.title = ui.title(self.root, text=slide.title, row=1)
        self.body = tk.Label(self.root, text=slide.body)
        # rebuild interface
        self.build()


    def next(self):
        """
        A method to change the slide
        content from its current state to
        its next state.

        @return {void}
        """

        if self.current_slide_index + 1 < len(self.lesson.slides):
            # increment slide index
            self.current_slide_index += 1

        # load next slide
        slide = self.lesson.slides[self.current_slide_index]
        # remove current slide title & body
        self.title.destroy()
        self.body.destroy()
        # set new title & body
        self.title = ui.title(self.root, text=slide.title, row=1)
        self.body = tk.Label(self.root, text=slide.body)
        # rebuild interface
        self.build()


    def complete(self):
        """
        Once the lesson has been completed
        the lesson status object relating to
        the student and that lesson is set
        to viewed. The window then closes.

        @return {void}
        """

        #### SET LESSON STATUS HERE ####
        self.root.destroy()


    # Title

    def make_title(self):
        """
        Add page title to interface.

        @return {void}
        """
        ui.margin_y(self.root, px=20, row=0)
        self.title
        ui.margin_y(self.root, px=2, row=2)


    # Body

    def make_body(self):
        """
        Add body to interface.

        @return {void}
        """
        self.body.grid(row=3)


    # Navigation

    def make_nav(self):
        """
        Create a lesson navigation bar in
        the view lesson window. The navigation
        bar contains a previous, next and finish
        lesson button.

        @return {void}
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
        """
        Build the page.

        @return {void}
        """
        self.make_title()
        self.make_body()
        self.make_nav()


def main(_id):
    """
    Display the lesson view interface
    and populate with the required data.

    @param {string} _id
    @return {void}
    """
    # Storage
    store = shelve.open('lesson/store')
    lesson = store[_id]
    store.close()

    window = tk.Tk()
    window.title("Studybook | Lesson Viewer")
    app = LessonView(window, lesson)
    window.mainloop()
