__author__ = 'Spasley'


class RecordFields:

    def __init__(self, firstname=None, lastname=None, middlename=None, nickname=None, title=None,
                 company=None, address=None, address2=None, home=None, mobile=None, work=None, fax=None, homepage=None, phone2=None,
                 notes=None, email=None, email2=None, email3=None, ayear=None, byear=None, byear_day=None, byear_month=None, ayear_day=None,
                 ayear_month=None, photo=None):
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
        self.ayear = ayear
        self.byear = byear
        self.byear_day = byear_day
        self.byear_month = byear_month
        self.ayear_day = ayear_day
        self.ayear_month = ayear_month
        self.photo = photo

