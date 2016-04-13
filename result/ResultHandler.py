#Author: Tom Wynne-Owen
import numpy as np

"""
example dictionary:

results_with_id = {'studentID1':43,'studentID2':45,'studentID3':83,'studentID4':12}

these functions require the parameter to be given in this format
"""

def getTestResults(results):
	"""
	Converts a dictionary of test results
	into an anonymous pythonic list of
	the marks

	used in getMeanTestResult
	"""
	l = []
	for student,mark in results:
		l.append(mark)
	return l
	
def getMeanTestResult(results):
	"""
	Returns the mean test results for the given
	test.
	"""
	l = getTestResults(results)
	return np.mean(l)

def getMaxTestResult(results):
	"""
	Returns the highest test score and the
	associated studentID
	"""
	student = max(results,key=results.get)
	return student, results[student]

def getMinTestResult(results):
	"""
	Returns the lowest test score and the
	associated studentID
	"""
	student = min(results,key=results.get)
	return student, results[student]

def getStudentResult(results, studentID):
	"""
	Returns the test result for a given
	test (results) and student (studentID)

	Returns None if the studentID is invalid
	"""
	#check if studentID is valid
	if studentID in results:
		return results[studentID]
	else:
		return None
