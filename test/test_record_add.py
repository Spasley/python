# -*- coding: utf-8 -*-
from model.recordfields import RecordFields


def test_test_record_add(app, json_records):
    record = json_records
    old_records = app.record.get_record_list()
    app.record.filling_form(record)
    assert len(old_records) + 1 == app.record.count()
    new_records = app.record.get_record_list()
    old_records.append(record)
    assert sorted(old_records, key=RecordFields.id_or_max) == sorted(new_records, key=RecordFields.id_or_max)




