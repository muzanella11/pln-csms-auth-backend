from app.core.controllers import BaseControllers
from app.services.identity_type_service import IdentityTypeService
import re

class IdentityTypes(BaseControllers):
    request = None

    TABLES = {}

    def __init__(self, request = None):
        super(IdentityTypes, self).__init__()

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

        data_sql = IdentityTypeService().generate_identity_type_list(data_model)

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

        data_sql = IdentityTypeService().generate_identity_type_detail(columns, value)

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
        name = request_data.get('name')
        label = request_data.get('label')
        description = request_data.get('description')
        
        data_model = {
            'name': name,
            'label': label,
            'description': description
        }

        IdentityTypeService().create_identity_type(data_model)

        return self.create_response(data)

    def update_data(self, identity_type_id = None):
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
            'id': identity_type_id,
            'data': queries
        }

        IdentityTypeService().update_identity_type(data_model)

        return self.create_response(data)

    def delete_data(self, identity_type_id = None):
        data = {
            'code': 200,
            'message': 'Success',
            'total_data': 0
        }

        IdentityTypeService().delete_identity_type(identity_type_id)

        return self.create_response(data)
        