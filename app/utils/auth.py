import os
from app import oauth
from dotenv import load_dotenv


load_dotenv()


auth0_domain = os.getenv('AUTH0_DOMAIN')
auth0_client_id = os.getenv('AUTH0_CLIENT_ID')
auth0_client_secret = os.getenv('AUTH0_CLIENT_SECRET')


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
