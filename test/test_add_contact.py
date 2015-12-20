# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Yuliya", lastname="Yarashuk", home="375295225058", mobile="375295225058", work="565784844",
                      middlename="tttt", title="rrr",nickname="rtrt",company="xim",address="tytututyty",fax="123123",
                      email="rrr@yyy.tu",email2="rrr1@yyy.tu",email3="rrr2@yyy.tu",homepage="yyy")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="", lastname="", home="")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts)+1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)






