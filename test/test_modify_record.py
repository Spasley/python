__author__ = 'Spasley'
from model.recordfields import RecordFields
import random


def test_record_del(app, db, check_ui):
    if len(db.get_record_list()) == 0:
        app.record.filling_form(RecordFields(firstname='Test'))
    old_records = db.get_record_list()
    record = random.choice(old_records)
    record_index = old_records.index(record)
    new_record_data = RecordFields(firstname='New', lastname='Newsec', fax='777777', homepage='www.d3.ru',
                                            phone2='890890', notes='Cool guy', email='firstmail',
                                            email2='secondemail', email3='thirdenail', ayear='2001',
                                            byear='2002', byear_day="//div[@id='content']/form/select[1]//option[3]",
                                            byear_month="//div[@id='content']/form/select[2]//option[3]",
                                            ayear_day="//div[@id='content']/form/select[3]//option[5]",
                                            ayear_month="//div[@id='content']/form/select[4]//option[4]",
                                            photo="//div[@id='content']/form/input[21]")
    app.record.modify_record_by_id(record.id, new_record_data)
    new_records = db.get_record_list()
    old_records[record_index] = new_records[record_index]
    assert sorted(old_records, key=RecordFields.id_or_max) == sorted(new_records, key=RecordFields.id_or_max)
    if check_ui:
        assert (sorted(app.contact.get_contact_list(), key=RecordFields.id_or_max) == sorted(new_records, key=RecordFields.id_or_max))