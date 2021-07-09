from app import app
from app.services.user_role_service import UserRoleService
from app.services.identity_type_service import IdentityTypeService
from app.models.model_users import ModelUsers
from app.core.secrets import Secrets

class UserService(object):
    config = {}
    base_result = {
        'data': None,
        'total_data': 0
    }
    
    def __init__(self, config = None):
        super(UserService, self).__init__()

        if config:
            self.config = config

    def generate_user_list(self, data_model = None):
        data_sql = getattr(ModelUsers(data_model), 'get_list')()

        raw_data = data_sql.get('data')

        if raw_data:
            for item_raw_data in raw_data:
                # Get User Role
                user_role_id = item_raw_data.get('user_role')

                content_data = UserRoleService().generate_user_roles_detail('id', user_role_id)
                content_data = content_data.get('data')
                
                item_raw_data['user_role'] = content_data

                # Get Identity Type
                identity_type_id = item_raw_data.get('identity_type')

                content_data = IdentityTypeService().generate_identity_type_detail('id', identity_type_id)
                content_data = content_data.get('data')
                
                item_raw_data['identity_type'] = content_data

        self.base_result['data'] = raw_data
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def generate_user_detail(self, columns = None, value = None, show_password = False):
        data_sql = getattr(ModelUsers(), 'get_detail_by')(columns, value, show_password)

        raw_data = data_sql.get('data')

        if raw_data:
            # Get User Role
            user_role_id = raw_data.get('user_role')

            content_data = UserRoleService().generate_user_roles_detail('id', user_role_id)
            content_data = content_data.get('data')

            raw_data['user_role'] = content_data

            # Get Identity Type
            identity_type_id = raw_data.get('identity_type')

            content_data = IdentityTypeService().generate_identity_type_detail('id', identity_type_id)
            content_data = content_data.get('data')

            raw_data['identity_type'] = content_data

        self.base_result['data'] = raw_data
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def create_user(self, data_model = None):
        # Encrypt password
        password = Secrets({
            'value': data_model['password']
        }).encrypt()

        data_model['password'] = password

        # To Do :: Create validation here
        getattr(ModelUsers(), 'create_data')(data_model)

    def update_user(self, data_model = None):
        # To Do :: Create validation here
        getattr(ModelUsers(), 'update_data')(data_model)

    def delete_user(self, user_id = None):
        # To Do :: Create validation here
        getattr(ModelUsers(), 'delete_data')(user_id)