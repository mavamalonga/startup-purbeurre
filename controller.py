
import tables
import tkinter as tk
import model



class Interface:

	def __init__(self, Product, Catgory, Favorite):
		self.Product = Product
		self.Catgory = Catgory
		self.Favorite = Favorite

	def main_menu(self):

		self.text_m1 = "Menu principal \n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
		1 : Sélectionnez une catégorie \n \
		2 : Choisir un aliment à substitué. \n \
		q : Quitter le programme."
		print(self.text_m1)

	def category_menu(self, category_list):
		print(" {0} : {1}.".format(self.Catgory.category_id, self.Catgory.catégories_name))


	def products_menu(self, products_list):

		self.products_list = products_list
		txt_prod = "Liste de poruits\n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
			Rentrez la valeur q pour quitter le programme."
		print(txt_prod)

		for product in self.products_list:
			self.tuple_products = product
			self.product_id, self.product_name = self.tuple_products
			print("{0} : {1}".format(self.product_id, self.product_name))

	def display_prouct_value(self, product_value):
		self.product_value = product_value










	





	


