# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Group_1", header="Group_Header", footer="Group_Footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
