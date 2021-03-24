import requests
from database import Data
from api import get_data_api
from pynput import keyboard
from template import Interface
import tables
from controller import Controlboard

ctrl = Controlboard(tables.TABLES)
display = Interface()
database = Data(tables.TABLES)




def main():

	ctrl.ctrl_main()
	
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


			if ctrl.menu == 'favorie':
				if event == 'r':
					ctrl.ctrl_main()
					event = 0
				if event == 's':
					pass

				if int(str(event)) > 0:
					pass
					event = 0

			if ctrl.menu == 'category':
				if event == 'r':
					ctrl.ctrl_main()
					event = 0
				if int(str(event)) > 0:
					ctrl.ctrl_product(event)
					event = 0


			if ctrl.menu == 'product':
				if event == 'r':
					ctrl.ctrl_category()
					event = 0
				if int(str(event)) > 0:
					ctrl.ctrl_feature(event)
					event=0

			if ctrl.menu == 'feature':
				if event == 'r':
					ctrl.ctrl_product(ctrl.index)
					event=0
				if event == 'e':
					database.save_product()

			event = 0

if __name__ == '__main__':
	main()


