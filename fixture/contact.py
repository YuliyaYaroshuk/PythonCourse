from model.contact import Contact
import re
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
        self.change_field_value_contact("mobile", contact.mobile)
        self.change_field_value_contact("work", contact.work)
        self.change_field_value_contact("address", contact.address)
        self.change_field_value_contact("email", contact.email)
        self.change_field_value_contact("email2", contact.email2)
        self.change_field_value_contact("email3", contact.email3)
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

    def edit_contact_by_index(self,index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector(".center>a>img[title=\"Edit\"]")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector(".center>a>img[title=\"Edit\"]")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector(".center>a>img[title=\"Details\"]")[index].click()

    def edit_contact(self):
        self.edit_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        #wd.get("http://localhost:8080/addressbook/")
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact(self):
        self.delete_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            #wd.get("http://localhost:8080/addressbook/")
            self.contact_cache=[]
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname,lastname=lastname,id = id,
                                                  all_phones_from_home_page = all_phones,
                                                  address=address,all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname,id=id,home=home, mobile= mobile, work=work,
                       address=address,
                       email=email,email2=email2,email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)",text ).group(1)
        mobile = re.search("M: (.*)",text ).group(1)
        work = re.search("W: (.*)",text ).group(1)
        return Contact(home=home, mobile= mobile, work=work)






