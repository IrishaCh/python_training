# __author__ = 'Irina.Chegodaeva'
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random
import pytest

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


# добавление первого попавшегося контакта в первую попавшуюся группу
def test_add_any_contact_in_any_group(app):
    if len(db.get_contact_list()) == 0:
        with pytest.allure.step('If there is no contact I will add a new one'):
            app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                    delete_photo=False,
                                    dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    if len(db.get_group_list()) == 0:
        with pytest.allure.step('If there is no group I will add a new one: Group(name="test")'):
            app.group.create(Group(name="test"))
    with pytest.allure.step('Given a random contact from the list and a random group from the list'):
        group = db.get_group_list()
        contact = random.choice(db.get_contact_list())
        group_index = random.choice(range(0, len(group)))
    with pytest.allure.step('Then the contact %s is including into the group %s' % (contact, group[group_index])):
        app.contact.add_contact_in_group(contact.id, group_index)


# добавление контакта в группу, если он не в этой группе
def test_add_contact_in_group_if_its_not_in_this_group(app):
    for i in range(0, 100):
        if len(db.get_group_list()) == 0:
            with pytest.allure.step('If there is no contact I will add a new one'):
                app.group.create(Group(name="test"))
        with pytest.allure.step('Given a random contact without group and a random group from the list'):
            group_index = random.choice(range(0, len(db.get_group_list())))
            group = db.get_group_list()[group_index]
            contact_list = db.get_contacts_not_in_group(group)
        if len(contact_list) == 0:
            with pytest.allure.step('If there is no contact I will add a new one'):
                app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                        delete_photo=False,
                                        dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
        contact = random.choice(db.get_contacts_not_in_group(group))
        with pytest.allure.step('Then I add the contact %s in the group %s' % (contact, group)):
            app.contact.add_contact_in_group(contact.id, group_index)
