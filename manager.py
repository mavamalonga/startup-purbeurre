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

	def dashboard(self):
		try :
			if int(self.event) == 1:
				self.url = 'all_categories'
				self.display_help(self.url)
				self.get_category()
			elif int(self.event) == 2:
				self.url = 'all_favorites'
				self.display_help(self.url)
				self.get_favorite()
			else: 
				self.displayError()
		except:
			self.displayError()
		
	def choiceCategory(self):
		try:
			if str(self.event) == 'r':
				self.home()
			elif int(self.event) > 0:
				self.category_id = self.event
				self.url = 'all_products'
				self.get_product(self.url, self.category_id)
		except:
			print("Veillez rentrer une valeur valide.")


    # method select list substitute or one substitute when substitute_id > 0

	def check_substitute(self):

		try:
			if int(self.substitute_id) == 0:
				self.display_help(self.url)
				self.get_feature(self.product_id)
				self.select_substitute_list(self.category_id, self.product_id)
			elif int(self.substitute_id) > 0:

				self.display_help(self.url)
				self.get_feature(self.product_id)
				self.select_substitute(self.substitute_id)
		except:
			print("Veillez rentrer une valeur valide.")

	def choiceProduct(self):

		try: 
			if str(self.event) == 'r':
				self.url = 'all_categories'
				self.display_help(self.url)
				self.get_category()
			elif int(self.event) > 0:
				self.url = 'product'
				self.product_id = self.event
				self.substitute_id = 0
				self.check_substitute()
		except: 
			print("Veillez rentrer une valeur valide.")


	def choiceSubstitute(self):
		try:
			if str(self.event) == 'r':
				self.url = 'all_products'
				self.display_help(self.url)
				self.get_product(self.url, self.category_id)
				self.select_feature_favorite()
			elif int(self.event) > 0:
				self.url = 'product_substitute'
				self.substitute_id = self.event
				self.check_substitute()
		except:
			print("Veillez rentrer une valeur valide.")


	def comparisonChart(self):
		try:

			if  str(self.event) == 'e':
				self.save_product(self.product_id, self.substitute_id)
			elif str(self.event) == 'r':
				self.url = 'product'
				self.substitute_id = 0
				self.check_substitute()
			else:
				print("Veillez rentrer une valeur valide.")

		except:
			print("Veillez rentrer une valeur valide.")

	def choiceFavorite(self):
		try:
			if str(self.event) == 'r':
				self.url = 'open_home'
				self.home()
			elif int(self.event) > 0:
				self.favorite_id = self.event
				self.url = 'favorite'
				self.display_help(self.url)
				self.select_feature_favorite(self.favorite_id)
		except:
			print("Veillez rentrer une valeur valide.")

	def comparisonChartFavorite(self):
		try:
			if self.event == 'r':
				self.url = 'all_favorites'
				self.display_help(self.url)
				self.get_favorite()
			elif self.event == 's':
				self.delete_favorite(self.favorite_id)
			elif int(self.event) != 0:
				print("Veillez rentrer une valeur valide.")
				
		except:
			print("Veillez rentrer une valeur valide.")
		

	def main(self):

		self.home()
		while True:

			self.event = input("choix : ")

			
			if self.event == 'q':
				quit()

			elif self.url == 'home':
				self.dashboard()
				self.event = 0

			elif self.url == 'all_categories':
				self.choiceCategory()
				self.event = 0
			
			elif self.url == 'all_products':
				self.choiceProduct()
				self.event = 0

			elif self.url == 'product':
				self.choiceSubstitute()
				self.event = 0

			elif self.url == 'product_substitute':
				self.comparisonChart()
				self.event = 0

			elif self.url == 'all_favorites':
				self.choiceFavorite()
				self.favorite_id = self.event
				self.event = 0

			elif self.url == 'favorite':
				self.comparisonChartFavorite()
				self.event = 0








