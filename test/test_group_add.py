# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="newgroup", header="header", footer="footer"))
    app.session.logout()

def test_test__empty_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

