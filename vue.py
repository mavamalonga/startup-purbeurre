import requests
from database import Database
from api import get_data_api
from controller import Interface
import tables


inter = Interface()
database = Database(tables.TABLES, inter)

def main():

	obj_interface = Interface()
	obj_interface.main_menu()
	menu = 'main_menu'
	event = 0

	while True:
		
		if event == '1' and (menu == 'main_menu'):
			database.get_category_list()
			menu = 'category_menu'
			event = 0
		if event == '1' and (menu == 'category_menu'):
			database.get_food_list(event)

		if event == 'q':
			quit()
		event = input("choix : ")

if __name__ == '__main__':
	main()