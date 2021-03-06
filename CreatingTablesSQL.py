from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

"""
# Indetifiants d'accès à la base de données       commentary
config = {
'host': 'localhost', 
'user': 'root', 
'password': '100ml80%vol.', 
'port': '330'
}
"""

DB_NAME = 'person'

# instruction création de table clients
TABLES = {}
TABLES['contact'] = (
"CREATE TABLE contact ("
	"  id int(3) NOT NULL AUTO_INCREMENT,"
	"  first_name varchar(14) NOT NULL,"
	"  last_name varchar(16) NOT NULL,"
	"  phone_number bigint(10) NOT NULL,"
	" PRIMARY KEY (id)"
	")ENGINE=innoDB")


cnx = mysql.connector.connect(user='root', password='100ml80%vol.',
	host='localhost', port='330')
cursor = cnx.cursor()




def create_database(cursor):
	try:
		cursor.execute(
			"CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
	except mysql.connector.ERROR as err:
		print("Failed create database: {}".format(err))
		exit(1)



try:
	cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
	print("Database {} does not exists.".format(DB_NAME))
	if err.errno == errorcode.ER_BAD_DB_ERROR:
		create_database(cursor)
		print("Database {} created successfully.".format(DB_NAME))
		cnx.database = DB_NAME
	else:
		print(err)
		exit(1)

for table_name, table_description in TABLES.items():
	try:
		print("Creating table {}: ".format(table_name), end='')
		cursor.execute(table_description)
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
			print("already exists.")
		else: 
			print(err.msg)
	else:
		print("OK")

cursor.close()
cnx.close()



