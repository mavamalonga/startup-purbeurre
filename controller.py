
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

	def category_menu(self, ctg1, ctg2, ctg3, ctg4):

		self.ctg1 = ctg1
		self.ctg2 = ctg2
		self.ctg3 = ctg3
		self.ctg4 = ctg4

		self.text_m2 = "Menu des catégories \n Mode d'emploi : Rentrez le numéro correspondant au choix. \n \
		1 : {0} \n \
		2 : {1}\n \
		3 : {2} \n \
		4 : {3} \n\
		q : Quitter le programme.".format(self.ctg1, self.ctg2, self.ctg3, self.ctg4)


		print(self.text_m2)

	def products_menu(self, products_list):
		i = 1
		self.products_list = products_list
		for product in self.products_list:
			print("{0} : {1}".format(i, product))
			i+=1








	





	


