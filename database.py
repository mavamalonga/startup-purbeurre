import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
import tables
import tkinter as tk
import controller
import model

class Database:

	def __init__(self, table, Interface):
		self.Interface = Interface
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
		self.cursor.execute("select distinct id, categories from category order by id;")
		self.category_id_list = []
		for each_tuple in self.cursor:
			self.ctg_id, self.ctg_name = each_tuple
			self.Interface.category_menu(self.ctg_id, self.ctg_name)
			self.category_id_list.append(self.ctg_id)
		self.nb_categorie = len(self.category_id_list)



			

	def get_product_list(self, category_choice):

		self.category_choice = category_choice
		self.connect_database()
		self.connect_database()
		self.cursor.execute("select distinct id, product_name from food where category_id = {0} \
			order by id".format(self.category_choice))
		
		self.products_list = []
		for products in self.cursor:
			self.product_id, self.product_name = products
			self.Interface.products_menu(self.product_id, self.product_name)


	def get_product(self, product_choice):
		self.product_choice = product_choice
		self.connect_database()
		self.cursor.execute("select product_name, brands, nutrition_grades from food where id = {0}".format(self.product_choice))
		for product in self.cursor:
			self.value = product
		self.Interface.display_product(self.value[0], self.value[1], self.value[2])

		self.cursor.execute("select product_name, brands, nutrition_grades from food where id = {0} + '1'".format(self.product_choice))
		for product in self.cursor:
			self.value = product
		self.Interface.display_substitue(self.value[0], self.value[1], self.value[2])

"""
	def save_product_at_favorite(self, product_id, substitue_id):
		self.product_id = product_id
		self.substitue_id = substitue_id
		self.connect_database()
		self.cursor.execute("insert into favorite (id_food, id_substitue) values ({0}, {0})".format(self.product_id, self.substitue_id)
"""