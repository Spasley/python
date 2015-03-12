__author__ = 'Spasley'

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        # open groups page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, Group):
        # init group page
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        #fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.name)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select//option[1]").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.footer)
        # submit form
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        # return to groups page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()