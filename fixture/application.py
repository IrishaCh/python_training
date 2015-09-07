__author__ = 'Irina.Chegodaeva'
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.libs import CommonLib


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.libs = CommonLib(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if wd.current_url.endswith("addressbook/") and wd.find_element_by_link_text("Logout").is_displayed():
            wd.find_element_by_link_text("Logout").click()
        if not (wd.current_url.endswith("addressbook/") and wd.find_element_by_link_text("Create account").is_displayed()):
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
