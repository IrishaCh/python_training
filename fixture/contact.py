__author__ = 'Irina.Chegodaeva'
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
import time


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_form(self, contact, delete_photo, is_new):
        wd = self.app.wd
        # if new contact: open page "add new", if editing: stay on current page and click Edit
        if is_new == 1:
            # adding new contact
            self.open_add_contact_form()
        elif is_new <= 0:
            # editing contact from edit_form = 0, deleting contact from edit_form = -1
            wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
            # redefining name of the group
            contact.last_name = contact.last_name + str(self.app.postfix.substring)
        elif is_new == 2:
            # editing contact from detail_form
            wd.find_element_by_css_selector("img[alt=\"Details\"]").click()
            time.sleep(10)
            wd.find_element_by_name("modifiy").click()
            time.sleep(10)
            # redefining name of the group
            contact.last_name = contact.last_name + str(self.app.postfix.substring)
            contact.first_name = contact.first_name + str(self.app.postfix.substring)
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
        if delete_photo == 1:
            # deleting photo
            if not wd.find_element_by_name("delete_photo").is_selected():
                wd.find_element_by_name("delete_photo").click()
        else:
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

    def choose_from_combo(self, combo, value):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[%s]//option[%s]" % (combo, value))\
                .is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[%s]//option[%s]" % (combo, value)).click()

    def save_contact_form(self, is_new):
        wd = self.app.wd
        if is_new == 1:
            name_path = "//div[@id='content']/form/input[21]"
        elif is_new == 0:
            name_path = "//div[@id='content']/form[1]/input[22]"
        elif is_new == -1:
            name_path = "//div[@id='content']/form[2]/input[2]"
        wd.find_element_by_xpath(name_path).click()

    def button_delete_and_reaction(self, answer, is_checkbox_exists):
        # pressing delete and confirming deleting or not
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        if wd.switch_to_alert():
            if answer == "N" and is_checkbox_exists:
                wd.switch_to_alert().dismiss()
            else:
                wd.switch_to_alert().accept()

    def delete_first_or_all(self, answer, name_attr_for_deleting):
        wd = self.app.wd
        if name_attr_for_deleting == "selected[]":
            function_for_find = wd.find_element_by_name
        else:
            function_for_find = wd.find_element_by_id
        try:
            # checkbox exists
            if not function_for_find(name_attr_for_deleting).is_selected():
                function_for_find(name_attr_for_deleting).click()
            is_checkbox_exists = True
            self.button_delete_and_reaction(answer, is_checkbox_exists)
        except (NoSuchElementException, UnexpectedAlertPresentException):
            # checkbox not exists
            is_checkbox_exists = False
            self.button_delete_and_reaction(answer, is_checkbox_exists)
