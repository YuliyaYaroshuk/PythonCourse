from model.contact import Contact

def test_edit_contact_firstname(app):
    app.contact.edit_contact(Contact(firstname="Vanya"))


def test_edit_contact_lastname(app):
    app.contact.edit_contact(Contact(lastname="Petrov"))
