#Author: Thomas Sweetman

import shelve
import tkinter as tk
import templates.ui as ui

class TestView:

	def __init__(self, root, test, lesson):#student_id in here too
		self.root = root
		self.lesson = lesson
		#self.Student = student_id
		self.test = test
		self.current_question = 0
		self.answer = []

		for q in self.test.questions:
			self.answer.append(0)

		self.build()

	def next(self, Test):
		if self.current_question < len(self.test.questions) -1:
			self.current_question += 1
		Test.destroy()
		self.build()

	def previous(self, Test):
		if self.current_question > 0:
			self.current_question -= 1
		Test.destroy()
		self.build()
		
	def complete(self, Test):
		#mark = 0
		#for a in self.answer:
		#	if a == 1:
		#		mark += 1

		#self.test.setResult(self.Student, mark)
		self.root.destroy()

	def detail(self):
		Test = tk.Frame(self.root)

		ui.margin_y(Test, px=20, row=0)
		ui.title(Test, text="Take Test", row=1)
		ui.margin_y(Test, px=2, row=2)

		previous_command = lambda test = Test : self.previous(test)
		next_command = lambda test = Test : self.next(test)
		complete_command = lambda test = Test : self.complete(test)

		self.previous_button = tk.Button(Test, text="Previous Question", command=previous_command)
		self.next_button = tk.Button(Test, text="Next Question", command=next_command)
		self.complete_button = tk.Button(Test, text="Submit Test", command=complete_command)

		padx = 20

		question = self.test.questions[self.current_question]
		self.body = tk.Label(Test, text=question[0]).grid(row=3)

		ui.margin_y(self.root, px=20, row=4)

		self.body = tk.Radiobutton(Test, text=question[1][0], variable=self.answer[self.current_question], value = 1).grid(row=5)
		self.body = tk.Radiobutton(Test, text=question[1][1], variable=self.answer[self.current_question], value = 2).grid(row=6)
		self.body = tk.Radiobutton(Test, text=question[1][2], variable=self.answer[self.current_question], value = 3).grid(row=7)
		self.body = tk.Radiobutton(Test, text=question[1][3], variable=self.answer[self.current_question], value = 4).grid(row=8)
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

		Test.place(relx=0.5, rely=0.5, anchor='center')

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