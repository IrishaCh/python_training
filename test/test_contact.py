__author__ = 'Irina.Chegodaeva'
from model.contact import Contact
import re
from random import randrange


def test_contact_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                    delete_photo=False,
                                    dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.company_address == contact_from_edit_page.company_address
    assert contact_from_home_page.all_e_mails_from_home_page == merge_e_mails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.homepage == contact_from_edit_page.homepage


def extract_numbers(phone_number):
    phone_number = re.sub("[() -]", "", phone_number)
    return phone_number


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: extract_numbers(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.extra_phone]))))


def merge_e_mails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", [contact.email_1, contact.email_2, contact.email_3]))
