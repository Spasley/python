# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from record_fields import Record_fields

import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_record_add(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        # open homepage
        wd.get("http://localhost/addressbook/edit.php")

    def login(self, wd, username="admin", password="secret"):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def filling_form(self, wd, Record_fields):
        # filling form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(Record_fields.fistname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(Record_fields.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(Record_fields.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(Record_fields.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(Record_fields.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(Record_fields.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(Record_fields.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(Record_fields.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(Record_fields.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(Record_fields.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(Record_fields.fax)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(Record_fields.homepage)
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").is_selected():
        wd.find_element_by_xpath(Record_fields.byear_day).click()
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
        wd.find_element_by_xpath(Record_fields.byear_month).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(Record_fields.byear)
        wd.find_element_by_xpath("//div[@id='content']//label[.='Anniversary:']").click()
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[5]").is_selected():
        wd.find_element_by_xpath(Record_fields.ayear_day).click()
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").is_selected():
        wd.find_element_by_xpath(Record_fields.ayear_month).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(Record_fields.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(Record_fields.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(Record_fields.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(Record_fields.notes)
        #wd.find_element_by_name("title").click() похоже, случайно кликнул, хз зачем это тут
        wd.find_element_by_name("photo").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def test_test_record_add(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.filling_form(wd, Record_fields(firstname='Vova', lastname='Kolenov',
                                            middlename='Michailovich', nickname='nick', title='Title', company='company',
                                            address='address', address2='SecAddress', home='123123', mobile='234234',
                                            work='345345', fax='456456', homepage='www.d3.ru',
                                            phone2='890890', notes='Cool guy', email='firstmail',
                                            email2='secondemail', email3='thirdenail', ayear='2001',
                                            byear='2002', byear_day="//div[@id='content']/form/select[1]//option[3]",
                                            byear_month="//div[@id='content']/form/select[2]//option[3]",
                                            ayear_day="//div[@id='content']/form/select[3]//option[5]",
                                            ayear_month="//div[@id='content']/form/select[4]//option[4]"))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
