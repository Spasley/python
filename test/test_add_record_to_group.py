__author__ = 'Volodya'
from model.recordfields import RecordFields
from model.group import Group
import random


def test_add_record_to_group(app, db, check_ui):
    groups = db.get_group_list()
    group = random.choice(groups)
    records = db.get_record_list()
    record = random.choice(records)
    if len(db.get_record_list()) == 0:
        app.record.filling_form(RecordFields(firstname='Test'))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Test'))
    app.record.move_to_group(record.id, group.name)
