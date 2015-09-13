# __author__ = 'irina.chegodaeva'
from model.group import Group
import re
from timeit import timeit


def test_group_list(app, db):
    print("/n")
    print(timeit(lambda: app.group.get_group_list(), number=1))
    def clean(group):
        return Group(id=group.id, name=re.sub(r'\s+', ' ', group.name).strip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
