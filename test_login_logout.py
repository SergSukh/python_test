# -*- coding: utf-8 -*-
import pytest

from application import Application
from group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_patient(app):
    app.login(username="Директор1", password="123456")
    app.fill_newclient_form(Group(surname="ФамилияАвтоТест", name="Имя", secondname="Отчество",
                                  datapicker="10102010", phone="79278889966", fromwhere="2ГИС"))
    app.submit_newpatient_creation()


def test_empty_clientdata(app):
    app.login(username="Директор1", password="123456")
    app.fill_newclient_form(Group(surname="", name="", secondname="",
                                  datapicker="", phone="", fromwhere=""))
    # app.submit_newpatient_creation()
