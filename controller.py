# -*- coding: utf-8 -*-

import template
import database
import tables

class Controlboard (database.Data):
	def __init__(self, table):
		super().__init__(table)

	def ctrl_main(self):
		self.menu = 'main'
		self.display_help(self.menu)

	def ctrl_category(self):
		self.menu = 'category'
		self.display_help(self.menu)
		self.get_category()

	def ctrl_favorite(self):
		self.menu = 'favorite'
		self.display_help(self.menu)
		self.get_favorite()

	def ctrl_product(self, index):
		self.index = index
		self.menu = 'product'
		self.display_help(self.menu)
		self.get_product(self.index)

	def ctrl_feature(self, category_choice, product_choice, substitute):

		self.substitute = substitute

		if int(str(substitute)) == 0:
			self.menu = 'feature'
			self.display_help(self.menu)
			self.get_feature(product_choice)
			self.select_substitute_list(category_choice, product_choice)
		elif int(str(substitute)) > 0:

			self.menu = 'comparison'
			self.display_help(self.menu)
			self.get_feature(product_choice)
			self.select_substitute(substitute)

	def ctrl_save(self, product_choice, substitute):
		self.menu = 'camparison'
		self.display_help(self.menu)
		self.save_product(product_choice, substitute)

	def ctrl_feature_favorite(self, favorite_id):
		self.menu = 'feature_favorite'
		self.display_help(self.menu)
		self.select_feature_favorite(favorite_id)

	def ctrl_delete(self):
		self.menu = 'delete'
		self.display_help(self.menu)
		self.delete_porduct(self.index)

