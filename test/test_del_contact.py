__author__ = 'Irina.Chegodaeva'
from model.contact import Contact
from random import randrange


# deleting some contact without accepting
def test_delete_some_contact_decline(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_some_contact_or_all(index, answer="N", name_attr_for_deleting="selected[]")
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert old_contacts == new_contacts


# deleting first contact with accepting
def test_delete_some_contact_accept(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=True,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_some_contact_or_all(index, answer="Y", name_attr_for_deleting="selected[]")
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts


# deleting contact from edit_form
# fill combo-boxes ("комбобокс","число, мес€ц или группа")
# value: 3  - 1 число, 2  - январь мес€ц, 12 - 10 число, 3  - ‘евраль мес€ц, группа не редактируетс€
def test_delete_some_contact_from_edit_form(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_some_contact_from_edit_form(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


# deleting all contacts without accepting
def test_delete_all_contacts_decline(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_some_contact_or_all(index=None, answer="N", name_attr_for_deleting="MassCB")
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert old_contacts == new_contacts


# deleting all contacts with accepting
def test_delete_all_contacts_accept(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    app.contact.delete_some_contact_or_all(index=None, answer="Y", name_attr_for_deleting="MassCB")
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == 0
