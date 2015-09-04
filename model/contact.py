__author__ = 'Irina.Chegodaeva'
from sys import maxsize
import re


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, pic=None, title=None,
                 company_name=None, company_address=None, home_phone=None, mobile_phone=None, work_phone=None,
                 fax=None, email_1=None, email_2=None, email_3=None, homepage=None, birth_year=None, anniv_year=None,
                 home_addr=None, notes=None, extra_phone=None, id=None, all_phones_from_home_page=None,
                 all_e_mails_from_home_page=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.pic = pic
        self.title = title
        self.company_name = company_name
        self.company_address = company_address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.birth_year = birth_year
        self.anniv_year = anniv_year
        self.home_addr = home_addr
        self.notes = notes
        self.extra_phone = extra_phone
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_e_mails_from_home_page = all_e_mails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.last_name, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.last_name == other.last_name and self.first_name == other.first_name #and \
               #self.all_phones_from_home_page == other.all_phones_from_home_page #and \
               #re.match(other.first_3_phones, self.first_3_phones) is not None

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
