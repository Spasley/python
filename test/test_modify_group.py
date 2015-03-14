__author__ = 'Spasley'
from model.group import Group

def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name='new_name', header='new_header',
                                       footer='new_footer'))
    app.session.logout()