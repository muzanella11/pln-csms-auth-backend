from app.core.controllers import BaseControllers
from app.services.user_service import UserService
import re

class Users(BaseControllers):
    request = None

    TABLES = {}

    def __init__(self, request = None):
        super(Users, self).__init__()

        self.request = request

    def run(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': []
        }

        return self.create_response(data)

    def get_list(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': [],
            'total_data': 0
        }

        data_model = {
            'type': 'list',
            'pagination': True,
            'filter': self.request.args
        }

        data_sql = UserService().generate_user_list(data_model)

        data['data'] = data_sql.get('data')
        data['total_data'] = data_sql.get('total_data')

        return self.create_response(data)

    def get_detail(self, columns = None, value = None):
        if columns == "error":
            return self.create_response({
                'code': 400,
                'messages': 'Bad Request'
            })

        data = {
            'code': 200,
            'message': 'Success',
            'data': {},
            'total_data': 0
        }

        data_sql = UserService().generate_user_detail(columns, value)

        data['data'] = data_sql.get('data')
        data['total_data'] = data_sql.get('total_data')

        return self.create_response(data)

    def create_data(self):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json
        fullname = request_data.get('fullname')
        email = request_data.get('email')
        password = request_data.get('password')
        nik = request_data.get('nik')
        dob = request_data.get('dob')
        gender = request_data.get('gender')
        identity = request_data.get('identity')
        identity_type = request_data.get('identity_type')
        user_role = request_data.get('user_role')
        address = request_data.get('address')
        avatar = request_data.get('avatar')
        
        data_model = {
            'fullname': fullname,
            'email': email,
            'password': password,
            'nik': nik,
            'dob': dob,
            'gender': gender,
            'identity': identity,
            'identity_type': identity_type,
            'user_role': user_role,
            'address': address,
            'avatar': avatar
        }

        UserService().create_user(data_model)

        return self.create_response(data)

    def update_data(self, privilege_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json

        fullname = request_data.get('fullname')
        email = request_data.get('email')
        nik = request_data.get('nik')
        dob = request_data.get('dob')
        gender = request_data.get('gender')
        identity = request_data.get('identity')
        identity_type = request_data.get('identity_type')
        user_role = request_data.get('user_role')
        address = request_data.get('address')
        avatar = request_data.get('avatar')

        queries = "fullname='{}', \
            email='{}', \
            nik='{}', \
            dob='{}', \
            gender='{}', \
            identity='{}', \
            identity_type='{}', \
            user_role='{}', \
            address='{}', \
            avatar='{}'".format(fullname, email, nik, dob, gender, identity, identity_type, user_role, address, avatar)
        
        data_model = {
            'id': privilege_id,
            'data': queries
        }

        UserService().update_user(data_model)

        return self.create_response(data)

    def delete_data(self, privilege_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        UserService().delete_user(privilege_id)

        return self.create_response(data)
        