from model.contact import Contact
class ContactHelper:

    def __init__(self,app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value_contact("firstname", contact.firstname)
        self.change_field_value_contact("lastname", contact.lastname)
        self.change_field_value_contact("home", contact.home)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def change_field_value_contact(self,field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def edit_contact(self, new_contact_data):
        wd = self.app.wd
        wd.get("http://localhost:8080/addressbook/")
        wd.find_element_by_css_selector(".center>a>img[title=\"Edit\"]").click()
        #wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[3]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_contact(self):
        wd = self.app.wd
        wd.get("http://localhost:8080/addressbook/")
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            wd.get("http://localhost:8080/addressbook/")
            self.contact_cache=[]
            for element in wd.find_elements_by_css_selector("#maintable>tbody>tr>td>input"):
            #text = element.text
                id = element.get_attribute("value")
                self.contact_cache.append(Contact(id = id))
        return list(self.contact_cache)






