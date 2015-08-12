# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from contact import Contact
import unittest
import os


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_add_contact_form(self, wd):
        wd.find_element_by_link_text("add new").click()

    def choose_from_combo(self, wd, combo, value):
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[%s]//option[%s]" % (combo, value))\
                .is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[%s]//option[%s]" % (combo, value)).click()

    def fill_contacts_form(self, wd, contact):
        # filling initials
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # adding the photo
        wd.find_element_by_name("photo").send_keys(contact.pic)
        # employers' information
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.company_address)
        # phones
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        # e-mails and website
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # important dates
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniv_year)
        # address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.home_addr)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.extra_phone)

    def save_contact_form(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact_form(wd)
        self.fill_contacts_form(wd, Contact(first_name="First_Name",
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
                                            extra_phone="(999)111-11-55"))
        # fill combo-boxes
        self.choose_from_combo(wd, combo="1", value="3")   # 1 - комбо, 3  - 1 число
        self.choose_from_combo(wd, combo="2", value="2")   # 2 - комбо, 2  - Январь месяц
        self.choose_from_combo(wd, combo="3", value="12")  # 3 - комбо, 12 - 10 число
        self.choose_from_combo(wd, combo="4", value="3")   # 4 - комбо, 3  - Февраль месяц
        # fill the group
        self.choose_from_combo(wd, combo="5", value="1")   # 5 - комбо, 1  - не принадлежит никакой группе
        self.save_contact_form(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact_form(wd)
        self.fill_contacts_form(wd, Contact(first_name="",
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
                                            extra_phone=""))
        # fill combo-boxes: combo - № комбобокса, value - значение (1 - соответствует "не выбрано")
        for i in range(1, 6):
            self.choose_from_combo(wd, combo=str(i), value="1")   # 1 - комбо, 1  - число не выбрано
        self.save_contact_form(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
