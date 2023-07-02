import os
import json
from flask import session, request
import requests
from functools import wraps
from jose import jwt
from jose.exceptions import JWTError


class RBACAuthenticator:
    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.auth0_domain = os.environ.get('AUTH0_DOMAIN')
        self.auth0_client_id = os.environ.get('AUTH0_CLIENT_ID')
        self.auth0_client_secret = os.environ.get('AUTH0_CLIENT_SECRET')
        self.api_identifier = os.environ.get('API_IDENTIFIER')
        self.jwks_url = f'https://{os.environ.get("AUTH0_DOMAIN")}/.well-known/jwks.json'

    def requires_permission(self, permissions=[]):
        def decorator(f):
            @wraps(f)
            def decorated(*args, **kwargs):
                token = None
                if ('access_token' in session):
                    token = session['access_token']
                elif ('Authorization' in request.headers):
                    token = request.headers.get('Authorization')[7:]
                else:
                    return 'Access token not found.', 401

                # Retrieve and verify the key for signature verification
                jwks = self._get_jwks()
                key = self._get_key(token, jwks)

                try:
                    # Verify the token using the key
                    payload = jwt.decode(
                        token,
                        key,
                        algorithms=['RS256'],
                        audience=self.api_identifier,  # Verify the audience claim
                        options={"verify_signature": True}
                    )

                    # Verify token permissions for the protected endpoint
                    if 'permissions' not in payload:
                        return 'Insufficient permissions.', 403

                    user_permissions = payload['permissions']

                    if not permissions:
                        return f(*args, **kwargs)

                    for permission in permissions:
                        if permission not in user_permissions:
                            return 'Insufficient permissions.', 403

                    return f(*args, **kwargs)
                except JWTError:
                    return 'Invalid token or audience.', 401
            return decorated
        return decorator

    def _get_jwks(self):
        response = requests.get(self.jwks_url)
        jwks = json.loads(response.text)
        return jwks

    def _get_key(self, token, jwks):
        headers = jwt.get_unverified_header(token)
        kid = headers.get('kid')

        for key in jwks['keys']:
            if key['kid'] == kid:
                return key

        raise ValueError('Unable to find appropriate key.')
