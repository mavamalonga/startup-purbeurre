# -*- coding: utf-8 -*-

import requests
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode

class ApiOPFF:
	def __init__(self):
		self.categoriesList = ['Mueslis', 'Boissons', 'Desserts', 'Fruits', 'Viandes', 'Fromages']
		self.responseApi = []
		
	def connectDatabase(self):

		with open('loginData.yml', 'r') as file:
			self.login = file.read().split()
		self.cnx = mysql.connector.connect(user=self.login[0], host=self.login[1],
		 password=self.login[2], port=self.login[3])
		self.cursor = self.cnx.cursor()
		self.cursor.execute("use Purbeurre")

	def loginData(self):

		for categoryName in self.categories:
			payload = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',
			'tag_0': "\'" + categoryName + "\'", 'page_size': '1', 'json': 'true'}
			request = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)
			response = request.json()
			self.responseApi.append(response)


	def insertCategories(self):

		connectDatabase()
		for elt in self.categories:
				insertCategories = ("""insert ignore category (categories)
									values({0})"""
										.format("\'"+elt+"\'"))
				self.cursor.execute(insertCategories)
				self.cnx.commit()
				self.cursor.close()

	def insertFeatures(self):

		connectDatabase()
		for categoryName, element in zip(self.categories, self.responseApi):
				for value in element['products']:
	
					product_name = "\'"+value['product_name_fr'].replace("'","")+"\'"
					brands = "\'"+value['brands'].replace("'", "")+"\'"
					category_id = elt
					ingredients_text = "\'"+value['ingredients_text'].replace("'","")+"\'"
					nutrition_grades = "\'"+','.join(value['nutrition_grades_tags'])+"\'"
					nutriments = "\'"+','.join(value['nutriments'])+"\'"
					quantity = "\'"+value['quantity']+"\'"
					store_tags = "\'"+",".join(value['stores_tags']).replace("'","")+"\'"
					link = "\'"+value['url'].replace("'","")+"\'"

					insertProduct = ("""insert ignore into Product (product_name, brands, category_id, 
						ingredients_text, nutrition_grades, nutriments, quantity, store, link)
						values({0}, {1}, (select id from category where categories = {2}), {3}, {4}, {5}, {6}, {7}, {8})""".format(
							product_name, brands, "\'"+ categoryName +"\'", ingredients_text, nutrition_grades, nutriments,
							 quantity, store_tags, link))

					self.cursor.execute(insertProduct)
					self.cnx.commit()
		self.cursor.close()

	
	def main(self):
		loginData()
		insertCategories()
		insertFeatures()
