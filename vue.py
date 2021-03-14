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
	b.get_category()


main(b, c)