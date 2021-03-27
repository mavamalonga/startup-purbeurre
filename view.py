# -*- coding: utf-8 -*-

import requests
from database import Data
from template import Interface
import tables
from controller import Controlboard

ctrl = Controlboard(tables.TABLES)
display = Interface()
database = Data(tables.TABLES)


def main():

	ctrl.ctrl_main()

	category_choice = 0
	product_choice = 0
	substitute = 0
	
	while True:

			event = input("choix : ")

			if event == 'q':
				quit()

			if ctrl.menu == 'main':
				if event == 'r':
					print("Veillez rentrer une valeur correspondant aux choix.")
				if event == '1':
					ctrl.ctrl_category()
					event = 0
				if event == '2':
					ctrl.ctrl_favorite()
					event = 0


			if ctrl.menu == 'favorite':
				if event == 'r':
					ctrl.ctrl_main()
					event = 0
				if int(str(event)) > 0:
					ctrl.ctrl_feature_favorite(event)
					event = 0
			if ctrl.menu == 'feature_favorite':
				if event == 'r':
					ctrl.ctrl_favorite()
					event = 0



				if int(str(event)) > 0:
					pass
					event = 0

			if ctrl.menu == 'category':
				if event == 'r':
					ctrl.ctrl_main()
					event = 0
				if int(str(event)) > 0:
					category_choice = event
					ctrl.ctrl_product(event)
					event = 0


			if ctrl.menu == 'product':
				if event == 'r':
					ctrl.ctrl_category()
					event = 0
				if int(str(event)) > 0:
					product_choice = event
					substitute = 0
					ctrl.ctrl_feature(category_choice, product_choice, substitute)
					event=0

			if ctrl.menu == 'feature':
				if event == 'r':
					ctrl.ctrl_product(ctrl.index)
					event=0
				if int(str(event)) > 0:
					substitute = event
					ctrl.ctrl_feature(category_choice, product_choice, substitute)

			if ctrl.menu == 'comparison':
				if event == 'e':
					ctrl.ctrl_save(product_choice, substitute)
				if event == 'r':
					substitute = 0
					ctrl.ctrl_feature(category_choice, product_choice, substitute)
					event = 0


			print(category_choice)
			print(product_choice)
			print(substitute)
			print(ctrl.menu)
			print(event)




			event = 0

if __name__ == '__main__':
	main()


