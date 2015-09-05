# -*- coding: utf-8 -*-
import os
from model.contact import Contact


def test_add_contact(app):
    # fill combo-boxes ("комбобокс","число, месяц или группа")
    # value: 3  - 1 число, 2  - Январь месяц, 12 - 10 число, 3  - Февраль месяц, 1  - не принадлежит никакой группе
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="First_Name",
                      middle_name="Middle_Name",
                      last_name="Last_Name",
                      nickname="Nickname",
                      pic=str(os.path.dirname(__file__)) + "\\photo.gif",
                      title="Title",
                      company_name="Company Name",
                      company_address="Company Address",
                      home_phone="(999)111-11-11",
                      mobile_phone="(999)111-11-22",
                      work_phone="(999)111-11-33",
                      fax="(999)111-11-44",
                      email_1="email_1@company.com",
                      email_2="email_2@company.com",
                      email_3="email_3@company.com",
                      homepage="http://www.homepage.net",
                      birth_year="1970",
                      anniv_year="1990",
                      home_addr="Home Address",
                      notes="Some Notes",
                      extra_phone="(999)111-11-55")
    app.contact.add_contact(contact,
                            delete_photo=False,
                            dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1"))
                            )
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="",
                      middle_name="",
                      last_name="",
                      nickname="",
                      pic="",
                      title="",
                      company_name="",
                      company_address="",
                      home_phone="",
                      mobile_phone="",
                      work_phone="",
                      fax="",
                      email_1="",
                      email_2="",
                      email_3="",
                      homepage="",
                      birth_year="",
                      anniv_year="",
                      home_addr="",
                      notes="",
                      extra_phone=""
                      )
    app.contact.add_contact(contact,
                            delete_photo=False,
                            dataset=(("1", "1"), ("2", "1"), ("3", "1"), ("4", "1"), ("5", "1"))
                            )
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
