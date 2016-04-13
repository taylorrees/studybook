# Author: Tom Wynne-Owen
import csv

class User:

	def __init__(self):
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

		self.login_status = 0
		self.user_id = ''


	def login(self, user_id, password):
		"""
		Login method
		Allow a user to login to the system provided
		their login credentials are correct. Give the
		user the appropriate access permissions.
		"""

		with open('users.csv') as csvfile:
			rdr = csv.reader(csvfile)
			for row in rdr:
				if (user_id == row[0] and password == row[1]):
					self.user_id = user_id
					self.login_status = int(row[2])
		csvfile.close()



	def logout(self):
		"""
		Logout method
		Set the users login status to the deafult value
		of zero, thus removing all access rights from the
		system.
		"""

		login_status = 0
		return login_status

	def add_user(self, user_id, password, permission=2):
		"""
		Add student method.
		Allows a lecturer to add a student user to the
		system.

		Permission is login_status (1:lecturer, 2:student)

		Returns True if user has been sucessfully added.
		Returns False if user already exists.
		Returns False if login_status is not 1 (lecturer).
		"""

		#check if login_status allows permission
		if (self.login_status == 1):
			#read and check if user_id exists
			with open('users.csv', 'r') as csvfile:
				rdr = csv.reader(csvfile)
				for row in rdr:
					if (user_id == row[0]):
						#user_id exists in the file so return false
						return False
			csvfile.close()

			#add user_id, password and permission status to file
			with open('users.csv', 'w', newline='') as csvfile:
				new_user = [user_id, password, permission]
				writer = csv.writer(csvfile, delimiter=',')
				csvfile.writerows(new_user)
			csvfile.close()
			return True
		else:
			return False

