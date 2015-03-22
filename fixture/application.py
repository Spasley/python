from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.record import RecordHelper
__author__ = 'Spasley'


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.record = RecordHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            False

    def open_home_page(self):
        # open homepage
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

