# -*- coding: utf-8 -*-

import tables
import tkinter as tk
import database


class Interface:

	def __init__(self, window_dict):
		self.window_dict = window_dict

	def InitData(self, action, response):
		self.action = action
		self.response = response
		if self.action == "createData":
			print(		"{0}".format(self.response))
		if self.action == "createTable":


	def displayError(self):
		print("			Veillez rentrer une valeur valide.")

	def display_help(self, url):
		self.url = url

		if self.url == 'home':
			print(self.window_dict['home'])

		if self.url == 'all_categories':
			print(self.window_dict['all_categories'])

		if self.url == 'all_products':
			print(self.window_dict['all_products'])


	def category_menu(self, category_id, category_name):
		self.category_id = category_id
		self.category_name = category_name
		print("			{0} : {1}".format(self.category_id, self.category_name))


	def products_menu(self, select_product_list):
		self.select_product_list = select_product_list
		for id_and_product in self.select_product_list:
			print("			{0} : {1}".format(id_and_product[0], id_and_product[1]))

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

		if len(self.list_fav_index) == 0:
			print("				Liste vide !")

		else:
			self.i = 0
			for tuple_favorite in zip(self.list_fav_food, self.list_fav_sub):
				print("			{0} : {1} <-------> {2}".format(self.list_fav_index[self.i][0], tuple_favorite[0][0], tuple_favorite[1][0]))
				self.i += 1

	def display_success_save(self):
		print("Enregistrement validé.")







	





	


