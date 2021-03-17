import requests
from database import Database
from api import get_data_api
from controller import Interface
import tables
import model


Obj_prd = model.Product()
Obj_cat = model.Category()
Obj_Fav = model.Favorite()
inter = Interface(Obj_prd, Obj_cat, Obj_Fav)


database = Database(tables.TABLES)

def main():


	inter.main_menu()
	menu = 'main_menu'
	event = 0

	while True:
		
		if menu == 'main_menu':
			if event == '1':
				database.get_category_list()
				menu = 'category_menu'
				event = 0

		if event == 'q':
			quit()
		event = input("choix : ")

if __name__ == '__main__':
	main()