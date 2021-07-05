from app import app
from app.core.models import Models

class ModelUsers(Models):
    def __init__(self, params = None):
        super(ModelUsers, self).__init__(params)

        self.table_name = 'users'

    def get_list(self):
        sql_rows = self.execute("SELECT id, \
            fullname, \
            email, \
            nik, \
            dob, \
            gender, \
            identity, \
            identity_type, \
            user_role, \
            address, \
            avatar, \
            {}, \
            {} from `{}`".format(self.convert_time_zone('created_at'), self.convert_time_zone('updated_at'), self.table_name))

        convert_attribute_list = [
            'created_at',
            'updated_at'
        ]

        sql_rows = self.convert_to_normal_date(sql_rows, convert_attribute_list)

        # Convert date with format
        convert_attribute_list = [
            'dob'
        ]

        sql_rows = self.convert_to_normal_date(sql_rows, convert_attribute_list, '%Y-%m-%d')

        return sql_rows

    def get_detail_by(self, columns = None, value = None):
        if columns == "name":
            value = value.replace('-', ' ')

        sql_rows = self.execute("SELECT id, \
            fullname, \
            email, \
            nik, \
            dob, \
            gender, \
            identity, \
            identity_type, \
            user_role, \
            address, \
            avatar, \
            {}, \
            {} from `{}` WHERE `{}` = '{}'".format(self.convert_time_zone('created_at'), self.convert_time_zone('updated_at'), self.table_name, columns, value))

        convert_attribute_list = [
            'created_at',
            'updated_at'
        ]

        sql_rows = self.convert_to_normal_date(sql_rows, convert_attribute_list)

        # Convert date with format
        convert_attribute_list = [
            'dob'
        ]

        sql_rows = self.convert_to_normal_date(sql_rows, convert_attribute_list, '%Y-%m-%d')

        return sql_rows

    def create_data(self, value = None):
        action = {}

        action['{}'.format(self.table_name)] = {
            'action': self.action_type.get('insert'),
            'command': (
                "INSERT INTO `{}` ( \
                `fullname`, \
                `email`, \
                `password`, \
                `nik`, \
                `dob`, \
                `gender`, \
                `identity`, \
                `identity_type`, \
                `user_role`, \
                `address`, \
                `avatar`, \
                `created_at`) VALUES".format(self.table_name) +
                " ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}', NOW())".format(value.get('fullname'), value.get('email'), value.get('password'), value.get('nik'), value.get('dob'), value.get('gender'), value.get('identity'), value.get('identity_type'), value.get('user_role'), value.get('address'), value.get('avatar'))
            )
        }

        self.execute_command(
            action
        )

    def update_data(self, value):
        action = {}

        action['{}'.format(self.table_name)] = {
            'action': self.action_type.get('update'),
            'command': (
                "UPDATE `{}` SET {}, updated_at=NOW() WHERE id={}".format(self.table_name, value.get('data'), value.get('id'))
            )
        }

        self.execute_command(
            action
        )

    def delete_data(self, value):
        action = {}

        action['{}'.format(self.table_name)] = {
            'action': self.action_type.get('delete'),
            'command': (
                "DELETE FROM `{}` WHERE id={}".format(self.table_name, value)
            )
        }

        self.execute_command(
            action
        )