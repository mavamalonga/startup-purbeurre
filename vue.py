import requests
from database import Database
from api import get_data_api
from controller import Interface
import tables
import model


Obj_prd = model.Product()
Obj_cat = model.Category()
Obj_Fav = model.Favorite()
Inter = Interface()


database = Database(tables.TABLES, Inter)

def main():


	Inter.main_menu()
	menu = 'main_menu'
	event = 0

	while True:
		
		if menu == 'main_menu':
			if event == '1':
				database.get_category_list()
				menu = 'category_menu'
				event = 0
		if menu == 'category_menu' and event != 0:
			if event == 'r':
				menu = 'main_menu'
				Inter.main_menu()
				event = 0
			if event == '1':
				database.get_product_list(event)
				ind_product = event
				menu = 'product_menu'
				event = 0
		if menu == 'product_menu':
			if event == 'r':
				database.get_category_list()
				menu = 'category_menu'

		if event == 'q':
			quit()
		event = input("choix : ")

if __name__ == '__main__':
	main()