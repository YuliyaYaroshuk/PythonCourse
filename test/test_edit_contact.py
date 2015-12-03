from model.contact import Contact

def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Yaroshuk"))
    app.contact.edit_contact(Contact(firstname="Vanya"))


def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Yaroshuk"))
    app.contact.edit_contact(Contact(lastname="Petrov"))
