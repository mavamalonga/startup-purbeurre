import template
import database
import tables

class Controlboard (database.Data):
	def __init__(self, table):
		super().__init__(table)

	def ctrl_main(self):
		self.menu = 'main'
		self.display_help(self.menu)
		return self.menu

	def ctrl_category(self):
		self.menu = 'categorie'
		self.display_help(self.menu)
		self.get_category()
		return self.menu

	def ctrl_favorite(self):
		self.menu = 'Favorie'
		self.display_help(self.menu)
		self.get_favorite()
		return self.menu

	def ctrl_product(self, event):
		self.event = event
		self.menu = 'product'
		self.display_help(self.menu)
		self.get_product(self.event)
		return self.menu

	def ctrl_feature(self, event):
		self.event = event 
		self.menu = 'feature'
		self.display_help(self.menu)
		self.get_feature(self.event)
		return self.menu

	def ctrl_save(self):
		self.display_help(self.menu)
		self.save_product()
