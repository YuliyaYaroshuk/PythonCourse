from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, home=None, id=None,all_phones_from_home_page=None, mobile=None, work=None,
                 middlename= None,nickname=None,title=None,company=None,address=None,fax=None,email=None,email2=None,
                 email3=None,homepage=None,all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.home = home
        self.id = id
        self.mobile = mobile
        self.work = work
        self.all_phones_from_home_page = all_phones_from_home_page
        self.middlename=middlename
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.fax=fax
        self.email=email
        self.email2=email2
        self.email3=email3
        self.homepage=homepage
        self.all_emails_from_home_page=all_emails_from_home_page


    def __repr__(self):
        return "%s" % (self.id)

    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize