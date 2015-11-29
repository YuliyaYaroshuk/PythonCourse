from model.contact import Contact

def test_edit_contact(app):
    app.session.login( username="admin",password="secret")
    app.contact.edit_contact(Contact(firstname="Vanya", lastname="Ivanov", home="375295225058"))
    app.session.logout()