# -*- coding: utf-8 -*-
import pytest
import os
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.fill_contacts_form(Contact(first_name="First_Name",
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
                                        extra_phone="(999)111-11-55"))
    # fill combo-boxes ("комбобокс","число, месяц или группа")
    # value: 3  - 1 число, 2  - Январь месяц, 12 - 10 число, 3  - Февраль месяц, 1  - не принадлежит никакой группе
    dataset = (("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1"))
    for i in range(0, 5):
        (combo, value) = dataset[i]
        app.choose_from_combo(combo, value, i)   # 1 - комбо, 3  - 1 число
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.fill_contacts_form(Contact(first_name="",
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
                                        extra_phone=""))
    # fill combo-boxes: combo - № комбобокса, value - значение (1 - соответствует "не выбрано")
    for i in range(0, 5):
        app.choose_from_combo(combo=str(i+1), value="1", step_counter=i)   # 1 - комбо, 1  - число не выбрано
    app.session.logout()
