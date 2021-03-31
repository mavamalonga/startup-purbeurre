# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
import tables
import tkinter as tk
import template
import windows


class Data(template.Interface):

	def __init__(self, table, window_dict):
		super().__init__(window_dict)
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
		self.list_category_id = []
		self.connect_database()
		self.cursor.execute("call get_categories()")
		for category_tuple in self.cursor:

			self.category_menu(category_tuple[0], category_tuple[1])
			self.list_category_id.append(category_tuple[0])
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
			self.display_feature(feature)
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
			self.display_feature(feature)
		self.cursor.close()


	def save_product(self, product_choice, substitute):
		self.connect_database()
		self.cursor.execute("insert into favorite (product_id, substitute_id) values ({0}, {1})".format(product_choice, substitute))
		self.cnx.commit()
		self.cursor.close()
		self.display_success_save()

	def get_favorite(self):

		self.list_fav_food = []
		self.list_fav_sub = []
		self.list_fav_index = []

		self.connect_database()
		self.cursor.execute("select product_name from product where id in ( select product_id from favorite order by id)")
		for prod_food in self.cursor:
			self.list_fav_food.append(prod_food)
		self.cursor.close()

		self.connect_database()
		self.cursor.execute("select product_name from product where id in ( select substitute_id from favorite order by id)")
		for prod_sub in self.cursor:
			self.list_fav_sub.append(prod_sub)
		self.cursor.close()

		self.connect_database()
		self.cursor.execute("select id from favorite order by id")
		for index in self.cursor:
			self.list_fav_index.append(index)
		self.cursor.close()

		self.display_favorite(self.list_fav_index, self.list_fav_food, self.list_fav_sub)
		
	def delete_favorite(self, favorite_id):
		self.favorite_id = favorite_id
		self.connect_database()
		self.cursor.execute("delete from favorite where id = {0}".format(self.favorite_id))
		self.cnx.commit()
		self.cursor.close()

	def select_feature_favorite(self, favorite_id):
		self.favorite_id = favorite_id
		self.connect_database()
		self.cursor.execute("select product_id from favorite where id = {0}".format(self.favorite_id))
		for product_id in self.cursor:
			self.product_id = product_id[0]
		self.cursor.close()

		self.connect_database()
		self.cursor.execute("select substitute_id from favorite where id = {0} ".format(self.favorite_id))
		for substitute_id in self.cursor:
			self.substitute_id = substitute_id[0]
		self.cursor.close()

		self.connect_database()
		self.cursor.execute("select category_id from product where id = {0} ".format(self.substitute_id))
		for category_id in self.cursor:
			self.category_id = category_id[0]
		self.cursor.close()


		self.get_feature(self.product_id)
		self.select_substitute(self.substitute_id)



		
