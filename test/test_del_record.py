__author__ = 'Spasley'

def test_record_del(app):
    app.session.login(username="admin", password="secret")
    app.record.delete_record()
    app.session.logout()
