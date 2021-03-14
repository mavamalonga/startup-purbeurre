import requests
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
from database import Database
from api import get_data_api
import tables
from controller import interface

b = Database(tables.TABLES)
c = get_data_api()
control = interface()

def main(Database, api):
	control.menu()



main(b, c)