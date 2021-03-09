import requests

class get_data_api:
	def __init__(self):
		self.categories = ['Mueslis', 'Boissons', 'Pains de mie', 'Pâtes à tartiner']
		self.data_api = []

	def load_data(self):

		for i in self.categories:
			payload = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',
			'tag_0': "\'" + i + "\'", 'page_size': '1', 'json': 'true'}

			request = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)
			response = request.json()
			self.data_api.append(response)
			print(self.data_api[0])


'''
c = get_data_api()
c.load_data()
