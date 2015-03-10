# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_group_add(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="newgroup", header="header", footer="footer"))
    app.logout()

def test_test__empty_group_add(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

