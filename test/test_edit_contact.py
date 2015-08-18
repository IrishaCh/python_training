__author__ = 'Irina.Chegodaeva'
import os
from model.contact import Contact


# is_new: -1 - удаление контакта из формы редактировани€  !!!возможно нужно перенести тест в тест удалени€ контакта!!!
#          0 - редактирование контакта из формы редактированич
#          1 - создание нового контакта
#          2 - редактирование контакта из формы просмотра деталей
def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_form(Contact(first_name="First_Name",
                                        middle_name="Middle_Name",
                                        last_name="Last_Name",
                                        nickname="Nickname",
                                        pic=str(os.path.dirname(__file__)) + "\\photo.gif",
                                        title="Title",
                                        company_name="Company Name",
                                        company_address="Company Address",
                                        home_phone="(999)111-11-11",
                                        mobile_phone="(999)111-11-22",
                                        work_phone="(999)111-11-33",
                                        fax="(999)111-11-44",
                                        email_1="email_1@company.com",
                                        email_2="email_2@company.com",
                                        email_3="email_3@company.com",
                                        homepage="http://www.homepage.net",
                                        birth_year="1970",
                                        anniv_year="1990",
                                        home_addr="Home Address",
                                        notes="Some Notes",
                                        extra_phone="(999)111-11-55"), delete_photo=1, is_new=0)
    # fill combo-boxes ("комбобокс","число, мес€ц или группа")
    # value: 3  - 1 число, 2  - январь мес€ц, 12 - 10 число, 3  - ‘евраль мес€ц, группа не редактируетс€
    dataset = (("1", "3"), ("2", "3"), ("3", "14"), ("4", "4"))
    for i in range(0, 4):
        (combo, value) = dataset[i]
        app.contact.choose_from_combo(combo, value)   # 1 - комбо, 3  - 1 число
    app.contact.save_contact_form(is_new=0)
    app.session.logout()


def test_edit_contact_from_details(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_form(Contact(first_name="First_Name",
                                        middle_name="Middle_Name",
                                        last_name="Last_Name",
                                        nickname="Nickname",
                                        pic=str(os.path.dirname(__file__)) + "\\photo.gif",
                                        title="Title",
                                        company_name="Company Name",
                                        company_address="Company Address",
                                        home_phone="(999)111-11-11",
                                        mobile_phone="(999)111-11-22",
                                        work_phone="(999)111-11-33",
                                        fax="(999)111-11-44",
                                        email_1="email_1@company.com",
                                        email_2="email_2@company.com",
                                        email_3="email_3@company.com",
                                        homepage="http://www.homepage.net",
                                        birth_year="1970",
                                        anniv_year="1990",
                                        home_addr="Home Address",
                                        notes="Some Notes",
                                        extra_phone="(999)111-11-55"), delete_photo=1, is_new=2)
    # fill combo-boxes ("комбобокс","число, мес€ц или группа")
    # value: 3  - 1 число, 2  - январь мес€ц, 12 - 10 число, 3  - ‘евраль мес€ц, группа не редактируетс€
    dataset = (("1", "3"), ("2", "3"), ("3", "14"), ("4", "4"))
    for i in range(0, 4):
        (combo, value) = dataset[i]
        app.contact.choose_from_combo(combo, value)   # 1 - комбо, 3  - 1 число
    app.contact.save_contact_form(is_new=0)
    app.session.logout()


def test_edit_contact_and_delete(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_form(Contact(first_name="First_Name",
                                        middle_name="Middle_Name",
                                        last_name="Last_Name",
                                        nickname="Nickname",
                                        pic=str(os.path.dirname(__file__)) + "\\photo.gif",
                                        title="Title",
                                        company_name="Company Name",
                                        company_address="Company Address",
                                        home_phone="(999)111-11-11",
                                        mobile_phone="(999)111-11-22",
                                        work_phone="(999)111-11-33",
                                        fax="(999)111-11-44",
                                        email_1="email_1@company.com",
                                        email_2="email_2@company.com",
                                        email_3="email_3@company.com",
                                        homepage="http://www.homepage.net",
                                        birth_year="1970",
                                        anniv_year="1990",
                                        home_addr="Home Address",
                                        notes="Some Notes",
                                        extra_phone="(999)111-11-55"), delete_photo=1, is_new=-1)
    # fill combo-boxes ("комбобокс","число, мес€ц или группа")
    # value: 3  - 1 число, 2  - январь мес€ц, 12 - 10 число, 3  - ‘евраль мес€ц, группа не редактируетс€
    dataset = (("1", "3"), ("2", "3"), ("3", "14"), ("4", "4"))
    for i in range(0, 4):
        (combo, value) = dataset[i]
        app.contact.choose_from_combo(combo, value)   # 1 - комбо, 3  - 1 число
    # deleting form from edit
    app.contact.save_contact_form(is_new=0)
    app.session.logout()
