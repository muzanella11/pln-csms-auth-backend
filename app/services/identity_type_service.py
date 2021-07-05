from app import app
from app.models.model_identity_types import ModelIdentityTypes
from app.core.secrets import Secrets

class IdentityTypeService(object):
    config = {}
    base_result = {
        'data': None,
        'total_data': 0
    }
    
    def __init__(self, config = None):
        super(IdentityTypeService, self).__init__()

        if config:
            self.config = config

    def generate_identity_type_list(self, data_model = None):
        data_sql = getattr(ModelIdentityTypes(data_model), 'get_list')()

        raw_data = data_sql.get('data')

        # if raw_data:
        #     for item_raw_data in raw_data:
                # For mapping data before serve

        self.base_result['data'] = raw_data
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def generate_identity_type_detail(self, columns = None, value = None):
        data_sql = getattr(ModelIdentityTypes(), 'get_detail_by')(columns, value)

        raw_data = data_sql.get('data')

        # if raw_data:
        #     # For mapping data before serve

        self.base_result['data'] = raw_data
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def create_identity_type(self, data_model = None):
        # To Do :: Create validation here
        getattr(ModelIdentityTypes(), 'create_data')(data_model)

    def update_identity_type(self, data_model = None):
        # To Do :: Create validation here
        getattr(ModelIdentityTypes(), 'update_data')(data_model)

    def delete_identity_type(self, identity_type_id = None):
        # To Do :: Create validation here
        getattr(ModelIdentityTypes(), 'delete_data')(identity_type_id)