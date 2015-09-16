# -*- coding: utf-8 -*-
# __author__ = 'Irina.Chegodaeva'
from selenium.common.exceptions import *
from model.contact import Contact
import re
import urllib
import time


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        wd = self.app.wd
        # если страница не оканчивается на addressbook/ и на ней нет кнопки "send e-mail", то открыть основную страницу
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath(
                "//div[@id='content']/form[2]/div[1]/input")) > 0):
            wd.get("http://localhost/addressbook/")

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
            if contact.pic is not None:
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
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def find_element_by_xpath_cell_id_index(self, index):
        wd = self.app.wd
        return wd.find_element_by_css_selector("input[value='%s']" % index).click()

    # возможно не будет использоваться
    def find_cell_id_by_index_and_click(self, index):
        index += 2
        if not self.find_element_by_xpath_cell_id_index(index).is_selected():
            self.find_element_by_xpath_cell_id_index(index).click()

    def find_cell_id_by_id_and_click(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    # возможно не будет использоваться
    def find_cell_id_by_index_and_unclick(self, index):
        wd = self.app.wd
        index += 2
        if self.find_element_by_xpath_cell_id_index(index).is_selected():
            self.find_element_by_xpath_cell_id_index(index).click()

    # action = update - изменить, action = delete - удалить
    def submit_modifications_from_edit_form(self, action):
        wd = self.app.wd
        for element in wd.find_elements_by_name("update"):
            if element.get_attribute("value") == action:
                element.click()
                return

    # edit_detail: "edit_form" - из формы редактирование, "detail_form" - из формы просмотра деталей
    def modify_some_contact_by_id(self, id, contact, delete_photo, dataset, edit_detail):
        wd = self.app.wd
        self.open_main_page()
        # нашли элемент по индексу
        if edit_detail == "edit_form":
            self.open_contact_to_edit_by_id(id)
        else:
            self.open_contact_view_by_id(id)
            wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(contact, delete_photo)
        self.fill_combo_boxes(dataset, counter_combo=4)
        self.submit_modifications_from_edit_form("Update")
        self.contact_cache = None

    # возможно не будет использоваться
    def modify_some_contact(self, index, contact, delete_photo, dataset, edit_detail):
        wd = self.app.wd
        self.open_main_page()
        # нашли элемент по индексу
        if edit_detail == "edit_form":
            self.open_contact_to_edit_by_index(index)
        else:
            self.open_contact_view_by_index(index)
            wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(contact, delete_photo)
        self.fill_combo_boxes(dataset, counter_combo=4)
        self.submit_modifications_from_edit_form("Update")
        self.contact_cache = None

    def delete_some_contact_from_edit_form(self, index):
        self.open_main_page()
        # нашли строку по индексу
        self.open_contact_to_edit_by_index(index)
        # submit
        self.submit_modifications_from_edit_form("Delete")
        self.contact_cache = None

    def delete_some_contact_from_edit_form_by_id(self, id):
        self.open_main_page()
        # нашли строку по ид
        self.open_contact_to_edit_by_id(id)
        # submit
        self.submit_modifications_from_edit_form("Delete")
        self.contact_cache = None

    def button_delete_and_reaction(self, answer, is_checkbox_exists):
        # pressing delete and confirming deleting or not
        wd = self.app.wd
        wd.find_element_by_xpath("//div/div[4]/form[2]/div[2]/input").click()
        if wd.switch_to_alert():
            if answer == "N" and is_checkbox_exists:
                wd.switch_to_alert().dismiss()
            else:
                wd.switch_to_alert().accept()
        self.contact_cache = None

    # возможно не будет использоваться
    def delete_some_contact_or_all_by_index(self, index, answer, name_attr_for_deleting):
        wd = self.app.wd
        self.open_main_page()
        if name_attr_for_deleting == "selected[]":
            try:
                self.find_cell_id_by_index_and_click(index)
                is_checkbox_exists = True
            except (NoSuchElementException, UnexpectedAlertPresentException):
                is_checkbox_exists = False
        else:
            if not wd.find_element_by_id(name_attr_for_deleting).is_selected():
                wd.find_element_by_id(name_attr_for_deleting).click()
            is_checkbox_exists = True
        self.button_delete_and_reaction(answer, is_checkbox_exists)
        # снимаем галку на выбранном чекбоксе, если не подтвержадем удаление
        if answer == "N" and name_attr_for_deleting == "selected[]":
            self.find_cell_id_by_index_and_unclick(index)
        self.contact_cache = None

    def delete_some_contact_or_all_by_id(self, id, answer, name_attr_for_deleting):
        wd = self.app.wd
        self.open_main_page()
        if name_attr_for_deleting == "selected[]":
            try:
                self.find_cell_id_by_id_and_click(id)
                is_checkbox_exists = True
            except (NoSuchElementException, UnexpectedAlertPresentException):
                is_checkbox_exists = False
        else:
            if not wd.find_element_by_id(name_attr_for_deleting).is_selected():
                wd.find_element_by_id(name_attr_for_deleting).click()
            is_checkbox_exists = True
        self.button_delete_and_reaction(answer, is_checkbox_exists)
        # снимаем галку на выбранном чекбоксе, если не подтвержадем удаление
        if answer == "N" and name_attr_for_deleting == "selected[]":
            self.find_cell_id_by_id_and_click(id)
        # нужен быстрый commit
        self.open_main_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_main_page()
            self.contact_cache = []
            # найдем все записи о контактах. ничего умнее пока в голову так и не пришло
            # в итоге сделала, как у инструктора
            for row in wd.find_elements_by_name("entry"):
                value_cell = row.find_elements_by_tag_name("td")
                # найдем id каждой записи
                id = value_cell[0].find_element_by_tag_name("input").get_attribute("value")
                l_name = value_cell[1].text
                f_name = value_cell[2].text
                address = value_cell[3].text
                all_e_mails = value_cell[4].text
                all_phones = value_cell[5].text
                try:
                    company_url = value_cell[9].find_element_by_tag_name("a").get_attribute("href")
                except NoSuchElementException:
                    company_url = ""
                try:
                    homepage = value_cell[10].find_element_by_tag_name("img").get_attribute("title")
                except NoSuchElementException:
                    homepage = ""
                self.contact_cache.append(Contact(last_name=l_name, first_name=f_name, company_address=address,
                                                  all_e_mails_from_home_page=all_e_mails, homepage=homepage, id=id,
                                                  all_phones_from_home_page=all_phones, company_url=company_url))
        return list(self.contact_cache)

    # возможно, не будет использоваться
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_main_page()
        for row in wd.find_elements_by_name("entry"):
            try:
                row.find_element_by_css_selector("input[value='%s']" % id)
                cell = row.find_elements_by_tag_name("td")[7]
                cell.find_element_by_tag_name("a").click()
                break
            except NoSuchElementException:
                pass

    # возможно не будет использоваться
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_id(self, id):
        wd = self.app.wd
        self.open_main_page()
        for row in wd.find_elements_by_name("entry"):
            try:
                row.find_element_by_css_selector("input[value='%s']" % id)
                cell = row.find_elements_by_tag_name("td")[6]
                cell.find_element_by_tag_name("a").click()
                break
            except NoSuchElementException:
                pass

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = self.app.libs.get_text_by_attribute_name("firstname")
        last_name = self.app.libs.get_text_by_attribute_name("lastname")
        address = self.app.libs.get_text_by_attribute_name("address")
        id = self.app.libs.get_text_by_attribute_name("id")
        kind_emails = ["email", "email2", "email3"]
        emails = []
        for elem in kind_emails:
            emails.append(self.app.libs.get_text_by_attribute_name(elem))
        email_1 = emails[0]
        email_2 = emails[1]
        email_3 = emails[2]
        homepage = self.app.libs.get_text_by_attribute_name("homepage")
        kind_phones = ["home", "mobile", "work", "phone2"]
        phones = []
        for elem in kind_phones:
            phones.append(self.app.libs.get_text_by_attribute_name(elem))
        home_phone = phones[0]
        mobile_phone = phones[1]
        work_phone = phones[2]
        extra_phone = phones[3]
        # декодируем url адреса компании
        if address != "":
            substring_url = urllib.parse.quote_plus(address.strip(), safe='\n', encoding=None, errors=None)
            company_url = "http://maps.google.com/maps?q=%s&t=h" % substring_url.replace('\n', '%2C+')
        else:
            company_url = ""
        # убираем в каждой строке адреса компании лидирующие и завершающие пробелы
        return Contact(first_name=first_name, last_name=last_name, company_address=address, id=id, home_phone=home_phone,
                       work_phone=work_phone, mobile_phone=mobile_phone, extra_phone=extra_phone, email_1=email_1,
                       email_2=email_2, email_3=email_3, homepage=homepage, company_url=company_url)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        prefixes = ["H", "M", "W", "P"]
        phones = []
        if text != "":
            for i in range(0, len(prefixes)):
                prefixes[i] += ": (.*)"
                try:
                    s = re.search(prefixes[i], text)
                    if s is not None:
                        s = s.group(1)
                    else:
                        s = ""
                except AttributeError:
                    s = ""
                phones.append(s)
            home_phone = phones[0]
            mobile_phone = phones[1]
            work_phone = phones[2]
            extra_phone = phones[3]
        else:
            home_phone = ""
            work_phone = ""
            mobile_phone = ""
            extra_phone = ""
        all_phones = str(home_phone + mobile_phone + work_phone + extra_phone)
        return Contact(home_phone=home_phone, work_phone=work_phone, mobile_phone=mobile_phone, extra_phone=extra_phone,
                       all_phones_from_home_page=all_phones)
