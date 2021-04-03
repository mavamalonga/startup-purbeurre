# -*- coding: utf-8 -*-

import tables
import tkinter as tk
import database


class Interface:

	def __init__(self, window_dict):
		self.window_dict = window_dict

	def displayHelp(self, url):
		self.url = url

		if self.url == 'home':
			print(self.window_dict['home'])

		elif self.url == 'all_categories':
			print(self.window_dict['all_categories'])

		elif self.url == 'all_products':
			print(self.window_dict['all_products'])

		elif self.url == 'product':
			print(self.window_dict['product'])

		elif self.url == 'product_substitute':
			print(self.window_dict['product_substitute'])


		elif self.url == 'home_favorites':
			print(self.window_dict['home_favorites'])

		elif self.url == 'favorite':
			print(self.window_dict['favorite']) 


	def displayCategories(self, category_id, category_name):
		self.category_id = category_id
		self.category_name = category_name
		print("			{0} : {1}".format(self.category_id, self.category_name))


	def displayProductList(self, product_id, product_name):
		self.product_id = product_id
		self.product_name = product_name
		print("			{0} : {1}".format(self.product_id, self.product_name))

	def displayProductId(self, feature):
		self.list_name = ['Nom', 'Marque', 'Ingredients', 'Nutriments', 'Nutri-score',
		'Quantity', 'Magasin(s)']
		self.feature = feature

		for name, value in zip(self.list_name, self.feature):
			print("			{0} : {1}".format(name, value))
		print("\n")


	def displaySubstituteList(self, sub_id, name, nutriscore):
		print("			{0} : {1} {2}".format(sub_id, name, nutriscore ))

	
	def displayFavoriteList(self, list_index, list_id_food, list_id_substitue):
		self.list_fav_index = list_index
		self.list_fav_food = list_id_food
		self.list_fav_sub = list_id_substitue

		self.i = 0
		for tuple_favorite in zip(self.list_fav_food, self.list_fav_sub):
			print("			{0} : {1} &".format(self.list_fav_index[self.i][0], tuple_favorite[0][0]))
			print("			{0}\n".format(tuple_favorite[1][0]))
			self.i += 1

	def displaySaveMsg(self):
		print("Enregistrement validé.")






	







	


