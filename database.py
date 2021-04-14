# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
import tables
import template
import windows


class Data(template.Interface):

	def __init__(self, table, window_dict):
		super().__init__(window_dict)
		self.table = table

	def connectDatabase(self):
		
		with open('login.yml', 'r') as file:
			self.login = file.read().split()
		self.cnx = mysql.connector.connect(user=self.login[0], host=self.login[1],
		 password=self.login[2], port=self.login[3])
		self.cursor = self.cnx.cursor()
		self.cursor1 = self.cursor
		self.cursor2 = self.cursor
		self.cursor.execute("use Purbeurre")

	def createDatabase(self):
		try:
			self.connectDatabase()
			self.cursor.execute("create database Purbeurre default character set 'utf8'")
		except mysql.connector.Error as err:
			self.displayNotify("Failed creating database Purbeurre")
			exit(1)
		else:
			self.displayNotify("Success create database")

	def createTable(self):
		for table_name in self.table:
			table_description = self.table[table_name]
			try:
				self.connectDatabase()
				self.cursor.execute(table_description)
			except mysql.connector.Error as err:
				if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
					self.displayNotify("already exists.")
				else:
					print(err.msg)
			else:
				self.displayNotify("creating table {0}".format(table_name))
		self.cursor.close()

	def selectCategories(self):

		self.connectDatabase()
		self.categoriesList = []
		self.cursor.execute("call select_categories()")
		for categories in self.cursor:
			self.categoriesList.append(categories)

		if self.categoriesList[0][0] == 'empty':
			self.displayNotify('La liste de catégories est vide.')
		else:
			self.url = 'categoriesList'
			self.displayHelp(self.url)
			for category in self.categoriesList:
				self.displayCategories(category[0], category[1])

		self.cursor.close()

	def selectProductsList(self, categoryId):

		self.connectDatabase()
		self.productsList = []
		self.cursor.execute("call select_products_list({0})".format(categoryId))
		for products in self.cursor:
			self.productsList.append(products)

		if self.productsList[0][0] == 'empty':
				self.displayNotify('Veillez rentrer un numéro de catégorie valide.')
		else:
			self.url = 'productsList'
			self.displayHelp(self.url)
			for product in self.productsList:
 				self.displayProducts(product[0], product[1])
		self.cursor.close()

	def selectProductId(self, categoryId, productId, substitute=False):

		self.connectDatabase()
		self.featureList = []
		self.cursor.execute("call select_product_id ({0}, {1})".format(categoryId, productId))
		for feature in self.cursor:
			self.featureList.append(feature)
		if self.featureList[0][0] == 'empty':
			self.displayNotify('Veillez rentrer un numéro de produit valide.')
		else:
			if substitute == False:
				self.url = "product_and_substitutes"
			else:
				self.url = "product_and_substitute_one"

			self.displayHelp(self.url)
			for feature in self.featureList:
				self.displayProductId(feature[0], feature[1], feature[2], feature[3], 
					feature[4], feature[5], feature[6])

		self.cursor.close()

		if substitute == False:
			self.selectSubstituteList(categoryId, productId)
		else:
			pass


	def selectSubstituteList(self, categoryId, productId):

		self.connectDatabase()
		self.substitutes = []
		self.cursor.execute("call select_substitute_list({0}, {1})".format(categoryId, productId))
		for substitute in self.cursor:
			self.substitutes.append(substitute)

		if self.substitutes[0][0] == 'empty':
			self.displayNotify("Ce produit n''a pas encore de substitue dans la base.")
		else:
			for tuple_substitute in self.substitutes:
				self.displaySubstituteList(tuple_substitute[0], tuple_substitute[1], tuple_substitute[2])
		self.cursor.close()

	def selectSubstitute(self, category_id, product_id, substitute_id):

		self.connectDatabase()
		self.featureSubstitute = []
		self.cursor.execute("call select_substitute({0}, {1}, {2})".format(category_id, product_id, substitute_id))
		for feature in self.cursor:
			self.featureSubstitute.append(feature)

		if self.featureSubstitute[0][0] == 'empty':
			self.displayNotify("Veillez saisir un numéro valide.")
		else:
			self.url = "product_and_substitute_one"
			self.displayHelp(self.url)
			for feature in self.featureSubstitute:
				self.displayProductId(feature[0], feature[1], feature[2], feature[3], 
					feature[4], feature[5], feature[6])
				print(feature[0], feature[1], feature[2], feature[3], 
					feature[4], feature[5], feature[6])
		
		self.cursor.close()


	def insertProducts(self, productId, substituteId):

		self.connectDatabase()
		self.cursor.execute("call insert_products({0},{1}}".format(productId, substituteId))
		self.cnx.commit()
		for response in self.cursor:
			if response == 'duplicate':
				self.displayNotify("Ces produits ont déjà été ajoutés au favories.")
			else:
				self.displayNotify("Ajout validé !")
		self.cursor.close()

	def selectFavorites(self):

		self.products_1 = []
		self.products_2 = []

		self.connectDatabase()
		self.cursor.execute("call select_products_1()")
		for product_1 in self.cursor:
			self.products_1.append(product_1)
		self.cursor.close()

		self.connectDatabase()
		self.cursor.execute("call select_products_2()")
		for product_2 in self.cursor:
			self.products_2.append(product_2)
		self.cursor.close()

		if self.products_1[0][0] == 'empty' or self.products_2[0][0] == 'empty':
			self.displayNotify("La liste de favoiries est vide.")
		else:
			self.url = 'favoritesList'
			self.displayHelp(self.url)
			self.displayFavoriteList(self.products_1, self.products_2)
		self.cursor.close()
		
	def deleteFavorite(self, favoriteId):

		self.connectDatabase()
		self.cursor.execute("call delete_favorite({0})".format(favoriteId))
		self.cnx.commit()
		for response in self.cursor:
			if response[0] == 'empty':
				self.displayNotify("Le numéro choisit ne correpond à aucun favorie.")
			elif response[0] == 'success':
				self.displayNotify("Suppression du favorie {0}".format(favoriteId))
			else:
				self.displayNotify("Le numéro choisit ne correpond à aucun favorie.")
		self.cursor.close()


	def selectFavoriteFeature(self, favoriteId):

		self.favoriteFeatureList = []
		self.connectDatabase()
		self.cursor.execute("call display_feature_favorite({0})".format(favoriteId))
		for doubt_tuple in self.cursor:
			self.favoriteFeatureList.append(doubt_tuple)

		if self.favoriteFeatureList[0][0] == 'empty':
			self.displayNotify("Le numéro saisit correspond à aucun favorie.")
		else:
			self.url = 'displayfeaturefavorite'
			self.displayHelp(self.url)
			self.displayFeatureFavorite(self.favoriteFeatureList[0], self.favoriteFeatureList[1])
		self.cursor.close()






