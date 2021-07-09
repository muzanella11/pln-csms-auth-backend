from app import app
from app.services.user_service import UserService
from app.services.user_session_service import UserSessionService
from app.libraries.random_string import RandomString
from app.libraries.token_handler import TokenHandler
from app.core.secrets import Secrets
from datetime import date

class AuthenticationService(object):
    config = {}
    base_result = {
        'data': None,
        'total_data': 0
    }
    SESSION_TOKEN_LENGTH = 11
    
    def __init__(self, config = None):
        super(AuthenticationService, self).__init__()

        if config:
            self.config = config

    def generate_session_token(self):
        result = ''
        amount = 8
        token = ''
        
        for item in range(amount):
            token = RandomString({
                'key_length': self.SESSION_TOKEN_LENGTH
            }).run()

            if result == '':
                result = token
            else:
                result = '{}-{}'.format(result, token)

        return result.upper()

    def generate_session_expired(self):
        # session_expired = TokenHandler({
        #     'time_by': 'hours',
        #     'time_by_value': 48,
        #     'session_time': session_user_created
        # }).create_expired_time()

        return date.today()

    def create_session(self):
        session_token = self.generate_session_token()

        UserSessionService().create_user_session({
            'token': session_token
        })

        session_user_id = app.mysql_lastrowid

        session_user_detail = UserSessionService().generate_user_session_detail('id', session_user_id)
        session_user_created = session_user_detail['data']['created_at']
        
        session_expired = TokenHandler({
            'time_by': 'hours',
            'time_by_value': 48,
            'session_time': session_user_created
        }).create_expired_time()

        queries = "expired='{}'".format(session_expired)
        
        data_model_session = {
            'id': session_user_id,
            'data': queries
        }

        UserSessionService().update_user_session(data_model_session)

        return session_token
