from database import Database
import tables
import tkinter as tk



class Interface:

	def __init__(self, database):
		self.root = tk.Tk()
		self.database = database

	def menu1(self):
		self.text_m1 = "sélectionner une cotégorie d'aliments"
		self.button_m1 = tk.Button(self.root, text=self.text_m1, command= lambda:self.database.get_category_list())
		self.button_m1.pack()

		self.button_m12 = tk.Button(self.root, text="Retrouver mes aliments substitués")
		self.button_m12.pack()

		self.button_m13 = tk.Button(self.root, text="Quitter")
		self.button_m13.pack()

		self.root.mainloop()






if __name__ == '__inter__':
	database = Database(tables.TABLES)
	inter = Interface(database)
	inter.menu1()





	


