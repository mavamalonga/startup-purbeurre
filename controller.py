# -*- coding: utf-8 -*-

import template
import database
import tables

class Controlboard (database.Data):
	def __init__(self, table):
		super().__init__(table)

	def main(self, url):
		self.displayHelp(url)

	def favorite(self, url):
		self.display_help(url)
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

	def ctrl_feature_favorite(self, favorite_id):
		self.menu = 'feature_favorite'
		self.display_help(self.menu)
		self.select_feature_favorite(favorite_id)

	def ctrl_delete(self):
		self.menu = 'delete'
		self.display_help(self.menu)
		self.delete_porduct(self.index)

