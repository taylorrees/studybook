# Authors: Taylor Rees

import tkinter as tk

padx = 80
font_family = "Arial"

def title(master, text, row):
    """
    Creates a standardised page title for
    a screen within the application.
    The function should be passed the master
    object to which the title is to be bound
    as well as the desired title text.

    @param {Object} master
    @param {string} text
    @param {int} row
    """

    title = tk.Label(master)
    title["text"] = text
    title["font"] = (font_family, 26)
    title.grid(row=row, column=0, padx=padx, sticky=tk.W)
    return title


def pair(master, label_text, button_text, command, row):
    """
    Creates a label, button pair. The label
    should be associated to the button with
    which it has been paired.

    @param {Object} master
    @param {string} label_text
    @param {string} button_text
    @param {function} command
    @param {int} row
    """

    label = tk.Label(master)
    label["text"] = label_text
    label["font"] = (font_family, 14)
    label.grid(row=row, column=0, padx=padx, sticky=tk.W)

    button = tk.Button(master)
    button["text"] = button_text
    button["command"] = command
    button.grid(row=row, column=1, padx=padx, sticky=tk.E)


def margin_y(master, row, px):
    """
    Creates an area of margin with the
    specified dimensions. This is essentially
    whitespace used to decorate the screen.

    @param {Object} master
    @param {int} row
    @param {int} px
    """

    label = tk.Label(master)
    label.grid(row=row, pady=px)
