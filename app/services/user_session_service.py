from app import app
from app.models.model_user_session import ModelUserSession
from app.core.secrets import Secrets

class UserSessionService(object):
    config = {}
    base_result = {
        'data': None,
        'total_data': 0
    }
    
    def __init__(self, config = None):
        super(UserSessionService, self).__init__()

        if config:
            self.config = config

    def generate_user_session_list(self, data_model = None):
        data_sql = getattr(ModelUserSession(data_model), 'get_list')()

        raw_data = data_sql.get('data')

        # if raw_data:
        #     for item_raw_data in raw_data:
        #         # For Mapping

        self.base_result['data'] = raw_data
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def generate_user_session_detail(self, columns = None, value = None):
        data_sql = getattr(ModelUserSession(), 'get_detail_by')(columns, value)

        raw_data = data_sql.get('data')

        # if raw_data:
        #     # For Mapping

        self.base_result['data'] = raw_data
        self.base_result['total_data'] = data_sql.get('total_rows')

        return self.base_result

    def create_user_session(self, data_model = None):
        # To Do :: Create validation here
        getattr(ModelUserSession(), 'create_data')(data_model)

    def update_user_session(self, data_model = None):
        # To Do :: Create validation here
        getattr(ModelUserSession(), 'update_data')(data_model)

    def delete_user_session(self, user_session_id = None):
        # To Do :: Create validation here
        getattr(ModelUserSession(), 'delete_data')(user_session_id)