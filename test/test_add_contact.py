# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Yuliya", lastname="Yarashuk", home="375295225058"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", home=""))






