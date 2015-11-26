# -*- coding: utf-8 -*-

import pytest

from fixture.application_contact import Application_Cont
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application_Cont()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login( username="admin",password="secret")
    app.create_contact(Contact(firstname="Yuliya", lastname="Yarashuk", home="375295225058"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin",password="secret")
    app.create_contact(Contact(firstname="", lastname="", home=""))
    app.session.logout()





