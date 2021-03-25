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
		self.menu = 'favorie'
		self.display_help(self.menu)
		self.get_favorite()

	def ctrl_product(self, index):
		self.index = index
		self.menu = 'product'
		self.display_help(self.menu)
		self.get_product(self.index)

	def ctrl_feature(self, index_c, index_p):
		self.index_c = index_c
		self.index_p = index_p
		self.menu = 'feature'
		self.display_help(self.menu)
		self.get_feature(self.index_p)
		self.select_substitute(self.index_c, self.index_p)

	def ctrl_save(self):
		self.display_help(self.menu)
		self.save_product()

	def ctrl_delete(self):
		self.menu = 'delete'
		self.display_help(self.menu)
		self.delete_porduct(self.index)

