# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_edit(Group(name="Group_1", header="Group_Header", footer="Group_Footer"), is_creating=1)
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_edit(Group(name="", header="", footer=""), is_creating=1)
    app.session.logout()
