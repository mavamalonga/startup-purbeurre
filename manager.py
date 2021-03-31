# -*- coding: utf-8 -*-

import template
import database
import tables
import windows

class Manager (database.Data):
	def __init__(self, table, windows_dict):
		super().__init__(table, windows_dict)

	def open_home(self):
		self.url = 'home'
		self.display_help(self.url)

	def home(self):
		try :
			if (self.event != 0) and int(self.event) == 1:
				self.url = 'all_categories'
				self.display_help(self.url)
				self.get_category()
			elif (self.event != 0) and int(self.event) == 2:
				self.url = 'all_favorites'
				self.display_help(self.url)
				self.get_favorite()
		except:
			print("Veillez rentrer une valeur valide.")
		
	def all_categories(self):
		try:
			if (self.event != 0) and self.event == 'r':
				self.open_home()
			elif (self.event != 0) and int(self.event) > 0:
				self.url = 'all_products'
				self.category_id = self.event
				self.display_help(self.url)
				self.get_product(self.category_id)
		except:
			print("Veillez rentrer une valeur valide.")


	def check_substitute(self):

		try:
			if (self.event != 0 ) and int(self.substitute_id) > 0:
				self.display_help(self.url)
				self.get_feature(self.product_id)
				self.select_substitute_list(self.category_id, self.product_id)
			elif (self.event != 0) and int(self.substitute_id) > 0:

				self.display_help(self.url)
				self.get_feature(self.product_id)
				self.select_substitute(self.substitute_id)
		except:
			print("Veillez rentrer une valeur valide.")

	def all_products(self):

		try: 
			if (self.event != 0) and self.event == 'r':
				self.url = 'all_categories'
				self.display_help(self.url)
				self.get_category()
			elif (self.event !=0) and int(self.event) > 0:
				self.url = 'product'
				self.product_id = self.event
				self.substitute_id = 0
				self.check_substitute()
		except: 
			print("Veillez rentrer une valeur valide.")


	def product(self):
		try:
			if (self.event != 0) and self.event == 'r':
				self.url = 'all_products'
				self.display_help(self.url)
				self.get_product(self.category_id)
				self.select_feature_favorite()
			elif (self.event != 0) and self.event > 0:
				self.url = 'product_substitute'
				self.substitute_id = self.event
				self.check_substitute()
		except:
			print("Veillez rentrer une valeur valide.")


	def product_substitute(self):
		try:
			if  (self.event != 0) and self.event == 'e':
				self.save_product(self.product_id, self.substitute_id)
			elif (self.even !=0) and self.event == 'r':
				self.url = 'product'
				self.substitute_id = 0
				self.check_substitute()
		except:
			print("Veillez rentrer une valeur valide.")

	def all_favorites(self):
		try:
			if self.event == 'r':
				self.url = 'open_home'
				self.open_home()
			elif int(self.event) > 0:
				self.favorite_id = self.event
				self.url = 'favorite'
				self.display_help(self.url)
				self.select_feature_favorite(self.favorite_id)
		except:
			print("Veillez rentrer une valeur valide.")

	def favorite(self):
		try:
			if self.event == 'r':
				self.url = 'all_favorites'
				self.display_help(self.url)
				self.get_favorite()
			elif self.event == 's':
				self.delete_favorite(self.favorite_id)
		except:
			print("Veillez rentrer une valeur valide.")
		

	def main(self):

		self.open_home()
		while True:

			self.event = input("choix : ")

			
			if self.event == 'q':
				quit()

			elif self.url == 'home':
				self.home()
				self.event = 0

			elif self.url == 'all_categories':
				self.all_categories()
				self.event = 0
			
			elif self.url == 'all_products':
				self.all_products()
				self.event = 0

			elif self.url == 'product':
				self.product()
				self.event = 0

			elif self.url == 'product_substitute':
				self.product_substitute()
				self.event = 0

			elif self.url == 'all_favorites':
				self.all_favorites()
				self.favorite_id = self.event
				self.event = 0

			elif self.url == 'favorite':
				self.favorite()
				self.event = 0








