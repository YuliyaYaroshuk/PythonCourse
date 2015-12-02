from model.group import Group


def test_edit_group_name(app):
    app.group.edit_group(Group(name="11111"))

def test_edit_group_header(app):
    app.group.edit_group(Group(header="22222"))




