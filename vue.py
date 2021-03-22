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
	
		if event == 'q':
			quit()
		
		if menu == 'main':
			if event == '1':
				menu = 'category'
				Inter.display_help(menu)
				database.get_category()
				event = 0
			if event == '2':
				database.get_favorite()
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
			if event == 's':
				database.save_product()
	
				

		event = input("choix : ")


if __name__ == '__main__':
	main()


