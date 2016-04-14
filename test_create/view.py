#Author: Thomas Sweetman

import tkinter as tk
from test.test import Test
from lesson.lesson import Lesson
import shelve

class TestView:

	def __init__(self,root):

		self.root = root

		self._id = ''
		self.description = ''
		self.questions = []
		self.students = []
		self.answer = [0, 0, 0, 0]
		self.QI = 0 

		self.build()

	def save(self, published = False):

		try:
			store = shelve.open('lesson/store')
		except Exception:
			print("no lessons to link")

		lessons = [(lesson._id, lesson.name) for lesson in store.values() if lesson.published]
		store.close()

		self._id2 = self._id.get()
		self.test = Test(self._id2)

		for d, a in self.questions:
			self.test.add(d, a)

		newlist = [seq[0] for seq in lessons]

		if self._id2 in newlist:
			self.element = str(newlist.index(self._id2))
		else:
			print("no lesson to link")
			return

		store = shelve.open('lesson/store')
		self.lesson = store[self._id2]
		store.close()

		self.lesson.test = True
		self.test._id = self._id2

		self.test.store()
		self.lesson.store()
		self.root.destroy()

	def add(self, Test_description):
		"""
		this method adds a question to the test.
		"""
		self.answer2 = [0,0,0,0]
		self.detail2 = 'not writen'
		self.detail2 = self.description.get()
		self.answer2[0] = self.answer[0].get()
		self.answer2[1] = self.answer[1].get()
		self.answer2[2] = self.answer[2].get()
		self.answer2[3] = self.answer[3].get()

		self.questions.append((self.detail2, self.answer2))
		self.QI += 1
		self.detail()
		Test_description.destroy()

	def detail(self):

		Test_description = tk.Frame(self.root)

		#Question description
		descBox = tk.Label(Test_description, text='question ' + str(self.QI + 1) + ':')
		descBox.grid(sticky=tk.W)

		self.description = tk.Text(Test_description, height=2,width=50)
		self.description = tk.Entry(Test_description)
		self.description.grid(sticky=tk.W)

		#answer
		answerBox = tk.Label(Test_description, text='Correct Answer')
		answerBox.grid(sticky=tk.W)
		self.answer[0] = tk.Entry(Test_description)
		self.answer[0].grid(sticky=tk.W)
		altBox = tk.Label(Test_description, text='alternative answers')
		altBox.grid(sticky=tk.W)
		self.answer[1] = tk.Entry(Test_description)
		self.answer[1].grid(sticky=tk.W)
		self.answer[2] = tk.Entry(Test_description)
		self.answer[2].grid(sticky=tk.W)
		self.answer[3] = tk.Entry(Test_description)
		self.answer[3].grid(sticky=tk.W)

		tk.Button(Test_description, text='Publish & Close', command=lambda: self.save(published=True)).grid(padx=40, sticky=tk.W)
		tk.Button(Test_description, text='Save & Close', command=lambda: self.save()).grid(padx=40, sticky=tk.W)
		tk.Button(Test_description, text='add question', command=lambda: self.add( Test_description)).grid(padx=40, sticky=tk.W)
		tk.Button(Test_description, text='Close', command=self.root.destroy).grid(padx=40, sticky=tk.W)
		tk.Label(Test_description).grid()

		Test_description.grid(padx=40, pady=0, sticky=tk.W)

	def build(self):

		title = tk.Label(self.root, text='Create Test', font = ('Arial', 26))
		title.grid(padx=40, pady=40, sticky=tk.W)

		Test_description = tk.Frame(self.root)

		#related lesson id
		tk.Label(Test_description, text='Lesson ID:').grid(sticky=tk.W)
		self._id = tk.Entry(Test_description)
		self._id.grid(sticky=tk.W)

		Test_description.grid(padx=40, pady=0, sticky=tk.W)

		self.detail()

def main():

	window = tk.Tk()
	window.title('Studybook | Create Lesson')
	app = TestView(window)
	window.grid_columnconfigure(0, weight=1)
	window.mainloop()