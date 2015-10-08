# __author__ = 'Irina.Chegodaeva'
from model.group import Group
import random
import pytest


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        with pytest.allure.step('If there is no group I will add a new one: Group(name="test")'):
            app.group.create(Group(name="test"))
    with pytest.allure.step('Given a group list before deleting'):
        old_groups = db.get_group_list()
    with pytest.allure.step('Given a random group from the list for deleting'):
        group = random.choice(old_groups)
    with pytest.allure.step('I delete the group from the list'):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('Given a group list after deleting'):
        new_groups = db.get_group_list()
    with pytest.allure.step('The deleted group has removed from the group list after deleting'):
        old_groups.remove(group)
    with pytest.allure.step('Then the new group list is equal to the old list without the deleted group'):
        assert old_groups == new_groups
        if check_ui:
            assert sorted(map(app.libs.clean_group, new_groups), key=Group.id_or_max) ==\
                   sorted(app.group.get_group_list(), key=Group.id_or_max)
