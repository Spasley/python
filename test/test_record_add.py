# -*- coding: utf-8 -*-
from model.recordfields import RecordFields

def test_test_record_add(app):
    old_records = app.record.get_record_list()
    record = RecordFields(firstname='Vova', lastname='Kolenov')
    app.record.filling_form(record)
    new_records = app.record.get_record_list()
    assert len(old_records) + 1 == len(new_records)
    old_records.append(record)
    assert sorted(old_records, key=RecordFields.id_or_max) == sorted(new_records, key=RecordFields.id_or_max)




