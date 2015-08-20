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

    def fill_contact_form(self, contact, delete_photo):
        wd = self.app.wd
        # filling initials
        self.app.libs.change_field_value("firstname", contact.first_name)
        self.app.libs.change_field_value("middlename", contact.middle_name)
        self.app.libs.change_field_value("lastname", contact.last_name)
        self.app.libs.change_field_value("nickname", contact.nickname)
        if delete_photo:
            # deleting photo
            if not wd.find_element_by_name("delete_photo").is_selected():
                wd.find_element_by_name("delete_photo").click()
        else:
            # adding the photo
            wd.find_element_by_name("photo").send_keys(contact.pic)
        # employers' information
        self.app.libs.change_field_value("title", contact.title)
        self.app.libs.change_field_value("company", contact.company_name)
        self.app.libs.change_field_value("address", contact.company_address)
        # phones
        self.app.libs.change_field_value("home", contact.home_phone)
        self.app.libs.change_field_value("mobile", contact.mobile_phone)
        self.app.libs.change_field_value("work", contact.work_phone)
        self.app.libs.change_field_value("fax", contact.fax)
        # e-mails and website
        self.app.libs.change_field_value("email", contact.email_1)
        self.app.libs.change_field_value("email2", contact.email_2)
        self.app.libs.change_field_value("email3", contact.email_3)
        self.app.libs.change_field_value("homepage", contact.homepage)
        # important dates
        self.app.libs.change_field_value("byear", contact.birth_year)
        self.app.libs.change_field_value("ayear", contact.anniv_year)
        # address
        self.app.libs.change_field_value("address2", contact.home_addr)
        self.app.libs.change_field_value("notes", contact.notes)
        self.app.libs.change_field_value("phone2", contact.extra_phone)

    def choose_from_combo(self, combo, value):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[%s]//option[%s]" % (combo, value))\
                .is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[%s]//option[%s]" % (combo, value)).click()

    def fill_combo_boxes(self, dataset, counter_combo):
        for i in range(0, counter_combo):
            (combo, value) = dataset[i]
            self.choose_from_combo(combo, value)  # 1 - комбо, 3  - 1 число

    def add_contact(self, contact, delete_photo, dataset):
        wd = self.app.wd
        self.open_add_contact_form()
        self.fill_contact_form(contact, delete_photo)
        self.fill_combo_boxes(dataset, counter_combo=5)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def modify_contact_from_edit_form(self, contact, delete_photo, dataset):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_contact_form(contact, delete_photo)
        self.fill_combo_boxes(dataset, counter_combo=4)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def modify_contact_from_detail_form(self, contact, delete_photo, dataset):
        wd = self.app.wd
        # editing contact from detail_form
        wd.find_element_by_css_selector("img[alt=\"Details\"]").click()
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(contact, delete_photo)
        self.fill_combo_boxes(dataset, counter_combo=4)
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def delete_contact_from_edit_form(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # submit
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()

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
