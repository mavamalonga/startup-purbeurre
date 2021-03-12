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
		for elt, element in zip(self.categories, self.data_api):

				for value in element['products']:

					product_name = "\'"+value['product_name_fr'].replace("'","")+"\'"
					brands = "\'"+value['brands'].replace("'", "")+"\'"
					#description =
					ingredients_text = "\'"+value['ingredients_text'].replace("'","")+"\'"
					nutrition_grades = value['nutrition_grades_tags']
										#description = "\'"+value
					store_tags = "\'"+",".join(value['stores_tags']).replace("'","")+"\'"
					link = "\'"+value['url'].replace("'","")+"\'"

					print(nutrition_grades)


		

c = get_data_api()
c.load_data()
c.insert_category()
c.insert_data()
