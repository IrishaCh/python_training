# __author__ = 'Irina.Chegodaeva'

import random
import string
import os.path
import jsonpickle
import sys
import getopt
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def e_mail(fname, lname, domain):
    s = fname + "." + lname + "@" + domain[11:]
    return s


firstname = random_string("first_name", 10)
lastname = random_string("last_name", 20)
homepage = "http://www.homepage.net"
e_mail_1 = e_mail(firstname, lastname, homepage)
testdata = [Contact(first_name="",
                    middle_name="",
                    last_name="",
                    nickname="",
                    pic="",
                    title="",
                    company_name="",
                    company_address="",
                    home_phone="",
                    mobile_phone="",
                    work_phone="",
                    fax="",
                    email_1="",
                    email_2="",
                    email_3="",
                    homepage="",
                    birth_year="",
                    anniv_year="",
                    home_addr="",
                    notes="",
                    extra_phone="")] + [
    Contact(first_name=firstname,
            middle_name=random_string("middle_name", 20),
            last_name=lastname,
            nickname=random_string("nickname", 10),
            pic=str(os.path.dirname(__file__)) + "/photo.gif",
            title=random_string("title", 10),
            company_name=random_string("company_name", 10),
            company_address=random_string("company_address", 10),
            home_phone=random_string("home_phone", 10),
            mobile_phone=random_string("mobile_phone", 10),
            work_phone=random_string("work_phone", 10),
            fax=random_string("fax", 10),
            homepage=homepage,
            email_1=e_mail_1,
            email_2=random_string("email_2", 10),
            email_3="email_3@company.com",
            birth_year=random_string("birth_year", 10),
            anniv_year=random_string("anniv_year", 10),
            home_addr=random_string("home_addr", 10),
            notes=random_string("notes", 10),
            extra_phone=random_string("extra_phone", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as output_file:
    jsonpickle.set_encoder_options("json", indent=2)
    output_file.write(jsonpickle.encode(testdata))
