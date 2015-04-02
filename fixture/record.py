__author__ = 'Spasley'
from model.recordfields import RecordFields


class RecordHelper:

    def __init__(self, app):
        self.app = app

    def open_records_page(self):
        # open records page
        wd = self.app.wd
        if not len(wd.find_elements_by_xpath("//*[@id='content']/h1")):
            wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def filling_form(self, RecordFields):
        # filling form
        wd = self.app.wd
        self.open_records_page()
        self.fill_record_form_text(RecordFields)
        self.fill_record_form_select(RecordFields)
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[1]").click()
        self.open_home_page()
        self.records_cache = None

    def open_record_edit_mode(self, index):
        wd = self.app.wd
        wd.find_elements_by_css_selector('img[title=Edit]')[index].click()

    def modify_record_by_index(self, RecordFields, index):
        wd = self.app.wd
        self.fill_record_form_text(RecordFields)
        self.fill_record_form_select(RecordFields)
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[1]").click()
        self.open_home_page()
        self.records_cache = None

    def modify_record(self):
        self.modify_record_by_index(0)

    def delete_record_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.records_cache = None

    def delete_record(self):
        self.delete_record_by_index(0)

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

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    records_cache = None

    def get_record_list(self):
        if self.records_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.records_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                lastname = element.find_elements_by_css_selector('td')[1].text
                firstname = element.find_elements_by_css_selector('td')[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.records_cache.append(RecordFields(firstname=firstname, lastname=lastname, id=id))
        return list(self.records_cache)

    #def get_record_info_from_edit_page(self, index):
       # self.