from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, home=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.home = home
        self.id = id

    def __repr__(self):
        return "%s" % (self.id)

    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize