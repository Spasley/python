__author__ = 'Volodya'
from model.recordfields import RecordFields
from model.group import Group
import random
from fixture.orm import ORMfixture
from fixture.db import DbFixture

db = ORMfixture(host='127.0.0.1', name='addressbook', user='root', password='')
db1 = DbFixture(host='127.0.0.1', name='addressbook', user='root', password='')

def test_test_delete_record_from_group(app):
    if len(db.get_record_list()) == 0:
        app.record.filling_form(RecordFields(firstname='Test'))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Test'))
    groups = db1.get_groups_with_records()
    choice = random.choice(groups)
    group = db.get_group_by_id(choice)
    app.record.remove_record_from_group(group)
