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
		self.displayHelp(self.url)

	def dashboard(self):
		try :
			if int(self.event) == 1:
				self.url = 'all_categories'
				self.displayHelp(self.url)
				self.selectCategories()
			elif int(self.event) == 2:
				self.url = 'all_favorites'
				self.displayHelp(self.url)
				self.selectFavorites()
			else: 
				errorValue = 1/0
		except:
			self.displayError()
		
	def choiceCategory(self):
		try:
			if str(self.event) == 'r':
				self.home()
			elif int(self.event) > 0:
				self.category_id = self.event
				self.url = 'all_products'
				self.selectProducts(self.url, self.category_id)
			else:
				errorValue = 1/0
		except:
			self.displayError()


    # method select list substitute or one substitute when substitute_id > 0

	def check_substitute(self):

		try:
			if int(self.substitute_id) == 0:
				self.displayHelp(self.url)
				self.selectProductId(self.product_id)
				self.selectSubstituteList(self.category_id, self.product_id)
			elif int(self.substitute_id) > 0:

				self.displayHelp(self.url)
				self.selectProductId(self.product_id)
				self.selectSubstituteId(self.substitute_id)
			else:
				errorValue = 1/0
		except:
			self.displayError()

	def choiceProduct(self):

		try: 
			if str(self.event) == 'r':
				self.url = 'all_categories'
				self.displayHelp(self.url)
				self.selectCategories()
			elif int(self.event) > 0:
				self.url = 'product'
				self.product_id = self.event
				self.substitute_id = 0
				self.checkSubstitute()
		except: 
			print("Veillez rentrer une valeur valide.")


	def choiceSubstitute(self):
		try:
			if str(self.event) == 'r':
				self.url = 'all_products'
				self.displayHelp(self.url)
				self.selectProducts(self.url, self.category_id)
				self.select_feature_favorite()
			elif int(self.event) > 0:
				self.url = 'product_substitute'
				self.substitute_id = self.event
				self.checkSubstitute()
			else:
				errorValue = 1/0
		except:
			self.displayError()


	def comparisonChart(self):
		try:

			if  str(self.event) == 'e':
				self.save(self.product_id, self.substitute_id)
			elif str(self.event) == 'r':
				self.url = 'product'
				self.substitute_id = 0
				self.checkSubstitute()
			else:
				errorValue = 1/0

		except:
			self.displayError()

	def choiceFavorite(self):
		try:
			if str(self.event) == 'r':
				self.url = 'open_home'
				self.home()
			elif int(self.event) > 0:
				self.favorite_id = self.event
				self.url = 'favorite'
				self.displayHelp(self.url)
				self.select_feature_favorite(self.favorite_id)
			else:
				errorValue = 1/0

		except:
			self.displayError()

	def comparisonChartFavorite(self):
		try:
			if self.event == 'r':
				self.url = 'all_favorites'
				self.displayHelp(self.url)
				self.selectFavorites()
			elif self.event == 's':
				self.deleteFavoriteId(self.favorite_id)
			else
				errorValue = 1/0
				
		except:
			self.displayError()

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








####for debug