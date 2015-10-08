# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest


def test_add_contact(app, db, json_contacts, check_ui):
    # fill combo-boxes ("комбобокс","число, месяц или группа")
    # value: 3  - 1 число, 2  - Январь месяц, 12 - 10 число, 3  - Февраль месяц, 1  - не принадлежит никакой группе
    with pytest.allure.step('Given a contact list from json'):
        contact = json_contacts
    with pytest.allure.step('Given a contact list before add'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('When I add a contact %s to the list' % contact):
        app.contact.add_contact(contact,
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    with pytest.allure.step('Then the new contact list is equal to the old list with the edit contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(map(app.libs.clean_contact, new_contacts), key=Contact.id_or_max) ==\
                   sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
