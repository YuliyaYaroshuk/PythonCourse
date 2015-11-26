from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application_Cont:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    #def logout(self):
       # wd = self.wd
        #wd.find_element_by_link_text("Logout").click()

    def create_contact(self,contact):
        wd = self.wd
        self.open_contact_page()
        #fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

   # def login(self, username, password):
        #wd = self.wd
       #self.open_home_page()
       # wd.find_element_by_name("user").click()
       # wd.find_element_by_name("user").clear()
        #wd.find_element_by_name("user").send_keys(username)
       # wd.find_element_by_name("pass").click()
       # wd.find_element_by_name("pass").clear()
       # wd.find_element_by_name("pass").send_keys(password)
        #wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()