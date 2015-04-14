__author__ = 'Spasley'
from sys import maxsize


class RecordFields:

    def __init__(self, firstname=None, lastname=None, middlename=None, nickname=None, title=None,
                 company=None, address=None, address2=None, home=None, mobile=None, work=None, fax=None, homepage=None, phone2=None,
                 notes=None, email=None, email2=None, email3=None, ayear=None, byear=None, byear_day=None, byear_month=None, ayear_day=None,
                 ayear_month=None, photo=None, id=None, all_phones_from_home_page=None, emails=None):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.address2 = address2
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.homepage = homepage
        self.phone2 = phone2 #secondary home phone number
        self.notes = notes
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.byear = byear
        self.ayear = ayear
        self.byear_day = byear_day
        self.byear_month = byear_month
        self.ayear_day = ayear_day
        self.ayear_month = ayear_month
        self.photo = photo
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.emails = emails

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return "%s:%s, %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname