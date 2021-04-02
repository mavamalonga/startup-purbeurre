# -*- coding: utf-8 -*-

import requests
from database import Data
from template import Interface
import tables
from controller import Controlboard
import windows 
from manager import Manager

board = Controlboard(tables.TABLES, windows.window_dict)
display = Interface(windows.window_dict)
database = Data(tables.TABLES, windows.window_dict)
manager = Manager(tables.TABLES, windows.window_dict)

def main():

	manager.category_id = 0
	manager.product_id = 0
	manager.substitute_id = 0
	manager.main()
	url = manager.url



	
	while True:

			event = input("choix : ")


			if event == 'q':
				quit()
			if manager.url == 'main':
				manager.man_main(event)
			
			if manager.url == 'main/favorites':
				manager.man_favorite1(event)


			if manager.url == 'main/favorites/':
				man_favorite2(event)


			if manager.url == 'main/categories':
				manager.man_categories1(event)

	
			if manager.url == 'main/categories/':
				manager.man_categories2(event)


			if manager.url == 'main/categories/{0}/products/':
				pass

			if manager.url == 'main/categories/{0}/products/{1}/':
				pass


			event = 0


if __name__ == '__main__':
	manager.main()


