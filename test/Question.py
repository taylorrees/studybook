#Author: Thomas Sweetman

class Question:
	"""
	this class is consists of a 
	question to be answered in a test.
	"""

	def __init__(self,_id, detail, answers):
		self._id = _id
		self.detail = detail
		self.answers = answers

	def get(self):
		"""
		returns the question
		"""

