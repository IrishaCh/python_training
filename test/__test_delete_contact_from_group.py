# __author__ = 'Irina.Chegodaeva'
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random
import pytest

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


# удаление любого котнакта из любой группы
def test_delete_any_contact_from_any_group(app):
    if len(db.get_contact_list()) == 0:
        with pytest.allure.step('If there is no contact I will add a new one'):
            app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                    delete_photo=False,
                                    dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
    if len(db.get_group_list()) == 0:
        with pytest.allure.step('If there is no group I will add a new one'):
            app.group.create(Group(name="test"))
    with pytest.allure.step('Given a random group from the list for edit'):
        group_index = random.choice(range(0, len(db.get_group_list())))
        group = db.get_group_list()[group_index]
    with pytest.allure.step('Given a contact list in a group %s' % group):
        contact_list = db.get_contacts_in_group(group)
    # если в этой группе нет контактов, то добавим один контакт в группу
    if len(contact_list) == 0:
        with pytest.allure.step('When I add new contact'):
            app.contact.add_contact(Contact(first_name="test" + app.libs.substring),
                                    delete_photo=False,
                                    dataset=(("1", "3"), ("2", "2"), ("3", "12"), ("4", "3"), ("5", "1")))
        with pytest.allure.step('And I add this contact in the group %s' % group):
            contact = random.choice(db.get_contacts_in_group(group))
            app.contact.add_contact_in_group(contact.id, group_index)
    with pytest.allure.step('Given a random contact from the list for edit'):
        contact = random.choice(db.get_contacts_in_group(group))
    with pytest.allure.step('Then I remove contact from the list'):
        app.contact.delete_contact_from_group(contact.id, group_index)
