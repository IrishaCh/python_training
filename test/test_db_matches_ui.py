# __author__ = 'irina.chegodaeva'
from model.group import Group
from model.contact import Contact
from timeit import timeit


def test_group_list(app, db):
    from_web = app.group.get_group_list()
    from_db = db.get_group_list()
    print("\n", timeit(lambda: from_web, number=1))
    print(timeit(lambda: map(app.libs.clean_group, from_db), number=1000))
    assert sorted(from_web, key=Group.id_or_max) == sorted(map(app.libs.clean_group, from_db), key=Group.id_or_max)


def test_contact_list(app, db):
    from_web = app.contact.get_contact_list()
    from_db = db.get_contact_list()
    print("\n", timeit(lambda: from_web, number=1))
    print(timeit(lambda: map(app.libs.clean_contact, from_db), number=1000))
    assert sorted(from_web, key=Contact.id_or_max) == sorted(map(app.libs.clean_contact, from_db), key=Contact.id_or_max)
