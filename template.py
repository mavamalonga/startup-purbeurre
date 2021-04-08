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

	"""Display notify of errors or message return after 
	execute method, database execute cursor.execute"""

	def displayNotify(self, error):
		for url, theme in self.window_dict.items():
			if error == url:
				print("{0}".format(theme))

	"""Display in each window the instruction commands about it, this method take argument url for display ythe true 
	message in function of window"""

	def displayHelp(self, url):
		self.url = url
		for url, theme in self.window_dict.items():
			if self.url == url:
				print(self.window_dict[self.url])

	"""method display categorires list, produicts list and substitutes list
	when value3='none' => value1= id, value2 = product_name
	when value3!='none' => value1= id, value2 = prodcut_name, value3 = nutrition_grades
	"""
	def displayList(self, value1, value2,  value3='none'):
		if value3 == 'none':
			print(self.emptyCase*24 + "{0} : {1}".format(value1, value2))
		else:
			print(self.emptyCase*24 + "{0} : {1} {2}".format(value1, value2, value3))


	def displayProductId(self, featureValue):
		self.featureValue = featureValue
		for name, feature in zip(self.featureNameList, self.featureValue):
			print(self.emptyCase*24 + "{0} : {1}".format(name, feature))
		print("\n")


	def displayFavoriteList(self, idList, productNameList, substituteNameList):
		self.i = 0
		self.idList = idList
		self.productNameList = productNameList
		self.substituteNameList = substituteNameList

		for names in zip(self.productNameList, self.substituteNameList):
			print(self.emptyCase*24 + "{0} : {1} &".format(self.idList[self.i][0], names[0][0]))
			print(self.emptyCase*24 + "{0}\n".format(names[1][0]))
			self.i += 1






	







	


