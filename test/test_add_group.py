# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.session.login( username="admin",password="secret")
    app.group.create(Group(name="Yuliya", header="Yuliya Yarashuk", footer="Python Trening"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin",password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


