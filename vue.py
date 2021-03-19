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
		if menu == 'category':
			if event == 'r':
				menu = 'main'
				Inter.display_help(menu)
				event = 0
			if event == '1':
				menu = 'product'
				Inter.display_help(menu)
				database.get_product_list(event)
				event = 0
				ind = event
		if menu == 'product':
			if event == 'r':
				database.get_category_list()
				menu = 'category'
			if event == '1':
				menu = 'value'
				Inter.display_help(menu)
				database.get_product(event)
				event=0
		if menu == 'value':
			if event == 'r':
				menu == 'product'
				database.get_product_list('1')

		if event == 'q':
			quit()
		event = input("choix : ")

if __name__ == '__main__':
	main()