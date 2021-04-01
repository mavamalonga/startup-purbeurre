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


if __name__ == '__main__':
	manager.main()


	


