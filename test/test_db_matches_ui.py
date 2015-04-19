__author__ = 'Volodya'
from model.recordfields import RecordFields


def test_group_list(app, db):
    db_records = db.get_record_list()
    ui_records = app.record.get_record_list()
    assert sorted(ui_records, key=RecordFields.id_or_max) == sorted(db_records, key=RecordFields.id_or_max)