
import tables
import tkinter as tk
import model



class Interface:

	def __init__(self):
		self.echa = 0
		

	def main_menu(self):

		self.text_m1 = "Menu principal \n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
		1 : Sélectionnez une catégorie \n \
		2 : Choisir un aliment à substitué. \n \
		q : Quitter le programme."
		print(self.text_m1)


	def category_menu(self, ctg_id, ctg_name):
		self.ctg_id = ctg_id
		self.ctg_name = ctg_name
		print(" {0} : {1}.".format(self.ctg_id, self.ctg_name))


	def products_menu(self, product_id, product_name):
		self.product_id = product_id
		self.product_name = product_name
		print("{0} : {1}".format(self.product_id, self.product_name))

	def display_prouct_value(self):
		self.product_value = product_value










	





	


