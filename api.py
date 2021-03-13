import requests
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode

class get_data_api:
	def __init__(self):
		self.Id = mysql.connector.connect(user='root', host='localhost', password='100ml80%vol.', port='330')
		self.cursor = self.Id.cursor()
		self.cursor.execute("use Purbeurre")
		self.categories = ['Mueslis', 'Boissons', 'Pains de mie', 'Pâtes à tartiner']
		self.data_api = []

	def load_data(self):

		for i in self.categories:
			payload = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',
			'tag_0': "\'" + i + "\'", 'page_size': '1', 'json': 'true'}

			request = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)
			response = request.json()
			self.data_api.append(response)


	def insert_category(self):
		for elt, element in zip(self.categories, self.data_api):
				insert_category = ("""insert ignore category (categories)
									values({0})"""
										.format("\'"+elt+"\'"))

				self.cursor.execute(insert_category)
				self.Id.commit()

	def insert_data(self):
		self.num = 0
		for elt, element in zip(self.categories, self.data_api):

				for value in element['products']:

					self.num = self.num + 1

					product_name = "\'"+value['product_name_fr'].replace("'","")+"\'"
					brands = "\'"+value['brands'].replace("'", "")+"\'"
					category_id = elt
					ingredients_text = "\'"+value['ingredients_text'].replace("'","")+"\'"
					nutrition_grades = "\'"+','.join(value['nutrition_grades_tags'])+"\'"
					nutriments = "\'"+','.join(value['nutriments'])+"\'"
					quantity = "\'"+value['quantity']+"\'"
					store_tags = "\'"+",".join(value['stores_tags']).replace("'","")+"\'"
					link = "\'"+value['url'].replace("'","")+"\'"

					insert_food = ("""insert ignore into food (product_name, brands, category_id, 
						ingredients_text, nutrition_grades, nutriments, quantity, store, link)
						values({0}, {1}, (select id from category where categories = {2}), {3}, {4}, {5}, {6}, {7}, {8})""".format(product_name, brands, "\'"+elt+"\'", ingredients_text, nutrition_grades, nutriments, quantity, store_tags, link))
					self.cursor.execute(insert_food)
					self.Id.commit()
