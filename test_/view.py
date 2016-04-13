#Author: Thomas Sweetman

import shelve
import tkinter as tk
import templates.ui as ui

class TestView:

	def __init__(self, root, test, lesson):
		self.root = root
		self.lesson = lesson
		self.test = test
		self.current_question = 0
		self.answer = []

		for q in self.test.questions:
			self.answer.append(0)

		self.title = ui.title(self.root, text=lesson.name, row=1)
		self.body = tk.Label(self.root, text='Click next to start the test')
		self.previous_button = tk.Button(self.root, text="Previous Question", command=self.previous)
		self.next_button = tk.Button(self.root, text="Next Question", command=self.next)
		self.complete_button = tk.Button(self.root, text="Submit Test", command=self.complete)

		self.build()

	def detail(self):
		Test = tk.Frame(self.root)

		self.answer[current_question]
		self.body = tk.Label(Test, text=question[0]).grid(row=1)
		self.body = tk.Radiobutton(Test, text=question[1][0]).grid(row=3, column=0)
		self.body = tk.Radiobutton(Test, text=question[1][1]).grid(row=5, column=0)
		self.body = tk.Radiobutton(Test, text=question[1][2]).grid(row=3, column=2)
		self.body = tk.Radiobutton(Test, text=question[1][3]).grid(row=5, column=2)

	def build(self):

		self.detail()

def main(_id):

	print(_id)
	store = shelve.open('lesson/store')
	lesson = store[_id]
	store.close()

	store = shelve.open('test_/store')
	test = store[_id]
	store.close()

	window = tk.Tk()
	window.title("Studybook | Test Viewer")
	app = TestView(window, test, lesson)
	window.mainloop()