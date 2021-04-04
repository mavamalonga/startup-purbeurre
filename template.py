# -*- coding: utf-8 -*-

import tables
import tkinter as tk
import database


class Interface:

	def __init__(self, window_dict):
		self.window_dict = window_dict


	"""Display notify of errors or message return after 
	execute method, database execute cursor.execute"""

	def displayNotify(self, msg):
		print("{0}".format(msg))

	"""Display in each window the instruction commands about it, this method take argument url for display ythe true 
	message in function of window"""

	def displayHelp(self, url):
		self.url = url
		for url, theme in self.window_dict.items():
			if self.url == url:
				print(self.window_dict[self.url])

	def displayCategories(self, category_id, category_name):
		print("			{0} : {1}".format(category_id, category_name))


	def displayProductList(self, product_id, product_name):
		print("			{0} : {1}".format(product_id, product_name))

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






	







	


