import requests
from database import Database
from api import get_data_api
from pynput import keyboard
from controller import Interface
import tables


Inter = Interface()

database = Database(tables.TABLES)


def main():


	menu = 'main'
	Inter.display_help(menu)
	event = 0

	while True:

			event = input("choix : ")

			if event != 'r' and event != 'q' and int(str(event)) == str:
				print("erreur")

			if event == 'q':
				quit()

			if menu == 'main':
				if event == 'r':
					print("Veillez rentrer une valeur correspondant aux choix.")
				if event == '1':
					menu = 'category'
					Inter.display_help(menu)
					database.get_category()
					event = 0
				if event == '2':
					menu = 'favorite'
					Inter.display_help(menu)
					database.get_favorite()
					event = 0
			if menu == 'favorite':
				if event == 's':
					pass
				if int(str(event)) > 0:
					menu = 'favorite'
					Inter.display_help(menu)
					database.focus_favorite(event)
					event = 0

			if menu == 'category':
				if event == 'r':
					menu = 'main'
					Inter.display_help(menu)
					event = 0
				if int(str(event)) > 0:
					menu = 'product'
					Inter.display_help(menu)
					database.get_product(event)
					ind = event
					event = 0
			if menu == 'product':
				if event == 'r':
					menu = 'category'
					Inter.display_help(menu)
					database.get_category()
					event = 0
				if int(str(event)) > 0:
					menu = 'feature'
					Inter.display_help(menu)
					database.get_feature(event)
					id_product = event
					event=0
			if menu == 'feature':
				if event == 'r':
					menu = 'product'
					Inter.display_help('product')
					database.get_product(ind)
					event=0
				if event == 'e':
					database.save_product()


if __name__ == '__main__':
	main()


