# Author: Taylor Rees

import tkinter as tk

class Message:

    def __init__(self, text):
        """
        Create and display a message box. The message
        box will have the value of the text param.

        @param {string} text
        @return {void}
        """

        self.text = text

        window = tk.Tk()
        window.title('Message')

        frame = tk.Frame(window)
        tk.Label(frame, text=self.text).pack(pady=5)
        tk.Button(frame, text="OK", command=window.destroy).pack(pady=5)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        w = 200
        h = 100
        # Find screen width and height
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        # Calculate x and y coordinates for the Tk window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        window.mainloop()
