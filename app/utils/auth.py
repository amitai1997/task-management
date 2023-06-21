import os
from flask import Blueprint, redirect, session, url_for
from authlib.integrations.flask_client import OAuth
from app import oauth
from dotenv import load_dotenv
from app import app

load_dotenv()

auth_bp = Blueprint('auth', __name__)

auth0_domain = os.getenv('AUTH0_DOMAIN')
auth0_client_id = os.getenv('AUTH0_CLIENT_ID')
auth0_client_secret = os.getenv('AUTH0_CLIENT_SECRET')


def configure_oauth(app):
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


@auth_bp.route('/login')
def login():
    return oauth.auth0.authorize_redirect(redirect_uri=url_for('auth.callback', _external=True))


@auth_bp.route('/callback')
def callback():
    token = oauth.auth0.authorize_access_token()
    # Handle the token and perform any necessary actions
    # e.g., store the token in the session, retrieve user information, etc.
    return redirect(url_for('index'))


@auth_bp.route('/logout')
def logout():
    session.clear()
    params = {'returnTo': url_for('index', _external=True), 'client_id': app.config['AUTH0_CLIENT_ID']}
    return redirect(oauth.auth0.api_base_url + '/v2/logout?' + urlencode(params))
