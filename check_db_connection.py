# __author__ = 'irina.chegodaeva'
from fixture.orm import ORMFixture
from model.group import Group
import mysql.connector


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
try:

    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
    l = db.get_contacts_not_in_group(Group(id="171"))
    for item in l:
        print(item)
    print(len(l))
finally:
    connection.close()
    pass
