import template
import database

class Controller(template.Interface, database.Database):
	def __init__(self):
		super().__init__()

	def ctrl_category(self):
		self.menu = 'categorie'
		self.display_help(self.menu)
		self.get_category()
		return self.menu

	def ctrl_favorite(self, event):
		self.event = event
		self.menu = 'favorie'
		self.display_help(self.menu)
		self.get_favorite(self.event)
		return self.menu

	def ctrl_product(self, event):
		self.event = event
		self.menu = 'product'
		self.display_help(self.menu)
		self.get_product(self.event)

	def ctrl_feature(self, event):
		










