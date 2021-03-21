import requests
from database import Database
from api import get_data_api
from pynput import keyboard
from controller import Interface
import tables
import model


Obj_prd = model.Product()
Obj_cat = model.Category()
Obj_Fav = model.Favorite()
Inter = Interface()

database = Database(tables.TABLES)


def main():


	menu = 'main'
	Inter.display_help(menu)
	event = 0

	while True:
		
		if menu == 'main':
			if event == '1':
				menu = 'category'
				Inter.display_help(menu)
				database.get_category_list()
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
				database.get_product_list(event)
				ind = event
				event = 0
		if menu == 'product':
			if event == 'r':
				menu = 'category'
				Inter.display_help(menu)
				database.get_category_list()
				event = 0
			if int(str(event)) > 0:
				menu = 'value'
				Inter.display_help(menu)
				database.get_product(event)
				id_product = event
				event=0
		if menu == 'value':
			if event == 'r':
				menu = 'product'
				Inter.display_help('product')
				database.get_product_list(ind)
				event=0
			if event == 's':
				database.save_product_favorite()
	
				

		if event == 'q':
			quit()
		event = input("choix : ")


if __name__ == '__main__':
	main()