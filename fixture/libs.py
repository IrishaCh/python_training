# __author__ = 'Irina.Chegodaeva'
from model.group import Group
from model.contact import Contact
import re
import datetime


class CommonLib:

    def __init__(self, app):
        self.app = app
        t = datetime.datetime.now()
        self.substring = "_" + t.strftime("%d%m%Y") + "_" + t.strftime("%H%M%S")

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_text_by_attribute_name(self, attr_name):
        wd = self.app.wd
        return wd.find_element_by_name(attr_name).get_attribute("value")

    def trim_space(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def clean_group(self, group):
        group = Group(id=group.id, name=self.trim_space(group.name))
        return group

    def clean_contact(self, contact):
        contact = Contact(id=contact.id,
                          first_name=self.trim_space(contact.first_name),
                          last_name=self.trim_space(contact.last_name),
                          middle_name=self.trim_space(contact.middle_name))
        return contact
