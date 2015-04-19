__author__ = 'Volodya'
from pony.orm import *
from datetime import datetime
from model.group import Group
from model.recordfields import RecordFields
from pymysql.converters import decoders


class ORMfixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMRecord(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, footer=group.footer, header=group.header)
        return list(map(convert, groups))

    def convert_records_to_model(self, records):
        def convert(record):
            return RecordFields(id=str(record.id), firstname=record.firstname, lastname=record.lastname)
        return list(map(convert, records))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMfixture.ORMGroup))

    @db_session
    def get_record_list(self):
        return self.convert_records_to_model(select(r for r in ORMfixture.ORMRecord if r.deprecated is None))