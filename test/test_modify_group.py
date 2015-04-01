__author__ = 'Spasley'
from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name='new_name')
    group.id = old_groups[index].id
    app.group.modify_group_by_index(group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    app.group.modify_first_group(Group(header='new_header'))

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    app.group.modify_first_group(Group(footer='new_footer'))'''
