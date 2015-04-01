__author__ = 'Spasley'
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    old_groups = app.group.get_group_list()
    group = Group(name='new_name')
    app.group.modify_first_group(group)
    group.id = old_groups[0].id
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

'''def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    app.group.modify_first_group(Group(header='new_header'))

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name='Test'))
    app.group.modify_first_group(Group(footer='new_footer'))'''
