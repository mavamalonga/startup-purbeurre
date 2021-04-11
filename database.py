# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
import tables
import tkinter as tk
import template
import windows


class Data(template.Interface):

	def __init__(self, table, window_dict):
		super().__init__(window_dict)
		self.table = table
		self.msg = "			successful recording"

	def connect_database(self):
		with open('login.yml', 'r') as file:
			self.login = file.read().split()
		self.cnx = mysql.connector.connect(user=self.login[0], host=self.login[1],
		 password=self.login[2], port=self.login[3])
		self.cursor = self.cnx.cursor()
		self.cursor.execute("use Purbeurre")

	def create_database(self):
		try:
			self.connect_database()
			self.cursor.execute("create database Purbeurre default character set 'utf8'")
		except mysql.connector.Error as err:
			print("Failed creating database Purbeurre")
			exit(1)

	def create_table(self):
		for table_name in self.table:
			table_description = self.table[table_name]
			try:
				self.connect_database()
				print("creating table {}:".format(table_name))
				self.cursor.execute(table_description)
			except mysql.connector.Error as err:
				if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
					print("already exists.")
				else:
					print(err.msg)
			else:
				print("OK")
		self.cursor.close()

	def selectCategories(self):

		self.connect_database()
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
				self.displayList(category[0], category[1])

		self.cursor.close()

	def selectProductsList(self, categoryId):

		self.connect_database()
		self.productsList = []
		self.categoryId = categoryId
		self.cursor.execute("call select_products_list({0})".format(self.categoryId))
		for products in self.cursor:
			self.productsList.append(products)

		if self.productsList[0][0] == 'empty':
				self.displayNotify('Veillez rentrer un numéro de catégorie valide.')
		else:
			self.url = 'productsList'
			self.displayHelp(self.url)
			for products in self.productsList:
 				self.displayList(products[0], products[1])
		self.cursor.close()

	def selectProductId(self, categoryId, productId):

		self.connect_database()
		self.featureList = []
		self.cursor.execute("call select_product_id ({0}, {1})".format(categoryId, productId))
		for feature in self.cursor:
			self.featureList.append(feature)

		if self.featureList[0][0] == 'empty':
			self.displayNotify('Veillez rentrer un numéro de produit valide.')
		else:
			self.url = 'productListSubstitute'
			self.displayHelp(self.url)
			self.displayProductId(self.featureList)
		self.cursor.close()
		self.selectSubstituteList(self.category_id, self.product_id)


	def selectSubstituteList(self, categoryId, productId):

		self.connect_database()
		self.substituteList = []
		self.cursor.execute("call select_substitute_list({0}, {1})".format(categoryId, productId))
		for substitute in self.cursor:
			self.substituteList.append(substitute)

		if self.substituteList[0][0] == 'empty':
			self.displayNotify("Ce produit n''a pas encore de substitue dans la base.")
		else:
			for substitute in self.substituteList:
				self.displayList(substitute[0], substitute[1], value3=substitute[2])
		self.cursor.close()

	def selectSubstitute(self, category_id, product_id, substitute_id):

		self.connect_database()
		self.featureSubstituteList = []
		self.cursor.execute("call select_substitute({0}, {1}, {2})".format(category_id, product_id, substitute_id))
		for feature in self.cursor:
			self.featureSubstituteList.append(feature)

		if self.featureSubstituteList[0][0] == 'empty':
			self.displayNotify("Veillez saisir un numéro valide.")
			self.displayProductId(feature)
		self.cursor.close()


	def insertProducts(self, productId, substituteId):
		self.connect_database()
		self.cursor.execute("call insert_products({0},{1}}".format(productId, substituteId))
		self.cnx.commit()
		self.cursor.close()
		self.displayNotify(self.msg)

	def selectFavorites(self):

		self.ids_names_list = []

		self.connect_database()
		self.cursor.execute("call select_favorites()")
		for response_tuple in self.cursor:
			self.ids_names_list.append(response_tuple)

		if self.ids_names_list[0][0] == 'empty':
			self.displayNotify("La liste de favoiries est vide.")
		else:
			self.url = 'favoritesList'
			self.displayHelp(self.url)
			self.displayFavoriteList(self.ids_names_list)

		self.cursor.close()
		
	def deletFavorite(self, favoriteId):
		self.connect_database()
		self.cursor.execute("call delete_favorite({0})".format(favoriteId))
		for response in self.cursor:
			if response[0] == 'empty':
				self.displayNotify("Le numéro choisit ne correpond à aucun favorie.")
			else:
				self.displayNotify("Suppression du favorie {0}".format(favoriteId))
		self.cnx.commit()
		self.cursor.close()


	def selectFavoriteFeature(self, favoriteId):
		self.favoriteFeatureList = []
		self.connect_database()
		self.cursor.execute("call display_feature_favorite({0})".format(favoriteId))
		for doubt_tuple in self.cursor:
			self.favoriteFeatureList.append(doubt_tuple)

		if self.favoriteFeatureList[0][0] == 'empty':
			self.displayNotify("Le numéro saisit correspond à aucun favorie.")
		else:
			for doubt_tuple in self.favoriteFeatureList:
				self.url = 'displayfeaturefavorite'
				self.displayHelp(self.url)
				self.display_feature_favorite(doubt_tuple)
		self.cursor.close()

		




