# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata=[Contact(firstname="", lastname="", home="", mobile="", work="",email="",email2="",email3="", address="")]+[
        Contact(firstname=random_string("firstname",10), lastname=random_string("lastname",10), home=random_string("home",7),
                mobile=random_string("mobile",7),work=random_string("work",7),email=random_string("email",10),
                email2=random_string("email2",10),email3=random_string("email3",10),address=random_string("address",10))
        for i in range(5)
        ]
@pytest.mark.parametrize("contact",testdata, ids=[str(x) for x in testdata])
def test_add_contact(app,contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)









