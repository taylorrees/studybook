#Author: Thomas Sweetman

import shelve
import tkinter as tk
import templates.ui as ui
from templates.message import Message

class TestView:

	def __init__(self, window, root, test, lesson, student_id):
		self.window = window
		self.root = root
		self.lesson = lesson
		self.Student = student_id
		self.test = test
		self.current_question = 0
		self.answer = []

		for q in self.test.questions:
			self.answer.append('')

		self.build()

	def next(self, Test):
		self.answer[self.current_question] = self.entry.get()

		if self.current_question < len(self.test.questions) -1:
			self.current_question += 1
		Test.destroy()
		self.build()

	def previous(self, Test):
		self.answer[self.current_question] = self.entry.get()

		if self.current_question > 0:
			self.current_question -= 1
		Test.destroy()
		self.build()
		
	def complete(self):
		self.answer[self.current_question] = self.entry.get()

		mark = 0
		for a in self.answer:
			if a == '1':
				mark += 1

		self.test.setResult(self.Student, mark)
		self.window.destroy()
		Message('Final mark: ' + str(mark) + '/' + str(len(self.answer)) + ' (' + str( (mark/len(self.answer)) * 100 ) + '%)')

	def detail(self):
		Test = tk.Frame(self.root)

		ui.margin_y(Test, px=20, row=0)
		ui.title(Test, text="Take Test", row=1)
		ui.margin_y(Test, px=2, row=2)

		previous_command = lambda test = Test : self.previous(test)
		next_command = lambda test = Test : self.next(test)
		complete_command = lambda test = Test : self.complete(self.root)

		self.previous_button = tk.Button(Test, text="Previous Question", command=previous_command)
		self.next_button = tk.Button(Test, text="Next Question", command=next_command)
		self.complete_button = tk.Button(Test, text="Submit Test", command=self.complete)

		padx = 20

		question = self.test.questions[self.current_question]
		self.body = tk.Label(Test, text=question[0]).grid(row=3)

		ui.margin_y(self.root, px=20, row=4)

		self.body = tk.Label(Test, text="1. " + question[1][0]).grid(row=5)
		self.body = tk.Label(Test, text="2. " + question[1][1]).grid(row=6)
		self.body = tk.Label(Test, text="3. " + question[1][2]).grid(row=7)
		self.body = tk.Label(Test, text="4. " + question[1][3]).grid(row=8)

		self.entry = tk.Entry(Test)
		self.entry.grid(row=9)
		self.entry.insert(0, self.answer[self.current_question])

		"""
		if self.current_question > 0:
			self.previous_button.grid(sticky=tk.W, row=9, padx=padx)

		if self.current_question == len(self.test.questions) -1:
			self.next_button.grid(sticky=tk.E, row=10, padx=padx)
			self.complete_button.grid_forget()
		else:
			self.complete_button.grid(sticky=tk.W, row=11, padx=padx)
			self.next_button.grid_forget()
		"""

		ui.margin_y(self.root, px=0, row=9)

		Test.grid()

	def make_nav(self):

	   	padx = 20

	   	if self.current_question > 0:
	   		self.previous_button.grid(sticky=tk.W, row=11, padx=padx)
	   	else:
	   		self.previous_button.grid_forget()

	   	self.next_button.grid(sticky=tk.E, row=11, padx=padx)

	   	if self.current_question == (len(self.test.questions) - 1):
	   		self.next_button.grid_forget()
	   		self.complete_button.grid(sticky=tk.E, row=11, padx=padx)
	   	else:
	   		self.complete_button.grid_forget()
	   		self.next_button.grid(sticky=tk.E, row=11, padx=padx)

	   	ui.margin_y(self.root, px=0, row=12)

	def build(self):

		self.detail()
		self.make_nav()

def main(_id, user_id):

	store = shelve.open('lesson/store')
	lesson = store[_id]
	store.close()

	store = shelve.open('test/store')
	test = store[_id]
	store.close()

	window = tk.Tk()
	window.title("Studybook | Test Viewer")
	centered_frame = tk.Frame(window)

	app = TestView(window, centered_frame, test, lesson, user_id)

	centered_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
	window.geometry(ui.center(window))
	window.mainloop()