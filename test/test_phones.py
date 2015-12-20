import re
from random import randrange
def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_all_form_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    form_on_home_page=app.contact.get_contact_list()[index]
    form_on_edit_page=app.contact.get_contact_info_from_edit_page(index)
    assert form_on_home_page.all_phones_from_home_page==merge_phones_like_on_home_page(form_on_edit_page)
    assert form_on_home_page.firstname == form_on_edit_page.firstname
    assert form_on_home_page.lastname == form_on_edit_page.lastname
    assert form_on_home_page.address == form_on_edit_page.address
    assert form_on_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(form_on_edit_page)


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

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None,[contact.email, contact.email2, contact.email3]))