# __author__ = 'Irina.Chegodaeva'
from model.contact import Contact
import re
import pytest


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        with pytest.allure.step('If there is no contact I will add a new one'):
            app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                    delete_photo=False,
                                    dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    with pytest.allure.step('Given a contact from home page'):
        contact_from_home_page = app.contact.get_contact_list()[0]
    with pytest.allure.step('Given a contact from edit page'):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    with pytest.allure.step('Then the phone list from homepage is equal to the phone list from edit page'):
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    with pytest.allure.step('Given a contact from view page'):
        contact_from_view_page = app.contact.get_contact_from_view_page(0)
    with pytest.allure.step('Given a contact from edit page'):
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    with pytest.allure.step('Then the phone list from homepage is equal to the phone list from edit page'):
        assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)


def extract_numbers(phone_number):
    phone_number = re.sub("[() -]", "", phone_number)
    return phone_number


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: extract_numbers(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.extra_phone]))))
