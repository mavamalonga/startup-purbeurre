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

	# create new window tkinter
	window = tk.Tk()
	text="Menu principal"

	#label widget for write text
	menu1 = tk.Label(text=text)
	#applied widget in window
	menu1.pack()

	textb1 = "Sélectinner une catégorie d'aliments"
	button1 = tk.Button(text=textb1)
	button1.pack()

	textb2 = "Retrouver mes aliments substitués"
	button2 = tk.Button(text=textb2)
	button2.pack()

	textb3 = "Quitter"
	button3 = tk.Button(text=textb3)
	button3.pack()

	#executed events tkinter
	window.mainloop()


if __name__ == '__main__':
	main(b, c)