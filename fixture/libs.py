__author__ = 'Irina.Chegodaeva'
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
