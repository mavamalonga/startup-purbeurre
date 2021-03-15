import requests
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
from database import Database
from api import get_data_api
import tables
from controller import interface
import tkinter as tk 

b = Database(tables.TABLES)
c = get_data_api()

def main(Database, api):

	def category():
		print("category")

	# create new window tkinter
	window = tk.Tk()

	frame_first_m = tk.Frame()

	text="Menu principal"

	#label widget for write text
	menu1 = tk.Label(master=frame_first_m, text=text)
	#applied widget in window
	menu1.pack()

	textb1 = "Sélectinner une catégorie d'aliments"
	button1 = tk.Button(master=frame_first_m, text=textb1, command=category )
	button1.pack()

	textb2 = "Retrouver mes aliments substitués"
	button2 = tk.Button(master=frame_first_m, text=textb2)
	button2.pack()

	textb3 = "Quitter"
	button3 = tk.Button(master=frame_first_m, text=textb3)
	button3.pack()

	frame_first_m.pack()

	window.mainloop()

	events_list = []

	#executed events tkinter
	window.mainloop()


if __name__ == '__main__':
	main(b, c)