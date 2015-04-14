__author__ = 'Volodka'
import re


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(RecordFields):
    return "\n".join(filter(lambda x: x != "",
                           map(lambda x: clear(x),
                               filter(lambda x: x is not None,
                                      [RecordFields.home, RecordFields.work, RecordFields.work, RecordFields.phone2]))))


def test_phones_on_home_page(app):
    record_from_homepage = app.record.get_record_list()[0]
    record_from_edit_page = app.record.get_record_info_from_edit_page(0)
    assert record_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(record_from_edit_page)


def test_phones_on_record_view_page(app):
    record_from_view_page = app.record.get_record_from_view_page()[0]
    record_from_edit_page = app.record.get_record_info_from_edit_page(0)
    assert record_from_view_page.home == record_from_edit_page.home
    assert record_from_view_page.work == record_from_edit_page.work
    assert record_from_view_page.mobile == record_from_edit_page.mobile
    assert record_from_view_page.phone2 == record_from_edit_page.phone2

