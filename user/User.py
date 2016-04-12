class User:

	def __init__(self, user_id, password, login_status = 0):
		"""
		Constructor
		This class is responsible for creating a user class
		which will in turn allow the user to login to the
		system. Using the login_status the user will be
		granted access to specific parts of the system with
		the appropriate access levels.

		login_status == 0 == logged out
		login_status == 1 == lecturer
		login_status == 2 == student

		"""

		self.user_id = user_id
		self.password = password
		self.login_status = login_status


	def login(self, user_id, password):
		"""
		Login method
		Allow a user to login to the system provided
		their login credentials are correct. Give the
		user the appropriate access permissions.

		*										*
		* LOGIN DETAILS HARD CODED TO PROTOTYPE *
		*										*
		"""

		if (user_id == "lecturer" and password == "password"):
			login_status = 1
			return login_status

		elif (user_id == "student" and password == "password"):
			login_status = 2
			return login_status


	def logout(self):
		"""
		Logout method
		Set the users login status to the deafult value
		of zero, thus removing all access rights from the
		system.
		"""

		login_status = 0
		return login_status
