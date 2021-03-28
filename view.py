# -*- coding: utf-8 -*-

import requests
from database import Data
from template import Interface
import tables
from controller import Controlboard

board = Controlboard(tables.TABLES)
display = Interface()
database = Data(tables.TABLES)


def main():

	category_id = 0
	product_id = 0
	substitute_id = 0
	url = 'main'

	board.main(url)
	
	while True:

			event = input("choix : ")

			if event == 'q':
				quit()

			if url == 'main':

				if event == '1':
					url = 'main/categories'
					board.categories(url)
					event = 0
				if event == '2':
					board.favorite()
					url = 'main/favorites'
					event = 0


			if url == 'main/favorites':
				if event == 'r':
					board.main()                      
				if int(str(event)) > 0:
					board.ctrl_feature_favorite(event)
					event = 0


			if url == 'main/favorites/details':
				if event == 'r':
					board.favorite()
				if event == 'm':
					pass
				if int(str(event)) > 0:
					pass
				event = 0


			if url == 'main/categories':
				if event == 'r':
					url = 'main'
					board.main(url)
					event = 0
				if int(str(event)) > 0:
					url = 'main/categories/'
					category_id = event
					board.products(url, category_id)
				event = 0


			if url == 'main/categories/':
				if event == 'r':
					url = 'main/categories'
					board.categories(url)
					event = 0
				if int(str(event)) > 0:
					url = 'main/categories/{0}products/'
					product_id = event
					substitute_id = 0
					board.select_product(url, category_id, product_id, substitute_id)
				event=0

			if url == 'main/categories/{0}products/':
				if event == 'r':
					url = 'main/categories/'
					board.products(url, category_id)
					event = 0
				if int(str(event)) > 0:
					url = 'main/categories/{0}/products/{1}/'
					substitute_id = event
					board.select_product(url, category_id, product_id, substitute_id)
				event = 0

			if url == 'main/categories/{0}/products/{1}/':
				if event == 'e':
					board.save(product_id, substitute_id)
					board.details(category_choice, product_choice, substitute)
				if event == 'r':
					url = 'main/categories/{0}products/'
					substitute_id = 0
					board.select_product(url, category_id, product_id, substitute_id)
				event=0


			event = 0

if __name__ == '__main__':
	main()


