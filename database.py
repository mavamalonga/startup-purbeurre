import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
import tables
import tkinter as tk
import controller

class Database:

	def __init__(self, table, controller):
		self.controller = controller
		self.table = table
		self.Id = mysql.connector.connect(user='root', host='localhost', password='100ml80%vol.', port='330')
		self.cursor = self.Id.cursor()

	def create_database(self):
		try:
			self.cursor.execute("create database Purbeurre default character set 'utf8'")
		except mysql.connector.Error as err:
			print("Failed creating database Purbeurre")
			exit(1)

	def connect_database(self):

		self.Id = mysql.connector.connect(user='root', host='localhost', password='100ml80%vol.', port='330')
		self.cursor = self.Id.cursor()
		self.cursor.execute("use Purbeurre")

	def create_table(self):
		for table_name in self.table:
			table_description = self.table[table_name]
			try:
				self.connect_database()

				print("creating table {}:".format(table_name))
				self.cursor.execute(table_description)
			except mysql.connector.Error as err:
				if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
					print("already exists.")
				else:
					print(err.msg)
			else:
				print("OK")
		self.cursor.close()
		
	def delete_data(self):
		self.cursor("delete from Food;"
			"delete from Category"
			"delete from Favorite")

	def get_category_list(self):
		self.connect_database()
		self.cursor.execute("select id, categories from category order by id;")

		self.category_list = []

		for categories in self.cursor:
			self.category_list.append(categories)
			self.controller.category_menu(self.category_list)

	def get_food_list(self, category_choice ):
		self.category_choice = category_choice
		print(self.category_choice)
		self.connect_database()
		self.cursor.execute("select id, product_name from food where category_id = {0} order by id".format(self.category_choice))
		self.products_list = []
		for products in self.cursor:
			self.products_list.append(products)
		self.controller.products_menu(self.products_list)

	def get_food(self, food_choice):
		self.food_choice = food_choice
		self.connect_database()
		self.cursor.execute("select * from food where id = {0}".format(self.food_choice))
		for product in self.cursor:
			print(product[1])

	


