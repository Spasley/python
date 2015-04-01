__author__ = 'Spasley'
from model.recordfields import RecordFields
from random import randrange


def test_record_del(app):
    if app.record.count() == 0:
        app.record.filling_form(RecordFields(firstname='Test'))
    old_records = app.record.get_record_list()
    index = randrange(len(old_records))
    app.record.delete_record_by_index(index)
    assert len(old_records) - 1 == app.record.count()
    new_records = app.record.get_record_list()
    old_records[index:index + 1] = []
    assert old_records == new_records