__author__ = 'Irina.Chegodaeva'
from model.contact import Contact
import re


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                    delete_photo=False,
                                    dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    l = merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    s = merge_phones_like_on_home_page(contact_from_view_page)
    l = merge_phones_like_on_home_page(contact_from_edit_page)
    ss = re.match(contact_from_edit_page.first_3_phones, contact_from_view_page.first_3_phones)
    rr = re.search(contact_from_edit_page.first_3_phones, contact_from_view_page.first_3_phones)
    #assert re.match(contact_from_edit_page.all_phones_from_home_page, contact_from_view_page.all_content) is not None
    #assert contact_from_view_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)# and \
           #re.match(contact_from_edit_page.first_3_phones, contact_from_view_page.first_3_phones) is not None

def extract_numbers(phone_number):
    phone_number = re.sub("[() -]", "", phone_number)
    return phone_number

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: extract_numbers(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.extra_phone]))))
