__author__ = 'Spasley'


class RecordHelper:

    def __init__(self, app):
        self.app = app

    def open_records_page(self):
        # open records page
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def filling_form(self, RecordFields):
        # filling form
        wd = self.app.wd
        self.open_records_page()
        self.fill_record_form_text(RecordFields)
        self.fill_record_form_select(RecordFields)
        '''wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(RecordFields.fistname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(RecordFields.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(RecordFields.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(RecordFields.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(RecordFields.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(RecordFields.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(RecordFields.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(RecordFields.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(RecordFields.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(RecordFields.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(RecordFields.fax)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(RecordFields.homepage)
        wd.find_element_by_xpath(RecordFields.byear_day).click()
        wd.find_element_by_xpath(RecordFields.byear_month).click()
        wd.find_element_by_xpath(RecordFields.ayear_day).click()
        wd.find_element_by_xpath(RecordFields.ayear_month).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(RecordFields.byear)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(RecordFields.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(RecordFields.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(RecordFields.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(RecordFields.notes)
        #wd.find_element_by_name("title").click() похоже, случайно кликнул, хз зачем это тут
        wd.find_element_by_name("photo").click()
        wd.find_element_by_xpath(RecordFields.photo).click()'''

    def modify_record(self, RecordFields):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_record_form_text(RecordFields)
        self.fill_record_form_select(RecordFields)
        '''wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(RecordFields.fistname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(RecordFields.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(RecordFields.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(RecordFields.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(RecordFields.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(RecordFields.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(RecordFields.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(RecordFields.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(RecordFields.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(RecordFields.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(RecordFields.fax)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(RecordFields.homepage)
        wd.find_element_by_xpath(RecordFields.byear_day).click()
        wd.find_element_by_xpath(RecordFields.byear_month).click()
        wd.find_element_by_xpath(RecordFields.ayear_day).click()
        wd.find_element_by_xpath(RecordFields.ayear_month).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(RecordFields.byear)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(RecordFields.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(RecordFields.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(RecordFields.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(RecordFields.notes)
        wd.find_element_by_name("photo").click()
        wd.find_element_by_xpath(RecordFields.photo).click()'''
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[1]").click()
        self.open_home_page()

    def delete_record(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value_if_select(self, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_xpath(text).click()

    def fill_record_form_text(self, RecordFields):
        self.change_field_value(RecordFields.firstname, "firstname")
        self.change_field_value(RecordFields.lastname, "lastname")
        self.change_field_value(RecordFields.middlename, "middlename")
        self.change_field_value(RecordFields.nickname, "nickname")
        self.change_field_value(RecordFields.title, "title")
        self.change_field_value(RecordFields.company, "company")
        self.change_field_value(RecordFields.address, "address")
        self.change_field_value(RecordFields.home, "home")
        self.change_field_value(RecordFields.mobile, "mobile")
        self.change_field_value(RecordFields.work, "work")
        self.change_field_value(RecordFields.fax, "fax")
        self.change_field_value(RecordFields.homepage, "homepage")
        self.change_field_value(RecordFields.byear, "byear")
        self.change_field_value(RecordFields.ayear, "ayear")
        self.change_field_value(RecordFields.address2, "address2")
        self.change_field_value(RecordFields.phone2, "phone2")
        self.change_field_value(RecordFields.notes, "notes")

    def fill_record_form_select(self, RecordFields):
        self.change_field_value_if_select(RecordFields.byear_day)
        self.change_field_value_if_select(RecordFields.byear_month)
        self.change_field_value_if_select(RecordFields.ayear_day)
        self.change_field_value_if_select(RecordFields.ayear_month)
        # self.change_field_value(RecordFields.photo)




