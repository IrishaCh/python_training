__author__ = 'Irina.Chegodaeva'
import os
from model.contact import Contact
from random import randrange


def test_edit_some_contact_from_edit_form(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(last_name="test" + app.libs.substring),
                                    delete_photo=False,
                                    dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
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
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_some_contact(index, contact, delete_photo=True,
                                                dataset=(("1", "3"), ("2", "3"), ("3", "14"), ("4", "3")), edit_detail="edit_form")
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_some_contact_from_details(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(last_name="test" + app.libs.substring),
                                    delete_photo=False,
                                    dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    contact = Contact(first_name="First_Name" + app.libs.substring,
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
                        extra_phone="(999)111-11-55"
                     )
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_some_contact(index, contact, delete_photo=True,
                                                dataset=(("1", "3"), ("2", "3"), ("3", "14"), ("4", "4")), edit_detail="detail_form")
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
