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
        if (wd.current_url.endswith("addressbook/") and
                    len(wd.find_elements_by_xpath("//form[@class='header']//a[.='Logout']")) > 0):
            wd.find_element_by_xpath("//form[@class='header']//a[.='Logout']").click()
        if not (wd.current_url.endswith("addressbook/") and
                    len(wd.find_elements_by_xpath("//div[@id='content']//a[.='Create account']")) > 0):
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
