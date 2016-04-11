class User:
	
	loginStatus = False
	
	def __init__(self, userID, password, loginStatus = False):
		self.userID = userID
		self.password = password
		self.loginStatus = loginStatus

	def login(userID, password):
		#values are hardcoded for prototyping

		#lecturer user
		if (userID == "lecturer" and password=="password"):
			loginStatus = True
			return loginStatus
		elif (userID == "student" and password=="password"):
			loginStatus = True
			return loginStatus

	def logout():
		loginStatus = False
		return