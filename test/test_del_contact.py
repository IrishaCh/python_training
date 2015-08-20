__author__ = 'Irina.Chegodaeva'
from model.contact import Contact


# deleting first contact without accepting
def test_delete_first_contact_decline(app):
    app.contact.delete_first_or_all(answer="N", name_attr_for_deleting="selected[]")


# deleting first contact with accepting
def test_delete_first_contact_accept(app):
    app.contact.delete_first_or_all(answer="Y", name_attr_for_deleting="selected[]")


# deleting contact from edit_form
# fill combo-boxes ("���������","�����, ����� ��� ������")
# value: 3  - 1 �����, 2  - ������ �����, 12 - 10 �����, 3  - ������� �����, ������ �� �������������
def test_delete_contact_from_edit_form(app):
    app.contact.delete_contact_from_edit_form()


# deleting all contacts without accepting
def test_delete_all_contacts_decline(app):
    app.contact.delete_first_or_all(answer="N", name_attr_for_deleting="MassCB")


# deleting all contacts with accepting
def test_delete_all_contacts_accept(app):
    app.contact.delete_first_or_all(answer="Y", name_attr_for_deleting="MassCB")
