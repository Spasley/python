# -*- coding: utf-8 -*-
from model.group import Group

def test_test_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="newgroup", header="header", footer="footer"))
    app.session.logout()

def test_test__empty_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

