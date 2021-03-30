# -*- coding: utf-8 -*-

import template
import database
import tables
import windows

class Manager (database.Data):
	def __init__(self, table, windows_dict):
		super().__init__(table, windows_dict)

	def home(self):
		self.url = 'home'
		self.display_help(self.url)
		if self.event == '1':
			self.url = 'all_categories'
			self.displayHelp(self.url)
			self.get_category()
		elif self.event == '2':
			self.url = 'main/favories'
			self.displayHelp(self.url)
			self.get_favorite()

	def all_categories(self):
		if self.event == 'r':
			self.main_principal()
		elif int(str(self.event)) > 0:
			self.url = 'main/categories/'
			self.category_id = self.event
			self.displayHelp(self.url, category_id=self.category_id)
			self.get_product(self.category_id)

	def check_substitute(self):

		if int(str(self.substitute_id)) == 0:
			self.displayHelp(self.url, self.category_id, self.product_id)
			self.get_feature(self.product_id)
			self.select_substitute_list(self.category_id, self.product_id)
		elif int(str(self.substitute_id)) > 0:

			self.displayHelp(self.url, self.category_id, self.product_id, self.substitute_id)
			self.get_feature(self.product_id)
			self.select_substitute(self.substitute_id)

	def categegory(self):
		if self.event == 'r':
			self.url = 'main/categories'
			self.all_categories()
		if int(str(self.event)) > 0:
			self.url = 'main/categories/{0}/products/'
			self.product_id = self.event
			self.substitute_id = 0
			self.check_substitute()

	def all_favorite(self):
		self.favorite_id = self.event
		if self.event == 'r':
			self.url = 'main'
			self.main()
			self.event = 0
		if int(str(self.event)) > 0:
			self.product_id = self.event
			url = 'main/favorites/'
			self.displayHelp(self.url, product_id=self.favorite_id)
			self.select_feature_favorite(self.favorite_id)
			self.event = 0

	def favorite(self, event):
		self.event
		if self.event == 'r':
			self.url = 'main/favorites'
			self.board.favorite(self.url)
			self.event =0
		if self.event == 's':
			self.board.delete_favorite_id(self.product)
			self.event = 0
		if int(str(self.event)) > 0:
			pass
		self.event = 0


	def man_product1(self, category_id, product_id, substitute_id):
		self.category_id = category_id
		self.product_id = product_id
		self.substitute_id = substitute_id
		if self.event == 'r':
			self.url = 'main/categories/'
			self.displayHelp(self.url, self.category_id)
			self.get_product(self.category_id)
			self.event = 0
		if int(str(self.event)) > 0:
			self.url = 'main/categories/{0}/products/{1}/'
			self.substitute_id = self.event
			self.select_product(self.url, self.category_id,
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

	def main(self):

		self.event = 0
		self.home()
		while True:

			self.event = input("choix : ")

			if self.event == 'q':
				quit()

			if self.url == 'main':
				self.home()
				self.event = 0

			if self.url == 'main/categories':
				self.all_categories()
				self.event = 0
			
			if self.url == 'main/categories/':
				self.categegory()
				self.event = 0

			print(self.category_id)
			print(self.product_id)
			print(self.substitute_id)













