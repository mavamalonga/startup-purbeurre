import requests
import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
from mysql.connector import errorcode
import database
import api
import tables

def main():

	b = Database(tables.TABLES)
	b.create_database()
	b.create_table()

	c = get_data_api()
	c.load_data()
	c.insert_category()
	c.insert_data()


main()
