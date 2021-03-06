# __author__ = 'Irina.Chegodaeva'
import re
from random import randrange
from fixture.db import *
import pytest
from fixture.orm import ORMFixture


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    list_items = db.get_contact_list()
    for item in list_items:
        print(item)
    index = len(list_items)
finally:
    pass


@pytest.mark.parametrize("contact", list_items, ids=[repr(x) for x in list_items])
def test_contact_on_home_page_compare_with_db(app, db, contact):
    count_contact = len(db.get_contact_list())
    contact_from_home_page = None
    contact_from_db = None
    if count_contact == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    index = int(contact.id)
    for l1 in app.contact.get_contact_list():
        if int(l1.id) == index:
            contact_from_home_page = l1
            break
    for l2 in db.get_contact_list():
        if int(l2.id) == index:
            contact_from_db = l2
            break
    #contact_from_db1 = filter(lambda x: int(x.id)==index, map(lambda y: y in x, db.get_contact_list()))
    #contact_from_db1 = filter(lambda x: x in db.get_contact_list(), filter(lambda y: int(y.id)==index, db.get_contact_list()))
    contact_from_db1 = filter(lambda x: int(x.id)==index, map(lambda x: x, db.get_contact_list()))
    contact_from_db1 = filter(lambda x: int(x.id)==index, db.get_contact_list())
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
    assert contact_from_home_page.company_address == trim_spaces(contact_from_db.company_address)
    assert contact_from_home_page.homepage == trim_spaces(contact_from_db.homepage)
    assert contact_from_home_page.company_url == contact_from_db.company_url
    assert contact_from_home_page.all_e_mails_from_home_page == merge_e_mails_like_on_home_page(contact_from_db)


# def test_contact_on_home_page_compare_with_db(app, db):
#     count_contact = len(db.get_contact_list())
#     if count_contact == 0:
#         app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
#                                 delete_photo=False,
#                                 dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
#     for id1 in range(0, count_contact):
#         contact_from_home_page = app.contact.get_contact_list()[id1]
#         contact_from_db = db.get_contact_list()[id1]
#         assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
#         assert contact_from_home_page.company_address == trim_spaces(contact_from_db.company_address)
#         assert contact_from_home_page.homepage == trim_spaces(contact_from_db.homepage)
#         assert contact_from_home_page.company_url == contact_from_db.company_url
#         assert contact_from_home_page.all_e_mails_from_home_page == merge_e_mails_like_on_home_page(contact_from_db)


def test_contact_on_home_page_compare_with_edit_page(app, db):
    count_contact = len(db.get_contact_list())
    if count_contact == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    index = randrange(count_contact)
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.company_address == trim_spaces(contact_from_edit_page.company_address)
    assert contact_from_home_page.homepage == trim_spaces(contact_from_edit_page.homepage)
    assert contact_from_home_page.company_url == contact_from_edit_page.company_url
    assert contact_from_home_page.all_e_mails_from_home_page == merge_e_mails_like_on_home_page(contact_from_edit_page)


def extract_numbers(phone_number):
    phone_number = re.sub("[() - .]", "", phone_number)
    return phone_number


def trim_space(text):
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: extract_numbers(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.extra_phone]))))


def merge_e_mails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   map(lambda x: trim_space(x),
                                       map(lambda x: x.strip(), [contact.email_1, contact.email_2, contact.email_3])))))


def trim_spaces(attribute):
    l = " ".join(map(lambda x: x.strip(), attribute.split("\n")))
    l = " ".join(filter(lambda x: x != "",
                        map(lambda x: x.strip(), l.split(" "))))
    return l
