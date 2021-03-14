import requests
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
from database import Database
from api import get_data_api
import tables

b = Database(tables.TABLES)
c = get_data_api()

def main(Database, api):

	b.create_database()
	b.create_table()

	c.load_data()
	c.insert_category()
	c.insert_data()


main(b, c)
