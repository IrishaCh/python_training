__author__ = 'Irina.Chegodaeva'


# deleting first contact without accepting
def test_delete_first_contact_decline(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_or_all(answer="N", name_attr_for_deleting="selected[]")
    app.session.logout()


# deleting first contact with accepting
def test_delete_first_contact_accept(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_or_all(answer="Y", name_attr_for_deleting="selected[]")
    app.session.logout()


# deleting all contacts without accepting
def test_delete_all_contacts_decline(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_or_all(answer="N", name_attr_for_deleting="MassCB")
    app.session.logout()


# deleting all contacts with accepting
def test_delete_all_contacts_accept(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_or_all(answer="Y", name_attr_for_deleting="MassCB")
    app.session.logout()
