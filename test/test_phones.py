import re
from random import randrange
from model.contact import Contact
from fixture.contact import ContactHelper

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_all_form_on_home_page(app,db):
    i=0
    j=0
    db_contacts = db.get_contact_list()
    list1 = sorted(app.contact.get_contact_list(),key=Contact.id_or_max)
    while i in range(len(db_contacts))and j in range(len(list1)):
        assert db_contacts[i].id == list1[j].id
        assert db_contacts[i].firstname == list1[j].firstname
        assert db_contacts[i].lastname == list1[j].lastname
        assert db_contacts[i].address == list1[j].address
        assert list1[j].all_phones_from_home_page==  "\n".join(filter(lambda x: x is not None,[db_contacts[i].home, db_contacts[i].mobile, db_contacts[i].work]))
        assert list1[j].all_emails_from_home_page == "\n".join(filter(lambda x: x is not None,[db_contacts[i].email, db_contacts[i].email2, db_contacts[i].email3]))
        i+=1
        j+=1













def test_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work

def clear(s):
    return re.sub("[() -]","",s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x!="",
                             map(lambda x: clear(x) ,
                                 filter(lambda x: x is not None,[contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(db_contacts):
    return "\n".join(filter(lambda x: x is not None,[db_contacts.email, db_contacts.email2, db_contacts.email3]))