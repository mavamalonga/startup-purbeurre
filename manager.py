# -*- coding: utf-8 -*-

import template
import database
import tables
import windows

class Manager (database.Data):
	def __init__(self, table, windows_dict):
		super().__init__(table, windows_dict)

	def main(self, url):
		self.displayHelp(url)

	def man_main(self, url, event):
		self.event = event
		if self.event == '1':
			self.url = 'main/categories'
			self.displayHelp(self.url)
			self.get_category()
			self.event = 0
		if self.event == '2':
			self.url = 'main/favories'
			self.board.favorite(url)
			self.event = 0

	def man_favorite1(self):
		if self.event == 'r':
			self.url = 'main'
			self.board.main(url)
			self.event = 0
		if int(str(self.event)) > 0:
			self.product_id = self.event
			url = 'main/favorites/'
			self.board.select_favorites(self.url, self.event)
			self.event = 0

	def man_favorite2(self):
		if self.evengt == 'r':
			self.url = 'main/favorites'
			self.board.favorite(self.url)
			self.event =0
		if self.event == 's':
			self.board.delete_favorite_id(self.product)
			self.event = 0
		if int(str(self.event)) > 0:
			pass
		self.event = 0

	def man_categories1(self):
		if self.event == 'r':
			self.url = 'main'
			self.board.main(self.url)
			self.event = 0
		if int(str(self.event)) > 0:
			self.url = 'main/categories/'
			self.category_id = self.event
			self.board.products(self.url, self.category_id)
		self.event = 0

	def man_categories2(self):
		if self.event == 'r':
			self.url = 'main/categories'
			self.board.categories(self.url)
			self.event = 0
		if int(str(self.event)) > 0:
			self.url = 'main/categories/{0}/products/'
			self.product_id = self.event
			self.substitute_id = 0
			self.board.select_product(self.url, self.category_id, 
				self.product_id, self.substitute_id)
		self.event = 0

	def man_product1(self):
		if self.event == 'r':
			self.url = 'main/categories/'
			self.board.products(self.url, self.category_id)
			self.event = 0
		if int(str(self.event)) > 0:
			self.url = 'main/categories/{0}/products/{1}/'
			self.substitute_id = self.event
			self.board.select_product(self.url, self.category_id,
				self.product_id, substitute_id)
		self.event = 0

	def man_product2(self):
		if  self.event == 'e':
			self.board.save(self.product_id, self.substitute_id)
			self.board.details(self.category_id, self.product_id,
				self.substitute_id)
		if self.event == 'r':
			self.url = 'main/categories/{0}/products/'
			self.substitute_id = 0
			self.board.select_product(self.url, self.category_id,
				self.product_id, self.substitute_id)
		self.event = 0




