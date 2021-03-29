# -*- coding: utf-8 -*-

import tables
import tkinter as tk
import database


class Interface:

	def __init__(self, window_dict):
		self.window_dict = window_dict

	def displayHelp(self, url, category_id=0, product_id=0, substitute_id=0):
		self.url = url
		self.category_id = category_id
		self.product_id = product_id
		self.substitute_id = substitute_id

		for urls in self.window_dict:
			if urls == self.url:
				window = self.window_dict[self.url]
				if len(self.url) <= 16 :
					window = window.format(self.url, self.category_id)
				elif 16 < len(self.url) <= 27:
					self.url = self.url.format(self.category_id)
					window = window.format(self.url, self.product_id)
				elif len(self.url) > 28:
					self.url =  self.url.format(self.category_id, self.product_id)
					window = window.format(self.url, self.substitute_id)
				print(window)
				print(len(self.url))


	def category_menu(self, category_id, category_name):
		self.category_id = category_id
		self.category_name = category_name
		print("			{0} : {1}".format(self.category_id, self.category_name))


	def products_menu(self, product_id, product_name):
		self.product_id = product_id
		self.product_name = product_name
		print("			{0} : {1}".format(self.product_id, self.product_name))

	def display_feature(self, feature):
		self.list_name = ['Nom', 'Marque', 'Ingredients', 'Nutriments', 'Nutri-score',
		'Quantity', 'Magasin(s)']
		self.feature = feature

		for name, value in zip(self.list_name, self.feature):
			print("			{0} : {1}".format(name, value))
		print("\n")


	def display_substitute(self, sub_id, name, nutriscore):
		print("			{0} : {1} {2}".format(sub_id, name, nutriscore ))

	
	def display_favorite(self, list_index, list_id_food, list_id_substitue):
		self.list_fav_index = list_index
		self.list_fav_food = list_id_food
		self.list_fav_sub = list_id_substitue

		self.i = 0
		for tuple_favorite in zip(self.list_fav_food, self.list_fav_sub):
			print("			{0} : {1} <-------> {2}".format(self.list_fav_index[self.i][0], tuple_favorite[0][0], tuple_favorite[1][0]))
			self.i += 1

	def display_success_save(self):
		print("Enregistrement validé.")







	





	


