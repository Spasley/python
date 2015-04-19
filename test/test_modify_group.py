__author__ = 'Spasley'
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui, json_groups):
    #new_group_data = json_group
    new_group_data = Group(name='very_new_name')
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='Test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(new_group_data, group.id)
    new_groups = db.get_group_list()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

