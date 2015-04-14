__author__ = 'Volodka'
import re
from random import randrange


def test_contact_info_on_home_page(app):
    records_list = app.record.get_record_list()
    index = randrange(len(records_list))
    records_from_home_page = app.record.get_record_list()[index]
    records_from_edit_page = app.record.get_record_info_from_edit_page(index)
    assert records_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(records_from_edit_page)
    assert records_from_home_page.address == merge_address_like_on_home_page(records_from_edit_page)
    assert records_from_home_page.emails == merge_emails_like_on_home_page(records_from_edit_page)
    assert records_from_home_page.firstname == records_from_edit_page.firstname
    assert records_from_home_page.lastname == records_from_edit_page.lastname


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(records_from_edit_page):
    return "\n".join(filter(lambda x: x is not None,
                            filter(lambda x: x != "", [records_from_edit_page.email, records_from_edit_page.email2,
                                                       records_from_edit_page.email3])))


def merge_phones_like_on_home_page(records_from_edit_page):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [records_from_edit_page.home, records_from_edit_page.mobile, records_from_edit_page.work,
                                        records_from_edit_page.phone2]))))


def merge_address_like_on_home_page(records_from_edit_page):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, records_from_edit_page.address.split())))
