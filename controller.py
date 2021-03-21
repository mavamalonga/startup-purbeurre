
import tables
import tkinter as tk
import model
import database


class Interface:

	def __init__(self):
		self.echa = 0

	def display_help(self, menu):
		self.menu = menu

		self.txt_main = "			\nMenu principal \n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			1 : Sélectionnez une catégorie \n \
			2 : Choisir un aliment à substitué. \n \
			q : Quitter le programme."

		self.txt_other = "			\nMenu {0} \n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			r : retour \n \
			q : Quitter \n \
		".format(self.menu)

		self.txt_value = "			\nMenu {0} \n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			r : retour \n \
			q : Quitter \n \
			s : Enregistrer \n \
		".format(self.menu)


		if self.menu == 'main':
			print(self.txt_main)
		if self.menu == 'category':
			print(self.txt_other)
		if self.menu == 'product':
			print(self.txt_other)
		if self.menu == 'value':
			print(self.txt_value)


	def category_menu(self, category_id, category_name):
		self.category_id = category_id
		self.category_name = category_name
		print("			{0} : {1}".format(self.category_id, self.category_name))


	def products_menu(self, product_id, product_name):
		self.product_id = product_id
		self.product_name = product_name
		print("			{0} : {1}".format(self.product_id, self.product_name))

	def display_product(self):
		print("			Produit : Substitute")
		print("			Nom  \
			{0} : {1}".format())
		print("			Marque  \
			{0} : {1}".format(self.brands))
		print("			Nutriments \
		 	{0} : {1}".format(self.nutriments))

	
	def display_favorite(self, id_food, id_substitue):
		self.id_food = id_food
		self.id_substitue = id_substitue
		











	





	


