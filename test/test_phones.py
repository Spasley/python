__author__ = 'Volodka'


def test_phones_on_home_page(app):
    record_from_homepage = app.record.get_record_list()[0]
    record_from_edit_page = app.record.get_record_info_from_edit_page(0)
    assert record_from_homepage.home == record_from_edit_page.home
    assert record_from_homepage.work == record_from_edit_page.work
    assert record_from_homepage.mobile == record_from_edit_page.mobile
    assert record_from_homepage.phone2 == record_from_edit_page.phone2