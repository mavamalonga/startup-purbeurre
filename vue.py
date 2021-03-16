import requests
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
from database import Database
from api import get_data_api
import tables
from controller import Interface
import tkinter as tk 

database = Database(tables.TABLES)
interface = Interface(database)

def main():

	interface.menu1()

	while True:
		event = input("choix : ")
		if event == '2':
			print("OK")


if __name__ == '__main__':
	main()