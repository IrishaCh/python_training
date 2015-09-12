# -*- coding: utf-8 -*-
from model.contact import Contact
import re


def test_add_contact(app, json_contacts):
    # fill combo-boxes ("комбобокс","число, месяц или группа")
    # value: 3  - 1 число, 2  - Январь месяц, 12 - 10 число, 3  - Февраль месяц, 1  - не принадлежит никакой группе
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(contact,
                            delete_photo=False,
                            dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1"))
                            )
    if len(old_contacts) + 1 != app.contact.count():
        app.contact.count()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # !!!
    contact.first_name = trim_space(contact.first_name)
    contact.last_name = trim_space(contact.last_name)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# функция удаляет пробелы в имени и фамилии, которые отсутствует на форме редактирования, но имеются на основной форме
def trim_space(text):
    text = re.sub(r'\s+', ' ', text).strip()
    return text
