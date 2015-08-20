__author__ = 'Irina.Chegodaeva'


def test_delete_first_group(app):
    app.group.delete_first()
