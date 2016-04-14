#Author: Thomas Sweetman

import shelve

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
		self.results[studentID] = mark

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

		print('store: '+ str(self.questions))
		print('ID: ' + str(self._id))

		try:
			store = shelve.open('test_/store', 'w')
		except Exception:
			store = shelve.open('test_/store', 'n')

		store[self._id] = self
		store.close()