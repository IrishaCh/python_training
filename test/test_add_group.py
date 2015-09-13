# -*- coding: utf-8 -*-
from model.group import Group
import re


def test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    #group.name = trim_space(group.name)
    # def clean(group):
    #     return Group(id=group.id, name=group.name.strip())
    #k = clean(new_groups)
    # l = sorted(old_groups, key=Group.id_or_max)
    # r = sorted(map(clean, new_groups), key=Group.id_or_max)
    # s = 0
    # if l != r:
    #     s= 1
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def trim_space(text):
    text = re.sub(r'\s+', ' ', text).strip()
    return text