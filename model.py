class Food:

	def __init__(self, product_id=None, product_name=None, brands=None, category_id=None, ingredients_text=None, 
		nutrition_grades=None, nutriments=None, quantity=None, store=None, link=None):
		self.product_id = product_id
		self.product_name = product_name
		self.brands = brands
		self.category_id = category_id
		self.ingredients_text = ingredients_text
		self.nutrition_grades = nutrition_grades
		self.nutriments = nutriments
		self.quantity = qauntity
		self.store = store
		self.link = link 


class Category:

	def __init__(self, categories_id=None, categories_name=None):
		self.category_id = category_id
		self.categories_name = categories_name


class Favorite:

	def __init__(self, favorite_id=None, id_food=None, id_substitute=None):
		self.favorite_id = favorite_id
		self.product_id = product_id
		self.substitute_id = substitute_id

