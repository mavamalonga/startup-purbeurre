import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

import recover_data_api

class Database:

	def __init__(self):

		self.Id = mysql.connector.connect(user='root', host='localhost',
	password='100ml80%vol.', port='330', database='person')
		self.cursor = self.Id.cursor()

	def create_database(self):

		with open("base_ap.sql", "r") as f:
			base = f.read()
			self.cursor.execute(base)

	def connect_database(self):

		self.Id = mysql.connector.connect(user='root', host='localhost',
	password='100ml80%vol.', port='330', database='person')
		self.cursor = self.Id.cursor()
		self.cursor.execute("use Purbeurre")

	
