import mysql.connector

cnx = mysql.connector.connect(user='root', host='localhost', 
	password='100ml80%vol.', port='330', database='person')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, phone_number FROM contact")

cursor.execute(query)

# get values
for (first_name, last_name, phone_number) in cursor:
	print("{} {}, phone number : {}".format(
	first_name, last_name, phone_number))

cursor.close()
cnx.close()

