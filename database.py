import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
import tables
import tkinter as tk
import template



class Data(template.Interface):

	def __init__(self, table):
		super().__init__()
		self.cnx = mysql.connector.connect(user='root', host='localhost', password='100ml80%vol.', port='330')
		self.cursor = self.cnx.cursor()
		self.cursor.execute("use Purbeurre")

	def create_database(self):
		try:
			self.cursor.execute("create database Purbeurre default character set 'utf8'")
		except mysql.connector.Error as err:
			print("Failed creating database Purbeurre")
			exit(1)

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

	def get_category(self):
		self.cursor.execute("select distinct id, categories from category order by id;")
		for category_tuple in self.cursor:
			self.category_menu(category_tuple[0], category_tuple[1])


	def get_product(self, category_choice):

		self.category_choice = category_choice
		self.cursor.execute("select distinct id, product_name from food where category_id = {0} \
			order by id".format(self.category_choice))
		
		for products in self.cursor:
			self.products_menu(products[0], products[1])

	def get_feature(self, product_choice):
		self.product_choice = product_choice
		self.product_substitute = int(str(self.product_choice)) + 1
		self.product_substitute = str(self.product_substitute)
		self.cursor.execute("select id, product_name, brands, nutrition_grades from food where id = {0} \
			union select id, product_name, brands, nutrition_grades from food where id = {1} \
			".format(self.product_choice, self.product_substitute))

		self.feature_list = []
		for feature in self.cursor:
			self.feature_list.append(feature)
		self.display_feature(self.feature_list)


	def save_product(self):
		print("{0} ".format(self.product_substitute))

		#self.cursor.execute("insert into favorite (id_food, id_substitute) values ({0}, {1})".format(self.product_choice, self.product_substitute))
		#self.cnx.commit()
		#print("Les produits ont été ajoutés au favories.")
		

	def get_favorite(self):
		self.list_fav_sub = []
		self.list_fav_food = []
		self.list_fav_index = []
		self.cursor.execute("select product_name, brands, nutrition_grades from food where id in ( select id_food from favorite order by id)")
		for prod_food in self.cursor:
			self.list_fav_food.append(prod_food)

		self.cursor.execute("select product_name, brands, nutrition_grades from food where id in ( select id_substitute from favorite order by id)")
		for prod_sub in self.cursor:
			self.list_fav_sub.append(prod_sub)

		self.cursor.execute("select id from favorite order by id")
		for index in self.cursor:
			self.list_fav_index.append(index)

		self.display_favorite(self.list_fav_index, self.list_fav_food, self.list_fav_sub)
		
	def delete_favorite(self, choice_favorite):
		self.choice_favorite = choice_favorite
		self.cursor.execute("delete from favorite where id = {0}".format(self.choice_favorite))

	def focus_favorite(self, choice_display):
		self.index_food = 0
		self.index_substitute = 0
		self.choice_display = choice_display
		self.cursor.execute("select id_food, id_substitute from favorite where id = {0}".format(self.choice_display))
		for tuple_favorite in self.cursor:
			self.index_food_substitute = tuple_favorite

		self.cursor.execute("select product_name, brands, nutrition_grades from food where id = {0}\
			union select product_name, brands, nutrition_grades from food where id = {1} ".format(self.index_food_substitute[0],
			self.index_food_substitute[1]))

		for tuple_fav in self.cursor:
			print(tuple_fav)








		
