__author__ = 'Irina.Chegodaeva'
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="Group_1", header="Group_Header", footer="Group_Footer"))
    app.session.logout()
