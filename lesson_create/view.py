# Author: Taylor Rees

import tkinter as tk
from lesson.lesson import Lesson
from lesson_create.slide_details import SlideDetails

class LessonCreate:
    """
    This class is responsible for providing
    a GUI through which a user can create a
    lesson.
    """

    def __init__(self, root):
        """
        Construct create lesson window.

        @param {tkinter object} root
        @return {void}
        """

        self.root = root

        # Interface elements
        self._id = ''
        self.name = ''
        self.slide_details = ''
        self.lesson = Lesson(self._id, self.name)
        self.slides = []

        # Build interface
        self.build()


    def save(self, published = False):
        """
        Save the lesson object to the lesson
        store once populated with the
        users data.

        @return {void}
        """

        slides = self.slide_details.get()

        # Set the lesson _id using
        # the id provided by the user
        #
        self.lesson._id = self._id.get()

        # Set the lesson name using
        # the id provided by the user
        #
        self.lesson.name = self.name.get()

        # Set the lesson published attribute
        # using the id provided by the user
        #
        self.lesson.published = published

        # Add the lesson slides to
        # the lesson object from the
        # slide details section of the form
        #
        for slide in slides:
            self.lesson.add(slide['_id'], slide['name'], slide['image'])

        # Store the lesson object in the
        # persistent lesson store
        #
        self.lesson.store()
        self.root.destroy()


    def build(self):
        """
        Builds the tkinter based interface
        for the create lesson window.

        @return {void}
        """

        title = tk.Label(self.root, text='Create Lesson', font=('Arial', 26))
        title.grid(padx=40, pady=40, sticky=tk.W)

        # Lesson Details Frame
        # Contains lesson id entry field and
        # lesson name entry field.
        #
        lesson_details_frame = tk.Frame(self.root)

        # lesson id
        tk.Label(lesson_details_frame, text='Lesson ID').grid(sticky=tk.W)
        self._id = tk.Entry(lesson_details_frame)
        self._id.grid(sticky=tk.W)

        # lesson name
        tk.Label(lesson_details_frame, text='Lesson Name').grid(sticky=tk.W)
        self.name = tk.Entry(lesson_details_frame)
        self.name.grid(sticky=tk.W)

        lesson_details_frame.grid(padx=40, pady=0, sticky=tk.W)

        # slide details
        self.slide_details = SlideDetails(self.root, self.lesson)

        # buttons
        tk.Button(self.root, text='Publish & Close', command=lambda: self.save(published=True)).grid(padx=40, sticky=tk.W)
        tk.Button(self.root, text='Save & Close', command=lambda: self.save()).grid(padx=40, sticky=tk.W)
        tk.Button(self.root, text='Close', command=self.root.destroy).grid(padx=40, sticky=tk.W)
        tk.Label(self.root).grid()


def main():
    """
    Create the window and generate
    the interface.

    @return {void}
    """

    window = tk.Tk()
    window.title('Studybook | Create Lesson')
    app = LessonCreate(window)
    window.grid_columnconfigure(0, weight=1)
    window.mainloop()
