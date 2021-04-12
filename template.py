#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tables
import tkinter as tk
import database


class Interface:

	def __init__(self, window_dict):
		self.window_dict = window_dict
		self.emptyCase = ' '
		self.featureNameList = ['Nom', 'Marque', 'Ingredients', 'Nutriments', 'Nutri-score',
		'Quantity', 'Magasin(s)']


	def displayNotify(self, error):
		print(self.emptyCase*24 + "{0}".format(error))


	def displayHelp(self, url):
		self.url = url
		for url, theme in self.window_dict.items():
			if self.url == url:
				print(self.window_dict[self.url])

	def displayCategories(self, category_id, category_name):
		print(self.emptyCase*24 + "{0} : {1}".format(category_id, category_name))


	def displayProducts(self, product_id, product_name):
		print(self.emptyCase*24 + "{0} : {1}".format(product_id, product_name))


	def displayProductId(self, product_name, brands, ingredients, nutriments, 
		nutriscore, quantity, store):
		self.featureValue = featureValue

		print(self.emptyCase*24 + "Nom : {0}".format(product_name))
		print(self.emptyCase*24 + "Marque : {0}".format(brands))
		print(self.emptyCase*24 + "Ingredients : {0}".format(ingredients))
		print(self.emptyCase*24 + "Nutriments : {0}".format(nutriments))
		print(self.emptyCase*24 + "Nutri-score : {0}".format(nutriscore))
		print(self.emptyCase*24 + "Quantite : {0}".format(quantity))
		print(self.emptyCase*24 + "Magasin(s) : {0}".format(store))
		print("\n")

	def displaySubstituteList(self, substitute_id, substitute_name, substitute_grade):
		print(self.emptyCase*24 + "{0} : {1}" + "nutriscore": + "{2}".format(substitute_id, substitute_name, 
			substitute_grade))


	def displayFavoriteList(self, allId, allProductsName, allsubstitutesName):
		self.i = 0
		for item in range(len(allId):
			print(allId[self.i] + allProductsName[self.i] + allsubstitutesName[self.i])
			self.i += 1

	def displayFeatureFavorite(self, product, substitute):
		
		print(self.emptyCase*24 + "Nom : {0}".format(product_name))
		print(self.emptyCase*24 + "Marque : {0}".format(brands))
		print(self.emptyCase*24 + "Ingredients : {0}".format(ingredients))
		print(self.emptyCase*24 + "Nutriments : {0}".format(nutriments))
		print(self.emptyCase*24 + "Nutri-score : {0}".format(nutriscore))
		print(self.emptyCase*24 + "Quantite : {0}".format(quantity))
		print(self.emptyCase*24 + "Magasin(s) : {0}".format(store))
		print("\n")






	