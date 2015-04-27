__author__ = 'Volodya'
import mysql.connector
from model.group import Group
from model.recordfields import RecordFields


class DbFixture:

    def __init__(self, host, name, user, password):
        self.name = name
        self.host = host
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute('SELECT group_id, group_name, group_header, group_footer FROM group_list')
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_record_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, address, company FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, company) = row
                list.append(RecordFields(id=str(id), firstname=firstname, lastname=lastname, address=address, company=company))
        finally:
            cursor.close()
        return list

    def get_groups_with_records(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT DISTINCT group_id FROM address_in_groups WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                group_id = row
                list.append(Group(id=str(group_id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()