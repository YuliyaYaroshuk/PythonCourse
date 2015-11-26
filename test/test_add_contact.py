# -*- coding: utf-8 -*-

import pytest

from fixture.application_contact import Application_Cont
from model.contact import Contact


@pytest.fixture
def app_contact(request):
    fixture = Application_Cont()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app_contact):
    app_contact.login( username="admin",password="secret")
    app_contact.create_contact(Contact(firstname="Yuliya", lastname="Yarashuk", home="375295225058"))
    app_contact.logout()

def test_add_empty_group(app_contact):
    app_contact.login(username="admin",password="secret")
    app_contact.create_contact(Contact(firstname="", lastname="", home=""))
    app_contact.logout()





