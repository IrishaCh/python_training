# __author__ = 'Irina.Chegodaeva'
import os
from model.contact import Contact
import random
import pytest


def test_edit_some_contact_from_edit_form(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        with pytest.allure.step('If there is no contact I will add a new one'):
            app.contact.add_contact(Contact(last_name="test" + app.libs.substring),
                                    delete_photo=False,
                                    dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    contact = Contact(first_name="First_Name",
                      middle_name="Middle_Name",
                      last_name="Last_Name" + app.libs.substring,
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
    with pytest.allure.step('Given a contact list before edit'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Given a random contact from the list for edit'):
        modified_contact = random.choice(old_contacts)
    with pytest.allure.step('I modified the contact'):
        app.contact.modify_some_contact_by_id(modified_contact.id, contact, delete_photo=True,
                                              dataset=(("1", "3"), ("2", "3"), ("3", "14"), ("4", "3")),
                                              edit_detail="edit_form")
    with pytest.allure.step('Given a contact list after edit'):
        new_contacts = db.get_contact_list()
    with pytest.allure.step('Then the length of the new contact list is equal to the length of the old list'):
        assert len(old_contacts) == len(new_contacts)
    with pytest.allure.step('The modified contact was changed in the old list'):
        contact.id = modified_contact.id
        old_contacts.remove(modified_contact)
        old_contacts.insert(int(modified_contact.id), contact)
    with pytest.allure.step('Then the new contact list is equal to the old list with the edit contact'):
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(map(app.libs.clean_contact, new_contacts), key=Contact.id_or_max) ==\
                   sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_edit_some_contact_from_details(app, db):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(last_name="test" + app.libs.substring),
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    contact = Contact(first_name="First_Name" + app.libs.substring,
                      middle_name="Middle_Name",
                      last_name="Last_Name" + app.libs.substring,
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
    old_contacts = db.get_contact_list()
    modified_contact = random.choice(old_contacts)
    app.contact.modify_some_contact_by_id(modified_contact.id, contact, delete_photo=True,
                                          dataset=(("1", "3"), ("2", "3"), ("3", "14"), ("4", "4")),
                                          edit_detail="detail_form")
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    contact.id = modified_contact.id
    old_contacts.remove(modified_contact)
    old_contacts.insert(int(modified_contact.id), contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
