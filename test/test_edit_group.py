__author__ = 'Irina.Chegodaeva'
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_edit(Group(name="Group_2_edited", header="Group_Header", footer="Group_Footer"), is_creating=0)
    app.session.logout()
