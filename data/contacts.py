# __author__ = 'irina.chegodaeva'
from model.contact import Contact
import os


testdata = [Contact(first_name="First_Name",
                    middle_name="Middle_Name1",
                    last_name="Last_Name1",
                    nickname="Nickname1",
                    pic=str(os.path.dirname(__file__)) + "\\photo.gif",
                    title="Title1",
                    company_name="Company Name1",
                    company_address="Company Address1",
                    home_phone="(999)111-11-11",
                    mobile_phone="(999)111-11-22",
                    work_phone="(999)111-11-33",
                    fax="(999)111-11-44",
                    email_1="email_1@company.com",
                    email_2="email_2@company.com",
                    email_3="email_3@company.com",
                    homepage="http://www.homepage1.net",
                    birth_year="1970",
                    anniv_year="1990",
                    home_addr="Home Address1",
                    notes="Some Notes1",
                    extra_phone="(999)111-11-55"),
            Contact(first_name="First_Name2",
                    middle_name="Middle_Name2",
                    last_name="Last_Name2",
                    nickname="Nickname2",
                    pic=str(os.path.dirname(__file__)) + "\\photo.gif",
                    title="Title2",
                    company_name="Company Name2",
                    company_address="Company Address2",
                    home_phone="(999)111-11-11",
                    mobile_phone="(999)111-11-22",
                    work_phone="(999)111-11-33",
                    fax="(999)111-11-44",
                    email_1="email_1@company.com",
                    email_2="email_2@company.com",
                    email_3="email_3@company.com",
                    homepage="http://www.homepage2.net",
                    birth_year="1970",
                    anniv_year="1990",
                    home_addr="Home Address2",
                    notes="Some Notes2",
                    extra_phone="(999)111-11-55")
            ]
