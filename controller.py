from database import Database

class controller:
	def __init__(self, Database):
		self.database = Database
		self.connect = Database.connect_database()
