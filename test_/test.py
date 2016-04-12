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
		self.students = []
		self.results = {}
		self.QI = 0

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


	def add(self, Question):
		"""
		this method adds a question to the test.
		"""
		self.questions.append(Question)
		self.QI += 1

	def remove(self, QID):
		"""
		this method removes the question from the test.
		"""
		del self.questions[QID]
		self.QI -= 1
