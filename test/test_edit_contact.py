from model.contact import Contact
import random

def test_edit_contact_firstname(app,db,check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Yaroshuk"))
    old_contacts = db.get_contact_list()
    contacts = random.choice(old_contacts)
    contact = Contact(firstname="Vanya")
    app.contact.edit_contact_by_id(contacts.id,contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_edit_contact_lastname(app):
 #   if app.contact.count() == 0:
  #      app.contact.create(Contact(lastname="Yaroshuk"))
   # old_contacts = app.contact.get_contact_list()
    #app.contact.edit_contact(Contact(lastname="Petrov"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts)== len(new_contacts)
