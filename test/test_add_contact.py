# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    # fill combo-boxes ("комбобокс","число, месяц или группа")
    # value: 3  - 1 число, 2  - Январь месяц, 12 - 10 число, 3  - Февраль месяц, 1  - не принадлежит никакой группе
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_contact(contact,
                            delete_photo=False,
                            dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(app.libs.clean_contact, new_contacts), key=Contact.id_or_max) ==\
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
