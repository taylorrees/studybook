#Author: Thomas Sweetman

import shelve
import tkinter as tk
import templates.ui as ui

class TestView:

	def __init__(self, root, test, lesson):
		self.root = root
		self.lesson = lesson
		self.test = test
		self.current_question = -1

		self.title = ui.title(self.root, text=lesson.name, row=1)
		self.body = tk.Label(self.root, text='Click next to start the test')
		self.previous_button = tk.Button(self.root, text="Previous Question", command=self.previous)
		self.next_button = tk.Button(self.root, text="Next Question", command=self.next)
		self.complete_button = tk.Button(self.root, text="Submit Test", command=self.complete)

		self.build()

	def previous(self):

		if self.current_question -1 > -1:
			self.current_question -= 1

		question = self.test.questions[self.current_question]
		self.title.destroy()
		self.body.destroy()

		self.detail = tk.Label(self.root, text=question.detail,row=1)
		self.answer1 = tk.Radiobutton(self.root, text=question.answers[0],column=2,row=4)
		self.answer2 = tk.Radiobutton(self.root, text=question.answers[1],column=2,row=8)
		self.answer3 = tk.Radiobutton(self.root, text=question.answers[2],column=6,row=4)
		self.answer4 = tk.Radiobutton(self.root, text=question.answers[3],column=6,row=8)

		self.build()

	def next(self):

		if self.current_question +1 < len(self.test.questions):
			self.current_question += 1

		question = self.test.questions[self.current_question]
		self.title.destroy()
		self.body.destroy()

		self.detail = tk.Label(self.root, text=question.detail,row=1)
		self.answer1 = tk.Radiobutton(self.root, text=question.answers[0],column=2,row=4)
		self.answer2 = tk.Radiobutton(self.root, text=question.answers[1],column=2,row=8)
		self.answer3 = tk.Radiobutton(self.root, text=question.answers[2],column=6,row=4)
		self.answer4 = tk.Radiobutton(self.root, text=question.answers[3],column=6,row=8)

		self.build()

	def complete(self):

		self.root.destroy()

	def make_title(self):

		ui.margin_y(self.root, px=20, row=0)
		self.title
		ui.margin_y(self.root, px=2, row=2)

	def make_body(self):

		self.body.grid(row=3)

	def make_nav(self):

		padx=20
		ui.margin_y(self.root, px=20, row=4)

		if self.current_question > 0:
			self.previous_button.grid(sticky=tk.W, row=5, padx=padx)
		else:
			self.previous_button.grid_forget()

		self.next_button.grid(sticky=tk.E, row =5, padx=padx)

		if self.current_question == (len(self.test.questions) - 1):
			self.next_button.grid_forget()
			self.complete_button.grid(sticky=tk.E, row=5, padx=padx)
		else:
			self.complete_button.grid_forget()
			self.next_button(sticky=tk.E, row=5, padx=padx)

		ui.margin_y(self.root,px=0,row=8)

	def build(self):

		self.make_title()
		self.make_body()
		self.make_nav()


def main(_id):

	store = shelve.open('lesson/store')
	lesson = store[_id]
	store.close()

	test = lesson.test

	window = tk.Tk()
	window.title("Studybook | Test Viewer")
	app = TestView(window, test, lesson)
	window.mainloop()