from __future__ import print_function
import mysql.connector

cnx = mysql.connector.connect(user='root', host='localhost',
	password='100ml80%vol.', port='330', database='person')
cursor = cnx.cursor()

add_contact = ("INSERT INTO contact"
	"(first_name, last_name, phone_number)"
	"VALUES('Antoine', 'Mathieu', '012345679')")

#insert new contact
cursor.execute(add_contact)
cnx.commit()
cursor.close()
cnx.close()