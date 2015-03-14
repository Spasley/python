__author__ = 'Spasley'
from model.record_fields import Record_fields

def test_record_del(app):
    app.session.login(username="admin", password="secret")
    app.record.modify_record(Record_fields(firstname='New', lastname='Newsec',
                                            middlename='Michailovich', nickname='nick', title='Title', company='company',
                                            address='address', address2='SecAddress', home='123123', mobile='234234',
                                            work='345345', fax='777777', homepage='www.d3.ru',
                                            phone2='890890', notes='Cool guy', email='firstmail',
                                            email2='secondemail', email3='thirdenail', ayear='2001',
                                            byear='2002', byear_day="//div[@id='content']/form/select[1]//option[3]",
                                            byear_month="//div[@id='content']/form/select[2]//option[3]",
                                            ayear_day="//div[@id='content']/form/select[3]//option[5]",
                                            ayear_month="//div[@id='content']/form/select[4]//option[4]",
                                            photo="//div[@id='content']/form/input[21]"))
    app.session.logout()