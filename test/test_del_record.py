__author__ = 'Spasley'
from model.recordfields import RecordFields


def test_record_del(app):
    if app.record.count() == 0:
        app.record.filling_form(RecordFields(firstname='Test'))
    old_records = app.record.get_record_list()
    app.record.delete_record()
    new_records = app.record.get_record_list()
    assert len(old_records) - 1 == len(new_records)
    old_records[0:1] = []
    assert old_records == new_records