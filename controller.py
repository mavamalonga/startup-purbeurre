
import tables
import tkinter as tk
import model



class Interface:

	def __init__(self):
		self.echa = 0

	def display_help(self, menu):
		self.menu = menu

		self.txt_main = "			Menu principal \n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			1 : Sélectionnez une catégorie \n \
			2 : Choisir un aliment à substitué. \n \
			q : Quitter le programme."

		self.txt_other = "			Menu {0} \n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			r : retour \n \
			q : Quitter \n \
		".format(self.menu)

		self.txt_value = "			Menu {0} \n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
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


	def category_menu(self, ctg_id, ctg_name):
		self.ctg_id = ctg_id
		self.ctg_name = ctg_name
		print("			{0} : {1}".format(self.ctg_id, self.ctg_name))


	def products_menu(self, product_id, product_name):
		self.product_id = product_id
		self.product_name = product_name
		print("			{0} : {1}".format(self.product_id, self.product_name))

	def display_product(self, name, brands, nutriments):
		self.name = name
		self.brands = brands 
		self.nutriments = nutriments
		print("			Nom produit : {0}".format(self.name))
		print("			Marque : {0}".format(self.brands))
		print("			Nutriments : {0}".format(self.nutriments))

	def display_substitue(self, name, brands, nutriments):
		self.name = name
		self.brands = brands 
		self.nutriments = nutriments
		print("\n 			Substitue  ")
		print("			Nom produit : {0}".format(self.name))
		print("			Marque : {0}".format(self.brands))
		print("			Nutriments : {0}".format(self.nutriments))










	





	


