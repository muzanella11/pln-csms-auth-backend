from app import app
from app.services.privilege_type_service import PrivilegeTypeService
from app.models.model_user_roles import ModelUserRoles
from app.core.secrets import Secrets

class UserRoleService(object):
    config = {}
    base_result = {
        'data': None,
        'total_data': 0
    }
    
    def __init__(self, config = None):
        super(UserRoleService, self).__init__()

        if config:
            self.config = config

    def generate_user_roles_list(self, data_model = None):
        data_sql = getattr(ModelUserRoles(data_model), 'get_list')()

        raw_data = data_sql.get('data')

        if raw_data:
            for item_raw_data in raw_data:
                # Get Privilege Type
                privilege_type_id = item_raw_data.get('privilege_type')

                content_data = PrivilegeTypeService().generate_privilege_type_detail('id', privilege_type_id)
                content_data = content_data.get('data')
                
                item_raw_data['privilege_type'] = content_data

        self.base_result['data'] = raw_data
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def generate_user_roles_detail(self, columns = None, value = None):
        data_sql = getattr(ModelUserRoles(), 'get_detail_by')(columns, value)

        raw_data = data_sql.get('data')

        if raw_data:
            # Get Privilege Type
            privilege_type_id = raw_data.get('privilege_type')

            content_data = PrivilegeTypeService().generate_privilege_type_detail('id', privilege_type_id)
            content_data = content_data.get('data')

            raw_data['privilege_type'] = content_data

        self.base_result['data'] = raw_data
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def create_user_roles(self, data_model = None):
        # To Do :: Create validation here
        getattr(ModelUserRoles(), 'create_data')(data_model)

    def update_user_roles(self, data_model = None):
        # To Do :: Create validation here
        getattr(ModelUserRoles(), 'update_data')(data_model)

    def delete_user_roles(self, user_roles_id = None):
        # To Do :: Create validation here
        getattr(ModelUserRoles(), 'delete_data')(user_roles_id)