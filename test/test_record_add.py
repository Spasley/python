# -*- coding: utf-8 -*-
from model.recordfields import RecordFields
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    RecordFields(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                 address=address, company=company)
    for firstname in ["", random_string("firstnamename", 15)]
    for middlename in ["", random_string("middlename", 15)]
    for lastname in ["", random_string("lastname", 15)]
    for nickname in ["", random_string("nickname", 15)]
    for address in ["", random_string("address", 15)]
    for company in ["", random_string("company", 15)]
]


@pytest.mark.parametrize("record", testdata, ids=[repr(x) for x in testdata])
def test_test_record_add(app, record):
    old_records = app.record.get_record_list()
    app.record.filling_form(record)
    assert len(old_records) + 1 == app.record.count()
    new_records = app.record.get_record_list()
    old_records.append(record)
    assert sorted(old_records, key=RecordFields.id_or_max) == sorted(new_records, key=RecordFields.id_or_max)




