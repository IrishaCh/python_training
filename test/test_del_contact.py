# __author__ = 'Irina.Chegodaeva'
from model.contact import Contact
import random


# deleting some contact without accepting
def test_delete_some_contact_decline(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_some_contact_or_all_by_id(int(contact.id), answer="N", name_attr_for_deleting="selected[]")
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(app.libs.clean_contact, new_contacts), key=Contact.id_or_max) ==\
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# deleting first contact with accepting
def test_delete_some_contact_accept(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=True,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    id = int(contact.id)
    app.contact.delete_some_contact_or_all_by_id(id, answer="Y", name_attr_for_deleting="selected[]")
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(app.libs.clean_contact, new_contacts), key=Contact.id_or_max) ==\
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# deleting contact from edit_form
# fill combo-boxes ("комбобокс","число, мес€ц или группа")
# value: 3  - 1 число, 2  - январь мес€ц, 12 - 10 число, 3  - ‘евраль мес€ц, группа не редактируетс€
def test_delete_some_contact_from_edit_form(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    id = int(contact.id)
    app.contact.delete_some_contact_from_edit_form_by_id(id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(app.libs.clean_contact, new_contacts), key=Contact.id_or_max) ==\
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# deleting all contacts without accepting
def test_delete_all_contacts_decline(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    old_contacts = db.get_contact_list()
    app.contact.delete_some_contact_or_all_by_id(id=None, answer="N", name_attr_for_deleting="MassCB")
    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(app.libs.clean_contact, new_contacts), key=Contact.id_or_max) ==\
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


# deleting all contacts with accepting
def test_delete_all_contacts_accept(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                delete_photo=False,
                                dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    app.contact.delete_some_contact_or_all_by_id(id=None, answer="Y", name_attr_for_deleting="MassCB")
    new_contacts = db.get_contact_list()
    assert len(new_contacts) == 0
    if check_ui:
        assert sorted(map(app.libs.clean_contact, new_contacts), key=Contact.id_or_max) ==\
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
