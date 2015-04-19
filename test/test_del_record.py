__author__ = 'Spasley'
from model.recordfields import RecordFields
import random


def test_record_del(app, db, check_ui):
    if len(db.get_record_list()) == 0:
        app.record.filling_form(RecordFields(firstname='Test'))
    old_records = db.get_record_list()
    record = random.choice(old_records)
    app.record.delete_record_by_id(record.id)
    assert len(old_records) - 1 == app.record.count()
    new_records = db.get_record_list()
    old_records.remove(record)
    assert old_records == new_records
    if check_ui:
        assert (sorted(app.contact.get_contact_list(), key=RecordFields.id_or_max) == sorted(new_records, key=RecordFields.id_or_max))