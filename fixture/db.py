# __author__ = 'irina.chegodaeva'
import mysql.connector
from model.group import Group
from model.contact import Contact
from contextlib import closing


class DbFixture:
    pass

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    # используем with для открытия и закрытия курсора
    def get_group_list(self):
        list = []
        with closing(self.connection.cursor()) as cursor:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        return list

    # def get_group_list(self):
    #     list = []
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
    #         for row in cursor:
    #             (id, name, header, footer) = row
    #             list.append(Group(id=str(id), name=name, header=header, footer=footer))
    #     finally:
    #         cursor.close()
    #     return list

    def get_contact_list(self):
        list = []
        with closing(self.connection.cursor()) as cursor:
            cursor.execute("select id, firstname, middlename, lastname, nickname, title, company, address, home, "
                           "mobile, work, fax, email, email2, email3, homepage, byear, ayear, address2, notes, "
                           "phone2 from addressbook where deprecated is null")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, fax, email,
                 email2, email3, homepage, byear, ayear, address2, notes, phone2) = row
                list.append(Contact(id=str(id),
                                    first_name=firstname,
                                    middle_name=middlename,
                                    last_name=lastname,
                                    nickname=nickname,
                                    title=title,
                                    company_name=company,
                                    company_address=address,
                                    home_phone=home,
                                    mobile_phone=mobile,
                                    work_phone=work,
                                    fax=fax,
                                    email_1=email,
                                    email_2=email2,
                                    email_3=email3,
                                    homepage=homepage,
                                    birth_year=byear,
                                    anniv_year=ayear,
                                    home_addr=address2,
                                    notes=notes,
                                    extra_phone=phone2))
        return list

    def destroy(self):
        self.connection.close()
