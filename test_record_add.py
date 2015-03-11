# -*- coding: utf-8 -*-
from record_fields import Record_fields
import pytest
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_record_add(app):
    app.login(username="admin", password="secret")
    app.filling_form(Record_fields(firstname='Vova', lastname='Kolenov',
                                            middlename='Michailovich', nickname='nick', title='Title', company='company',
                                            address='address', address2='SecAddress', home='123123', mobile='234234',
                                            work='345345', fax='456456', homepage='www.d3.ru',
                                            phone2='890890', notes='Cool guy', email='firstmail',
                                            email2='secondemail', email3='thirdenail', ayear='2001',
                                            byear='2002', byear_day="//div[@id='content']/form/select[1]//option[3]",
                                            byear_month="//div[@id='content']/form/select[2]//option[3]",
                                            ayear_day="//div[@id='content']/form/select[3]//option[5]",
                                            ayear_month="//div[@id='content']/form/select[4]//option[4]",
                                            photo="//div[@id='content']/form/input[21]")) # _day option[1-31], _month option[1-12]
    app.logout()


