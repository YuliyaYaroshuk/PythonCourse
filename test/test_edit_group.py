from model.group import Group


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group1"))
    app.group.edit_group(Group(name="11111"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="Header1"))
    app.group.edit_group(Group(header="22222"))




