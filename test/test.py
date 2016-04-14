#Author: Thomas Sweetman

import shelve
import csv

class Test:
	"""
	This class manages the creation, monitoring
	and usage of Test, a Test consists of Questions
	in multiple choice or other question class.
	"""

	def __init__(self, testID):
		self._id = testID
		self.questions = []
		self.results = {}
		self.resultcsv = 'results/' + testID + '.csv'

	def getStatus(self, studentID):
		"""
		this method returns true if the student
		has completed the test.
		"""
		if studentID in self.students:
			return True
		else:
			return False

	def setResult(self, studentID, mark):
		"""
		this method sets the result of a completed
		test.
		"""
		print(self.results)
		self.results[studentID] = mark
		self.store()
		with open(self.resultcsv, 'w', newline = '') as csvfile:
			writer = csv.writer(csvfile, delimiter=',')
			for _id in self.results.keys():
				writer.writerow([_id, self.results[_id]])
		csvfile.close()




	def getResult(self, studentID):
		"""
		this method returns the result of a previously
		completed test.
		"""
		return self.results[studentID]

	def takeTest(self):
		"""
		this method presents the user with the test
		to be taken.
		"""


	def add(self, detail, answers):
		"""
		this method adds a question to the test.
		"""
		self.questions.append((detail, answers))

	def store(self):

		try:
			store = shelve.open('test/store', 'w')
		except Exception:
			store = shelve.open('test/store', 'n')

		store[self._id] = self
		store.close()