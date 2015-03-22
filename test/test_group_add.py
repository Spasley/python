# -*- coding: utf-8 -*-
from model.group import Group


def test_test_group_add(app):
    app.group.create(Group(name="newgroup", header="header", footer="footer"))


def test_test__empty_group_add(app):
    app.group.create(Group(name="", header="", footer=""))


