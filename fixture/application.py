__author__ = 'Irina.Chegodaeva'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.libs import CommonLib


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.libs = CommonLib(self)

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
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
