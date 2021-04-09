# -*- coding: utf-8 -*-
import template
import database
import tables
import windows

class Manager (database.Data):
	def __init__(self, table, windows_dict):
		super().__init__(table, windows_dict)
		self.errorValue = "errorValue"


	def home(self):
		self.url = 'home'
		self.displayHelp(self.url)


	def dashboard(self):
		try:
			if self.event == '1':
				self.url = 'categoriesList'
				self.displayHelp(self.url)
				self.get_category()
			elif self.event == '2':
				self.url = 'favoritesList'
				self.displayHelp(self.url)
				self.get_favorite()
			else:
				self.bad_value = 1/0
		except :
			self.displayNotify(self.errorValue)
		print(self.event)
		self.event = 0

	def choiceCategory(self):
		try:
			if self.event == 'r':
				self.home()
			elif int(str(self.event)) > 0:
				self.url = 'productsList'
				self.category_id = self.event
				self.displayHelp(self.url)
				self.get_product(self.category_id)
				print(self.url)
			else:
				self.bad_value = 1/0
		except :
			self.displayNotify(self.errorValue)
		self.event = 0


	def checkSubstitute(self):

		try:
			if int(str(self.substitute_id)) == 0:
				self.displayHelp(self.url)
				self.get_feature(self.product_id)
				self.select_substitute_list(self.category_id, self.product_id)
			elif int(str(self.substitute_id)) > 0:

				self.displayHelp(self.url)
				self.get_feature(self.product_id)
				self.select_substitute(self.substitute_id)
			else:
				self.bad_value = 1/0
		except :
			self.displayNotify(self.errorValue)
		self.event = 0

	def choiceProduct(self):

		try:
			if self.event == 'r':
				self.url = 'categoriesList'
				self.displayHelp(self.url)
				self.get_category()
			elif int(str(self.event)) > 0:
				self.url = 'productListSubstitute'
				self.displayHelp(self.url)
				self.product_id = self.event
				self.substitute_id = 0
				self.checkSubstitute()
			else:
				self.bad_value = 1/0
		except :
			self.displayNotify(self.errorValue)
		self.event = 0

	def choiceSubstitute(self):
		try :
			if self.event == 'r':
				self.url = 'productsList'
				self.displayHelp(self.url)
				self.get_product(self.category_id)
				self.event = 0
			elif int(str(self.event)) > 0:
				self.url = 'productSubstitute'
				self.displayHelp(self.url)
				self.substitute_id = self.event
				self.checkSubstitute()
			else :
				self.bad_value = 1/0
		except :
			self.displayNotify(self.errorValue)
		self.event = 0

	def choiceSave(self):
		try :
			if  self.event == 'e':
				self.save_product(self.product_id, self.substitute_id)
			elif self.event == 'r':
				self.url = 'productListSubstitute'
				self.substitute_id = 0
				self.checkSubstitute()
			else:
				self.bad_value = 1/0
		except :
			self.displayNotify(self.errorValue)
		self.event = 0


	def choiceFavorite(self):
		try :
			if self.event == 'r':
				self.url = 'home'
				self.home()
			elif int(self.event) > 0:
				self.url = 'displayFavorite'
				self.favorite_id = self.event                 
				self.displayHelp(self.url)
				self.select_feature_favorite(self.favorite_id)
			else :
				self.bad_value = 1/0
		except :
			self.displayNotify(self.errorValue)
		self.event = 0

	def choiceDelete(self):
		try :
			if self.event == 's':
				self.url = 'displayFavorite'
				self.delete_favorite(self.favorite_id)         
			elif self.event == 'r':
				self.url = 'favoritesList'
				self.get_favorite()
			else :
				self.bad_value = 1/0
		except :
			self.displayNotify(self.errorValue)
		self.event = 0

	def main(self):

		self.home()

		while True:

			self.event = input("choix : ")

			if self.event == 'q':
				quit()

			elif self.url == 'home':
				self.dashboard()
				self.event = 0

			elif self.url == 'categoriesList':
				self.choiceCategory()
				self.event = 0
			
			elif self.url == 'productsList':
				self.choiceProduct()
				self.event = 0

			elif self.url == 'productListSubstitute':
				self.choiceSubstitute()
				self.event = 0

			elif self.url == 'productSubstitute':
				self.choiceSave()
				self.event = 0

			elif self.url == 'favoritesList':
				self.choiceFavorite()
				self.event = 0

			elif self.url == 'displayFavorite':
				self.choiceDelete()
				self.event = 0