__author__ = 'Volodya'
from model.recordfields import RecordFields
from model.group import Group
import random
from fixture.orm import ORMfixture

db = ORMfixture(host='127.0.0.1', name='addressbook', user='root', password='')

def test_add_record_to_group(app):
    if len(db.get_record_list()) == 0:
        app.record.filling_form(RecordFields(firstname='Test'))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Test'))
    groups = db.get_group_list()
    group = random.choice(groups)
    records = db.get_record_list()
    record = random.choice(records)
    old_records_in_group = db.get_records_in_group(group)
    app.record.move_to_group(record.id, group.name)
    new_records_in_group = db.get_records_in_group(group)
    old_records_in_group.append(record)
    assert sorted(old_records_in_group) == sorted(new_records_in_group)