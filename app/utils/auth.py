import os
from app import oauth
from dotenv import load_dotenv
from functools import wraps
from flask import session, jsonify
from authlib.jose import jwt

from os import environ as env

from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify
from authlib.integrations.flask_oauth2 import ResourceProtector
from app.utils.validator import Auth0JWTBearerTokenValidator
from app import app

load_dotenv()

require_auth = ResourceProtector()

auth0_domain = os.getenv('AUTH0_DOMAIN')
auth0_client_id = os.getenv('AUTH0_CLIENT_ID')
auth0_client_secret = os.getenv('AUTH0_CLIENT_SECRET')
validator_audience = os.getenv('VALIDATOR_AUDIENCE')


def register_oauth(app):
    oauth.init_app(app)

    oauth.register(
        'auth0',
        client_id=auth0_client_id,
        client_secret=auth0_client_secret,
        api_base_url=f'https://{auth0_domain}',
        access_token_url=f'https://{auth0_domain}/oauth/token',
        authorize_url=f'https://{auth0_domain}/authorize',
        client_kwargs={
            'scope': 'openid profile email',
        },
        server_metadata_url=f'https://{auth0_domain}/.well-known/openid-configuration',
    )

    validator = Auth0JWTBearerTokenValidator(
        f'{auth0_domain}',
        validator_audience
    )
    require_auth.register_token_validator(validator)
