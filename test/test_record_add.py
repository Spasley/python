# -*- coding: utf-8 -*-
from model.recordfields import RecordFields


def test_test_record_add(app, json_records, check_ui, db):
    record = json_records
    old_records = db.get_record_list()
    app.record.filling_form(record)
    new_records = db.get_record_list()
    old_records.append(record)
    assert sorted(old_records, key=RecordFields.id_or_max) == sorted(new_records, key=RecordFields.id_or_max)
    if check_ui:
        assert (sorted(app.contact.get_contact_list(), key=RecordFields.id_or_max) == sorted(new_records, key=RecordFields.id_or_max))




