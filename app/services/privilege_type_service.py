from app import app
from app.models.model_privilege_types import ModelPrivilegeTypes
from app.core.secrets import Secrets

class PrivilegeTypeService(object):
    config = {}
    base_result = {
        'data': None,
        'total_data': 0
    }
    
    def __init__(self, config = None):
        super(PrivilegeTypeService, self).__init__()

        if config:
            self.config = config

    def generate_privilege_type_list(self, data_model = None):
        data_sql = getattr(ModelPrivilegeTypes(data_model), 'get_list')()

        raw_data = data_sql.get('data')

        # if raw_data:
        #     for item_raw_data in raw_data:
                # For mapping data before serve

        self.base_result['data'] = raw_data
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def generate_privilege_type_detail(self, columns = None, value = None):
        data_sql = getattr(ModelPrivilegeTypes(), 'get_detail_by')(columns, value)

        raw_data = data_sql.get('data')

        # if raw_data:
        #     # For mapping data before serve

        self.base_result['data'] = raw_data
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def create_privilege_type(self, data_model = None):
        # To Do :: Create validation here
        getattr(ModelPrivilegeTypes(), 'create_data')(data_model)

    def update_privilege_type(self, data_model = None):
        # To Do :: Create validation here
        getattr(ModelPrivilegeTypes(), 'update_data')(data_model)

    def delete_privilege_type(self, privilege_type_id = None):
        # To Do :: Create validation here
        getattr(ModelPrivilegeTypes(), 'delete_data')(privilege_type_id)