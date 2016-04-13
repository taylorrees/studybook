# Author: Taylor Rees

import tkinter as tk
import templates.ui as ui

class Table:


    def __init__(self, title, data):
        """
        A class to generate a simple table made up
        of cells. The number of cells depends on the
        list passed in as the data param. The table will
        be generated in a new window.

        The data param should be a list of lists.
        Such that each list is considered a row
        and each subsequent item within that list
        is considered a field.

        _____________________________________________

        i.e.

        [['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C']]

        Would be interpreted as:

        A       B       C
        A       B       C
        A       B       C

        _____________________________________________

        The title param will set the window title
        and generate a page title with the specified
        value.

        _____________________________________________

        Example usage

        data = [['A', 'B', 'C'], ['A', 'B', 'C'], ['A', 'B', 'C']]
        Table('Student Results', data)
        _____________________________________________


        @param {string} title
        @param {list of lists} data
        @return {void}
        """

        self.data = data
        self.title = title

        window = tk.Tk()
        window.title(self.title)
        centered_frame = tk.Frame(window)
        row = 0

        ui.margin_y(window, px=20, row=row)
        row += 1
        ui.title(window, text=self.title, row=row)
        row += 1
        ui.margin_y(window, px=10, row=row)
        row += 1

        for y, row_ in enumerate(self.data):
            for x, cell in enumerate(row_):
                field = tk.Entry(centered_frame)
                field.insert(0, cell)
                field.configure(state='readonly')
                field.grid(row=row + y, column=x)

        centered_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        window.geometry(ui.center(window))
        window.mainloop()
