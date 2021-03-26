# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
import tables
import tkinter as tk
import template


class Data(template.Interface):

	def __init__(self, table):
		super().__init__()
		self.table = table

	def connect_database(self):
		self.cnx = mysql.connector.connect(user='root', host='localhost', password='100ml80%vol.', port='330')
		self.cursor = self.cnx.cursor()
		self.cursor.execute("use Purbeurre")

	def create_database(self):
		try:
			self.connect_database()
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

	def get_category(self):
		self.connect_database()
		self.cursor.execute("call get_categories()")
		for category_tuple in self.cursor:
			self.category_menu(category_tuple[0], category_tuple[1])
		self.cursor.close()

	def get_product(self, category_choice):

		self.connect_database()
		self.category_choice = category_choice
		self.cursor.execute("call get_product({0})".format(self.category_choice))
		for products in self.cursor:
			self.products_menu(products[0], products[1])
		self.cursor.close()

	def get_feature(self, product_choice):

		self.connect_database()
		self.cursor.execute("call get_feature({0})".format(product_choice))

		for feature in self.cursor:

			self.display_feature(feature[0], feature[1], feature[2], feature[3], feature[4],
				feature[5], feature[6])
		self.cursor.close()


	def select_substitute_list(self, index_c, index_p):

		self.connect_database()
		self.cursor.execute("call select_substitute({0}, {1})".format(index_c, index_p))
		for substitute in self.cursor:
			self.display_substitute(substitute[0], substitute[1], substitute[2])
		self.cursor.close()

	def select_substitute(self, substitute):

		self.connect_database()
		self.cursor.execute("call get_feature({0})".format(substitute))

		for feature in self.cursor:

			self.display_feature(feature[0], feature[1], feature[2], feature[3], feature[4],
				feature[5], feature[6])
		self.cursor.close()


	def save_product(self, product_choice, substitute):
		self.connect_database()
		self.cursor.execute("insert into favorite (product_id, substitute_id) values ({0}, {1})".format(product_choice, substitute))
		self.cnx.commit()
		self.cursor.close()

	def get_favorite(self):

		self.list_fav_food = []
		self.list_fav_sub = []
		self.list_fav_index = []

		self.connect_database()
	
		self.cursor.execute("select product_name from product where id in ( select product_id from favorite order by id)")
		for prod_food in self.cursor:
			self.list_fav_food.append(prod_food)

		self.cursor.execute("select product_name from product where id in ( select substitute_id from favorite order by id)")
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



		
