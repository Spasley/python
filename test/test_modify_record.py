__author__ = 'Spasley'
from model.recordfields import RecordFields

def test_record_del(app):
    if app.record.count() == 0:
        app.record.filling_form(RecordFields(firstname='Test'))
    app.record.modify_record(RecordFields(firstname='New', lastname='Newsec', fax='777777', homepage='www.d3.ru',
                                            phone2='890890', notes='Cool guy', email='firstmail',
                                            email2='secondemail', email3='thirdenail', ayear='2001',
                                            byear='2002', byear_day="//div[@id='content']/form/select[1]//option[3]",
                                            byear_month="//div[@id='content']/form/select[2]//option[3]",
                                            ayear_day="//div[@id='content']/form/select[3]//option[5]",
                                            ayear_month="//div[@id='content']/form/select[4]//option[4]",
                                            photo="//div[@id='content']/form/input[21]"))
