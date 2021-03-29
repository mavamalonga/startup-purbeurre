# -*- coding: utf-8 -*-

import template
import database
import tables
import windows

class Controlboard (database.Data):
	def __init__(self, table, window_dict):
		super().__init__(table, window_dict)

	def main(self, url):
		self.displayHelp(url)

	def favorite(self, url):
		self.displayHelp(url)
		self.get_favorite()

	def categories(self, url):
		self.displayHelp(url)
		self.get_category()

	def products(self, url, category_id):
		self.displayHelp(url, category_id=category_id)
		self.get_product(category_id)

	def select_product(self, url, category_id, product_id, substitute_id):

		if int(str(substitute_id)) == 0:
			self.displayHelp(url, category_id, product_id)
			self.get_feature(product_id)
			self.select_substitute_list(category_id, product_id)
		elif int(str(substitute_id)) > 0:

			self.displayHelp(url, category_id, product_id, substitute_id)
			self.get_feature(product_id)
			self.select_substitute(substitute_id)

	def save(self, product_choice, substitute):
		self.menu = 'comparison'
		self.save_product(product_choice, substitute)
		print('Produits ajoutés !')

	def select_favorite(self, url, favorite_id):
		self.displayHelp(url, product_id=favorite_id)
		self.select_feature_favorite(favorite_id)

	def delete_favorite_id(self, favorite_id):
		print(favorite_id)
		self.delete_favorite(favorite_id)
		print("Le favori {0} à été supprimé.".format(favorite_id))

