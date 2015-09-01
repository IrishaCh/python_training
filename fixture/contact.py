__author__ = 'Irina.Chegodaeva'
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        wd = self.app.wd
        # если страница не оканчивается на и на ней нет кнопки "send e-mail", то открыть основную страницу
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
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    # возможно в дальнейшем не будет использоваться
    def modify_contact_from_edit_form(self, contact, delete_photo, dataset):
        self.modify_some_contact_from_edit_form(0, contact, delete_photo, dataset)

    def find_cell_id_by_index(self, index, cell_id):
        wd = self.app.wd
        index += 2
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[%s]/a/img" % (index, cell_id)).click()

    def submit_modifications_from_edit_form(self, sform, sinput):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[%s]/input[%s]" % (sform, sinput)).click()

    def modify_some_contact_from_edit_form(self, index, contact, delete_photo, dataset):
        wd = self.app.wd
        self.open_main_page()
        # нашли элемент по индексу
        self.find_cell_id_by_index(index, 8)
        self.fill_contact_form(contact, delete_photo)
        self.fill_combo_boxes(dataset, counter_combo=4)
        # submit
        self.submit_modifications_from_edit_form(1, 22)
        self.contact_cache = None

    # возможно в дальнейшем не будет использоваться
    def modify_contact_from_detail_form(self, contact, delete_photo, dataset):
        self.modify_some_contact_from_detail_form(0, contact, delete_photo, dataset)

    def modify_some_contact_from_detail_form(self, index, contact, delete_photo, dataset):
        wd = self.app.wd
        self.open_main_page()
        # нашли элемент по индексу
        self.find_cell_id_by_index(index, 7)
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(contact, delete_photo)
        self.fill_combo_boxes(dataset, counter_combo=4)
        # submit
        self.submit_modifications_from_edit_form(1, 22)
        self.contact_cache = None

    # возможно в дальнейшем не будет использоваться
    def delete_contact_from_edit_form(self):
        self.delete_some_contact_from_edit_form(0)

    def delete_some_contact_from_edit_form(self, index):
        wd = self.app.wd
        self.open_main_page()
        # нашли элемент по индексу
        self.find_cell_id_by_index(index, 8)
        # submit
        self.submit_modifications_from_edit_form(2, 2)
        self.contact_cache = None

    # возможно в дальнейшем не будет использоваться
    def button_delete_and_reaction(self, answer, is_checkbox_exists):
        self.button_delete_and_reaction_by_index(0, answer, is_checkbox_exists)

    def button_delete_and_reaction_by_index(self, index, answer, is_checkbox_exists):
        # pressing delete and confirming deleting or not
        wd = self.app.wd
        wd.find_elements_by_xpath("//div[@id='content']/form[2]/div[2]/input")[index].click()
        if wd.switch_to_alert():
            if answer == "N" and is_checkbox_exists:
                wd.switch_to_alert().dismiss()
            else:
                wd.switch_to_alert().accept()
        self.contact_cache = None

    # возможно в дальнейшем не будет использоваться
    def delete_first_or_all(self, answer, name_attr_for_deleting):
        self.delete_some_contact_or_all(0, answer, name_attr_for_deleting)

    def delete_some_contact_or_all(self, index, answer, name_attr_for_deleting):
        wd = self.app.wd
        self.open_main_page()
        if name_attr_for_deleting == "selected[]":
            function_for_find = wd.find_element_by_name
        else:
            function_for_find = wd.find_element_by_id
        try:
            # checkbox exists
            if not function_for_find(name_attr_for_deleting).is_selected():
                function_for_find(name_attr_for_deleting).click()
            is_checkbox_exists = True
        except (NoSuchElementException, UnexpectedAlertPresentException):
            # checkbox does not exist
            is_checkbox_exists = False
        self.button_delete_and_reaction(index, answer, is_checkbox_exists)

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
            i = 2
            # найдем все записи о контактах. ничего умнее пока в голову так и не пришло
            for element in wd.find_elements_by_name("selected[]"):
                try:
                    # найдем id каждой записи
                    id = element.get_attribute("value")
                    # по i - найдем номер строки в талице, из которой вытащим текст 2-го и 3-го столбцов
                    value_cell = []
                    for c in range(2, 4):
                        value_cell.append(wd.find_element_by_xpath("//div/div[4]/form[2]/table/tbody/tr[%s]/td[%s]"
                                                                   % (i, c)).text)
                    l_name = str(value_cell[0])
                    f_name = str(value_cell[1])
                    self.contact_cache.append(Contact(last_name=l_name, first_name=f_name, id=id))
                    i += 1
                except NoSuchElementException:
                    pass
        return list(self.contact_cache)
