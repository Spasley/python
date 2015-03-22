# -*- coding: utf-8 -*-
from model.recordfields import RecordFields

def test_test_record_add(app):
    app.record.filling_form(RecordFields(firstname='Vova', lastname='Kolenov', middlename='Michailovich',
                                         nickname='nick', title='Title', company='company',
                                         address='address', address2='SecAddress', home='123123', mobile='234234',
                                         work='345345', fax='456456', homepage='www.d3.ru',
                                         phone2='890890', notes='Cool guy', email='firstmail',
                                         email2='secondemail', email3='thirdenail', ayear='2001',
                                         byear='2002', byear_day="//div[@id='content']/form/select[1]//option[3]",
                                         byear_month="//div[@id='content']/form/select[2]//option[3]",
                                         ayear_day="//div[@id='content']/form/select[3]//option[5]",
                                         ayear_month="//div[@id='content']/form/select[4]//option[4]",
                                         photo="//div[@id='content']/form/input[21]"))



