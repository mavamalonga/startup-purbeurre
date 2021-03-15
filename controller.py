from database import Database
import tkinter as tk


class Interface:
	def __init__(self):
		self.tk = tk.Tk()
		self.frame = tk.Frame()
		self.mainloop = tk.mainloop()
		self.label = tk.Label()

	def menu1(self):

		self.text_m1 = self.label(master=self.frame, text="Menu prinicpal")
		


inter = Interface()
inter.menu1()




	


