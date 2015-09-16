# __author__ = 'irina.chegodaeva'
import mysql.connector


connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("select * from addressbook where deprecated is null")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()