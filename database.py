import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared


class Database:

	def __init__(self):

		self.Id = mysql.connector.connect(user='root', host='localhost',
	password='100ml80%vol.', port='330')
		self.cursor = self.Id.cursor()

	def create_database(self):
		try:
			self.cursor.execute(
				"create database Purbeurre default character set 'utf8'")
		except mysql.connector.Error as err:
			print("Failed creating database Purbeurre")
			exit(1)

	def create_table(self):
		for table_name in TABLES:
			table_description = TABLES[table_name]
			try:
				print("creating table {}:".format(table_name), end='')
				self.cursor.execute(table_description)
			except mysql.connector.Error as err:
				if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
					print("already exists.")
				else:
					print(err.msg)
			else:
				print("OK")
		self.cursor.close()
		



	def connect_database(self):

		self.Id = mysql.connector.connect(user='root', host='localhost',
	password='100ml80%vol.', port='330')
		self.cursor = self.Id.cursor()
		self.cursor.execute("use Purbeurre")

b = Database()
b.create_database()


