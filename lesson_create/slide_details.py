# Author: Taylor Rees

import tkinter as tk

class SlideDetails:
    """
    This class is responsible for
    displaying the slide details section
    in the create lesson form. It handles
    actions that relate specifically to the
    creation of lesson slides.
    """

    def __init__(self, root, lesson):
        """
        Slide Details Frame
        Contains slide title entry field
        and slide body entry field.

        Made up of two frames.

         -------------------
        |  ---------------  |
        | | title         | |
        | | body          | |
        | |           add | |
        |  ---------------  |
         -------------------

        Important: Requires grid layout.

        @param {tkinter object} root
        @param {lesson object} lesson

        """
        self.root = root
        self.slides = []

        # Interface elements
        self.outer_frame = tk.Frame(self.root, bd=1, relief=tk.SOLID)
        self.inner_frame = tk.Frame(self.outer_frame)
        self.title = tk.Entry(self.inner_frame)
        self.body = tk.Text(self.inner_frame, height=16, width=50, bd=1, relief=tk.SOLID, wrap='word')
        self.add_button = tk.Button(self.inner_frame, text='Add Slide', command=self.add)

        # Build interface
        self.build()


    def clear(self):
        """
        Clear all form fields.

        @return {void}
        """

        self.title.delete(0, 'end')
        self.body.delete('1.0', 'end')


    def add(self):
        """
        Add slide details to slides array
        then clear the slide title and slide
        body fild within the slide details
        frame.

        @return {void}
        """

        self.slides.append({'_id': self.title.get(), 'name': self.body.get('1.0', tk.END)})
        self.clear()


    def get(self):
        """
        Return a list of dictionaries
        containing _id, name pairs from the
        slides created by the user.

        @return {list}
        """

        return self.slides


    def buttons(self):
        # add slide button
        self.add_button.grid(sticky=tk.E)


    def build(self):
        """
        Builds the tkinter based interface
        for the slide details section of the
        create lesson window.

        @return {void}
        """

        # slide title
        tk.Label(self.inner_frame, text='Title').grid(sticky=tk.W)
        self.title.grid(sticky=tk.W)

        # slide body
        tk.Label(self.inner_frame, text='Body').grid(sticky=tk.W)
        self.body.grid(sticky=tk.W)

        self.buttons()

        # bind to grid
        self.inner_frame.grid(padx=20, pady=20)
        self.outer_frame.grid(padx=40, pady=40, sticky=tk.W)
