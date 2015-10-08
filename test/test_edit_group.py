# __author__ = 'Irina.Chegodaeva'
from model.group import Group
import random
import pytest


def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        with pytest.allure.step('If there is no contact I will add a new one'):
            app.group.create(Group(name="test" + app.libs.substring))
    with pytest.allure.step('Given a group name before edit'):
        group_data = Group(name="New name" + app.libs.substring)
    with pytest.allure.step('Given a random group from the list for edit'):
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
    with pytest.allure.step('Then I modified the contact'):
        app.group.modify_group_by_id(group.id, group_data)
    with pytest.allure.step('Given a group list after edit'):
        new_groups = db.get_group_list()
    with pytest.allure.step('Then the length of the new group list is equal to the length of the old list'):
        assert len(old_groups) == len(new_groups)
    with pytest.allure.step('When I changed the contact %s in the old list' % group_data):
        group_data.id = group.id
        old_groups.remove(group)
        old_groups.insert(int(group.id), group_data)
    with pytest.allure.step('Then the new group list is equal to the old list with the edited group'):
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)