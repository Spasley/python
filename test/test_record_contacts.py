__author__ = 'Volodka'
import re
from random import randrange


def test_contact_info_on_home_page(app):
    records_list = app.record.get_record_list()
    index = randrange(len(records_list))
    records_from_home_page = app.record.get_record_list()[index]
    records_from_edit_page = app.record.get_record_info_from_edit_page(index)
    records_from_edit_page.all_phones_from_home_page = merge_phones_like_on_home_page(records_from_edit_page)
    records_from_edit_page.emails = merge_emails_like_on_home_page(records_from_edit_page)
    assert records_from_home_page.all_phones_from_home_page == records_from_edit_page.all_phones_from_home_page \
           and re.sub(r'\s+', ' ', records_from_home_page.address.rstrip("\n ")) == re.sub(r'\s+', ' ',
               records_from_edit_page.address.rstrip("\n ")) \
           and records_from_home_page.emails == records_from_edit_page.emails \
           and records_from_home_page.firstname == records_from_edit_page.firstname \
           and records_from_home_page.lastname == records_from_edit_page.lastname


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(RecordFields):
    return "\n".join(filter(lambda x: x is not None,
                            filter(lambda x: x != "", [RecordFields.email, RecordFields.email2, RecordFields.email3])))


def merge_phones_like_on_home_page(RecordFields):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [RecordFields.home, RecordFields.mobile, RecordFields.work,
                                        RecordFields.phone2]))))

