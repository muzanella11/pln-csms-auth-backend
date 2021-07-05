from app.core.controllers import BaseControllers
from app.services.privilege_type_service import PrivilegeTypeService
import re

class PrivilegeTypes(BaseControllers):
    request = None

    TABLES = {}

    def __init__(self, request = None):
        super(PrivilegeTypes, self).__init__()

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

        data_sql = PrivilegeTypeService().generate_privilege_type_list(data_model)

        data['data'] = data_sql.get('data')
        data['total_data'] = data_sql.get('total_rows')

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

        data_sql = PrivilegeTypeService().generate_privilege_type_detail(columns, value)

        data['data'] = data_sql.get('data')
        data['total_data'] = data_sql.get('total_rows')

        return self.create_response(data)

    def create_data(self):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json
        name = request_data.get('name')
        label = request_data.get('label')
        description = request_data.get('description')
        
        data_model = {
            'name': name,
            'label': label,
            'description': description
        }

        PrivilegeTypeService().create_privilege_type(data_model)

        return self.create_response(data)

    def update_data(self, privilege_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        request_data = self.request.json

        name = request_data.get('name')
        label = request_data.get('label')
        description = request_data.get('description')

        queries = "name='{}', label='{}', description='{}'".format(name, label, description)
        
        data_model = {
            'id': privilege_id,
            'data': queries
        }

        PrivilegeTypeService().update_privilege_type(data_model)

        return self.create_response(data)

    def delete_data(self, privilege_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        PrivilegeTypeService().delete_privilege_type(privilege_id)

        return self.create_response(data)
        