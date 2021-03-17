
import tables
import tkinter as tk



class Interface:

	def __init__(self):
		self.var = 0

	def main_menu(self):

		self.text_m1 = "Menu principal \n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
		1 : Sélectionnez une catégorie \n \
		2 : Choisir un aliment à substitué. \n \
		q : Quitter le programme."
		print(self.text_m1)

	def category_menu(self, category_list):
		self.category_list = category_list

		i=0
		print("Menu de catégories \n Mode d'emploi : Rentrez le numéro correspondant au choix.\n \
			Rentrez lavaleur q pour quitter le programme.")
		"""for category self.category_list:
			print("{0} : {1}.".format(i, category))
			i+=1
"""
	def products_menu(self, products_list):
		i = 1
		self.products_list = products_list
		txt_prod = "Liste de poruits\n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			Rentrez la valeur q pour quitter le programme."
		print(txt_prod)

		for product in self.products_list:
			print("{0} : {1}".format(i, product))
			i+=1








	





	


