import numpy as np

"""
example dictionary:

results_with_id = {'studentID1':43,'studentID2':45,'studentID3':83,'studentID4':12}

these functions require the parameter to be given in this format
"""


def getMeanTestResult(results):
	l = getTestResults(results)
	return np.mean(l)

#returns the highest test score and associated studentID
def getMaxTestResult(results):
	student = max(results,key=results.get)
	return student, results[student]


#returns the lowest test score and associated studentID
def getMinTestResult(results):
	student = min(results,key=results.get)
	return student, results[student]

#returns test result for one student, given the studentID
#returns none if studentID is invalid
def getStudentResult(results, studentID):
	#check if studentIDstu is valid
	if studentID in results:
		return results[studentID]
	else:
		return None


#returns an anonymous list of test results
def getTestResults(results):
	l = []
	for student,mark in results:
		l.append(mark)
	return l


