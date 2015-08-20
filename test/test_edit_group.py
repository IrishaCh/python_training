__author__ = 'Irina.Chegodaeva'
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group_2_edited", header="Group_Header", footer="Group_Footer"))
    app.session.logout()
