__author__ = 'Volodya'
from model.recordfields import RecordFields


def test_group_list(app, db):
    db_records = db.get_record_list()
    ui_records = app.record.get_record_list()
    def clean(record):
        return RecordFields(id=record.id, firstname=record.firstname.strip(), lastname=record.lastname.strip(),
                            address=record.address.strip(), company=record.company.strip())
    db_records_for_compare = []
    for record in db_records:
        clean(record)
        db_records_for_compare.append(record)
        return db_records_for_compare
    assert sorted(ui_records, key=RecordFields.id_or_max) == sorted(db_records_for_compare, key=RecordFields.id_or_max)