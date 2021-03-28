# -*- coding: utf-8 -*-

import tables
import tkinter as tk
import database





class Interface:

	def __init__(self):
		self.echa = 0

	def displayHelp(self, url, category_id=0, product_id=0, substitute_id=0):
		self.url = url
		self.category_id = category_id
		self.product_id = product_id
		self.substitute_id = substitute_id


		self.text_favorite ="\n 		########## Menu {0} ########## \n \
		Mode d'emploi : Pour sélectionner un favori, rentrez le numéro correspondant au choix. \n \
			r : retour \n \
			q : Quitter \n \
		".format(self.url)


		if self.url == 'main':
			self.txt_main = "		########## Menu principal ##########\n \
			Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			1 : Sélectionnez une catégorie \n \
			2 : Choisir un aliment à substitué. \n \
			q : Quitter le programme. \n \
			"
			print(self.txt_main)



		if self.url == 'main/categories' or self.url == 'main/categories/':
			self.txt_categories = "\n 		########## url : {0}{1} ###########\n \
			Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			r : retour \n \
			q : Quitter \n \
			".format(self.url, self.category_id)
			print(self.txt_categories)



		if self.url == 'main/categories/{0}products/':
			self.url = self.url.format(self.category_id)
			self.txt_product ="\n 		########## url : {0}{1} ########## \n \
			Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			r : retour \n \
			q : Quitter \n \
			".format(self.url, self.product_id)
			print(self.txt_product)

	

		if self.url == 'main/categories/{0}/products/{1}/':

			self.url =  self.url.format(self.category_id, self.product_id)
			self.txt_substitute ="\n 		########## url : {0}{1} ########## \n \
			Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			r : retour \n \
			q : Quitter \n \
			e : Enregistrer \n \
			".format(self.url, self.substitute_id)

			print(self.txt_substitute)
	



		if self.url == 'favorite' or self.url == 'feature_favorite':
			print(self.text_favorite)
		if self.url == 'comparison':
			print(self.txt_comparison)

		return self.url




	def category_menu(self, category_id, category_name):
		self.category_id = category_id
		self.category_name = category_name
		print("			{0} : {1}".format(self.category_id, self.category_name))


	def products_menu(self, product_id, product_name):
		self.product_id = product_id
		self.product_name = product_name
		print("			{0} : {1}".format(self.product_id, self.product_name))

	def display_feature(self, feature0, feature1, feature2, feature3, feature4,
		feature5, feature6):
		print("			Nom : {0}".format(feature0))
		print("			Marque : {0}".format(feature1))
		print("			Ingredients: {0}".format(feature2))
		print("			Nutriments : {0}".format(feature3))
		print("			Nutri-score : {0}".format(feature4))
		print("			Quantity : {0}".format(feature5))
		print("			Magasin(s): {0}\n".format(feature6))

	def display_substitute(self, sub_id, name, nutriscore):
		print("			{0} : {1} {2}".format(sub_id, name, nutriscore ))

	
	def display_favorite(self, list_index, list_id_food, list_id_substitue):
		self.list_fav_index = list_index
		self.list_fav_food = list_id_food
		self.list_fav_sub = list_id_substitue

		self.i = 0
		for tuple_favorite in zip(self.list_fav_food, self.list_fav_sub):
			print("	{0} : {1} <-------> {2}".format(self.list_fav_index[self.i][0], tuple_favorite[0][0], tuple_favorite[1][0]))
			self.i += 1

	def display_success_save(self):
		print("Enregistrement validé.")







	





	


