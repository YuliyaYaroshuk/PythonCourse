from model.group import Group


def test_edit_group(app):
    app.session.login( username="admin",password="secret")
    app.group.edit_group(Group(name="11111", header="11111", footer="Python Trening"))
    app.session.logout()



