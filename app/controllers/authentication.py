from app.core.controllers import BaseControllers
from app.services.authentication_service import AuthenticationService
from app.services.user_service import UserService
from app.services.user_session_service import UserSessionService
from app.libraries.helpers import Helpers
import re
import copy

class Authentication(BaseControllers):
    request = None

    TABLES = {}

    base_result = {
        'code': 200,
        'message': 'Success',
        'data': None
    }

    def __init__(self, request = None):
        super(Authentication, self).__init__()

        self.request = request

    def run(self):
        data = {
            'code': 200,
            'message': 'Success',
            'data': []
        }

        return self.create_response(data)

    def signin(self):
        request_data = self.request.json
        identity_signin = request_data.get('identity_signin') # You can fill with email or username
        password = request_data.get('password')
        user_data = None

        if Helpers().is_email(identity_signin):
            # Signin by email
            data_sql = UserService().generate_user_detail('email', identity_signin, True)
            user_data = data_sql.get('data')

            if user_data:
                if password != Helpers().decrypt(user_data.get('password')):
                    errors = [
                        {
                            'field': 'identity_signin',
                            'messages': 'Credential not match'
                        },
                        {
                            'field': 'password',
                            'messages': 'Credential not match'
                        }
                    ]

                    return self.error_response(errors)

                del user_data['password']
            else:
                errors = [
                    {
                        'field': 'identity_signin',
                        'messages': 'Wrong email or username'
                    }
                ]

                return self.error_response(errors)
        else:
            # Signin by nip
            data_sql = UserService().generate_user_detail('nip', identity_signin, True)
            user_data = data_sql.get('data')

            if user_data:
                if password != Helpers().decrypt(user_data.get('password')):
                    errors = [
                        {
                            'field': 'identity_signin',
                            'messages': 'Credential not match'
                        },
                        {
                            'field': 'password',
                            'messages': 'Credential not match'
                        }
                    ]

                    return self.error_response(errors)
                
                del user_data['password']
            else:
                errors = [
                    {
                        'field': 'identity_signin',
                        'messages': 'Wrong email or username'
                    }
                ]

                return self.error_response(errors)

        session_token = AuthenticationService().create_session()
        user_id = user_data['id']

        queries = "session_token='{}'".format(
            session_token
        )
        
        data_model = {
            'id': user_id,
            'data': queries
        }

        UserService().update_user(data_model)

        result = copy.deepcopy(self.base_result)
        result['message'] = 'Success sign in'
        result['data'] = {
            'token': session_token
        }

        return self.create_response(result)

    def signout(self):
        request_data = self.request.json
        session_token = request_data.get('token')

        if not session_token:
            errors = [
                {
                    'messages': 'Token not found'
                }
            ]

            return self.error_response(errors)

        data_sql = UserService().generate_user_detail('session_token', session_token)
        user_data = data_sql.get('data')

        if not user_data:
            errors = [
                {
                    'messages': 'Wrong token'
                }
            ]

            return self.error_response(errors)

        user_id = user_data['id']

        queries = "session_token=''"
        
        data_model = {
            'id': user_id,
            'data': queries
        }

        # Clear session token
        UserService().update_user(data_model)

        result = copy.deepcopy(self.base_result)
        result['message'] = 'Success sign out'

        del result['data']

        return self.create_response(result)

    def whoami(self, token = None):
        whoami_data = UserSessionService().generate_user_session_detail('token', token)
        whoami_expired = None
        is_expired = True

        if not whoami_data['data']:
            errors = [
                {
                    'messages': 'Token not found'
                }
            ]

            return self.error_response(errors)

        if whoami_data['data']:
            whoami_expired = whoami_data['data']['expired']
            is_expired = Helpers().check_expired(whoami_expired)
            user_data = None

            if not is_expired:
                user_data_sql = UserService().generate_user_detail('session_token', token)

                user_data = user_data_sql.get('data')
        
        result = copy.deepcopy(self.base_result)
        result['message'] = 'Success'
        result['data'] = {
            'is_expired': is_expired,
            'expired': whoami_expired,
            'whoami': user_data
        }

        return self.create_response(result)
