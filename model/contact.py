from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, home=None, id=None,all_phones_from_home_page=None, mobile=None, work=None,
                 address=None,email=None,email2=None,
                 email3=None,all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.home = home
        self.id = id
        self.mobile = mobile
        self.work = work
        self.all_phones_from_home_page = all_phones_from_home_page
        self.address=address
        self.email=email
        self.email2=email2
        self.email3=email3
        self.all_emails_from_home_page=all_emails_from_home_page


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.firstname, self.lastname,self.email)

    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize