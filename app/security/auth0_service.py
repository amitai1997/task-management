from http import HTTPStatus
from flask import session
import jwt
# from app.utils.auth import json_abort


class Auth0Service:
    """Perform JSON Web Token (JWT) validation using PyJWT"""

    def __init__(self):
        self.issuer_url = None
        self.audience = None
        self.algorithm = 'RS256'
        self.jwks_uri = None

    def initialize(self, auth0_domain, auth0_audience):
        self.issuer_url = f'https://{auth0_domain}/'
        self.jwks_uri = f'{self.issuer_url}.well-known/jwks.json'
        self.audience = auth0_audience

    def get_signing_key(self, token):
        try:
            jwks_client = jwt.PyJWKClient(self.jwks_uri)

            return jwks_client.get_signing_key_from_jwt(token).key
        except Exception as error:
            # self.json_abort(HTTPStatus.INTERNAL_SERVER_ERROR, {
            #     "error": "signing_key_unavailable",
            #     "error_description": error.__str__(),
            #     "message": "Unable to verify credentials"
            # })
            return error

    def validate_jwt(self, token):
        try:
            jwt_signing_key = self.get_signing_key(token)

            payload = jwt.decode(
                token,
                jwt_signing_key,
                algorithms=self.algorithm,
                audience=session['user']['userinfo']['aud'],
                issuer=self.issuer_url,
                client_kwargs={
                    'scope': 'openid profile email',
                },
            )
        except Exception as error:
            # self.json_abort(HTTPStatus.UNAUTHORIZED, {
            #     "error": "invalid_token",
            #     "error_description": error.__str__(),
            #     "message": "Bad credentials"
            # })
            # return
            return error

        return payload


# auth0_service = Auth0Service()
