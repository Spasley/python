__author__ = 'Spasley'
from model.recordfields import RecordFields


def test_record_del(app):
    if app.record.count() == 0:
        app.record.filling_form(RecordFields(firstname='Test'))
    app.record.delete_record()

