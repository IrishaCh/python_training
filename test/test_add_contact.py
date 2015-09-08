# -*- coding: utf-8 -*-
import os
from model.contact import Contact
import pytest
import string
import random
import re


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + """string.punctuation""" + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="",
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
                    extra_phone="")] + [
    Contact(#name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20)
            first_name=random_string("first_name", 10),
            middle_name=random_string("middle_name", 20),
            last_name=random_string("last_name", 20),
            nickname=random_string("nickname", 10),
            pic=str(os.path.dirname(__file__)) + "\\photo.gif",
            title=random_string("title", 10),
            company_name=random_string("company_name", 10),
            company_address=random_string("company_address", 10),
            home_phone=random_string("home_phone", 10),
            mobile_phone=random_string("mobile_phone", 10),
            work_phone=random_string("work_phone", 10),
            fax=random_string("fax", 10),
            email_1=random_string("email_1", 10),
            email_2=random_string("email_2", 10),
            email_3="email_3@company.com",
            homepage="http://www.homepage.net",
            birth_year=random_string("birth_year", 10),
            anniv_year=random_string("anniv_year", 10),
            home_addr=random_string("home_addr", 10),
            notes=random_string("notes", 10),
            extra_phone=random_string("extra_phone", 10))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    # fill combo-boxes ("комбобокс","число, месяц или группа")
    # value: 3  - 1 число, 2  - Январь месяц, 12 - 10 число, 3  - Февраль месяц, 1  - не принадлежит никакой группе
    old_contacts = app.contact.get_contact_list()
    # contact = Contact(first_name="First_Name",
    #                   middle_name="Middle_Name",
    #                   last_name="Last_Name",
    #                   nickname="Nickname",
    #                   pic=str(os.path.dirname(__file__)) + "\\photo.gif",
    #                   title="Title",
    #                   company_name="Company Name",
    #                   company_address="Company Address",
    #                   home_phone="(999)111-11-11",
    #                   mobile_phone="(999)111-11-22",
    #                   work_phone="(999)111-11-33",
    #                   fax="(999)111-11-44",
    #                   email_1="email_1@company.com",
    #                   email_2="email_2@company.com",
    #                   email_3="email_3@company.com",
    #                   homepage="http://www.homepage.net",
    #                   birth_year="1970",
    #                   anniv_year="1990",
    #                   home_addr="Home Address",
    #                   notes="Some Notes",
    #                   extra_phone="(999)111-11-55")
    app.contact.add_contact(contact,
                            delete_photo=False,
                            dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1"))
                            )
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    # !!!
    contact.first_name = trim_space(contact.first_name)
    contact.last_name = trim_space(contact.last_name)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def trim_spaces(attribute):
    l = [(p.first_name.strip(), p.first_name.strip) for p in attribute]

    return l

def trim_space(text):
    text = re.sub(r'\s+', ' ', text).strip()
    return text