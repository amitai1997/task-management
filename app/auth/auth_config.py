from flask import Blueprint, redirect, url_for, request, session
import requests
from app import authenticator


class AuthBlueprint(Blueprint):
    def __init__(self, name, import_name, url_prefix):
        super().__init__(name, import_name, url_prefix=url_prefix)

        self.auth0_domain = authenticator.auth0_domain
        self.auth0_client_id = authenticator.auth0_client_id
        self.auth0_client_secret = authenticator.auth0_client_secret
        self.api_identifier = authenticator.api_identifier

        self.add_url_rules()

    def add_url_rules(self):
        self.add_url_rule('/login', methods=['GET'],
                          view_func=self.login)
        self.add_url_rule('/login/callback', methods=['GET'],
                          view_func=self.login_callback)
        self.add_url_rule('/logout', methods=['GET'],
                          view_func=self.logout)
        self.add_url_rule('/logout/callback', methods=['GET'],
                          view_func=self.logout_callback)
        self.add_url_rule('/protected', methods=['GET'],
                          view_func=self.protected)

    def login(self):
        redirect_uri = request.base_url + '/callback'
        return self.redirect_to_auth0_login(redirect_uri)

    def login_callback(self):
        code = request.args.get('code')
        token_data = self.exchange_code_for_token(code)

        if 'access_token' in token_data:
            session['access_token'] = token_data['access_token']
            return 'Logged in successfully!'

        return 'Login failed.'

    def logout(self):
        session.clear()  # Clear the session data

        # Redirect the user to the Auth0 logout endpoint
        logout_url = f"https://{self.auth0_domain}/v2/logout"
        return redirect(logout_url)

    def logout_callback(self):
        return redirect(url_for('index'))

    def index():
        return redirect('/')

    @authenticator.requires_permission(['read:data', 'write:data'])
    def protected(self):
        # Retrieve access token from session
        token = session['access_token']
        headers = {'Authorization': f'Bearer {token}'}

        # Make a request to the protected endpoint
        response = requests.get(self.api_identifier + '/protected', headers=headers)

        if response.status_code == 200:
            return 'Access granted.'
        else:
            return 'Access denied.'

    def redirect_to_auth0_login(self, redirect_uri):
        return redirect(f'https://{self.auth0_domain}/authorize?audience={self.api_identifier}&response_type=code&client_id={self.auth0_client_id}&redirect_uri={redirect_uri}')

    def exchange_code_for_token(self, code):
        token_url = f'https://{self.auth0_domain}/oauth/token'
        payload = {
            'grant_type': 'authorization_code',
            'client_id': self.auth0_client_id,
            'client_secret': self.auth0_client_secret,
            'code': code,
            'redirect_uri': request.base_url
        }
        response = requests.post(token_url, json=payload)
        return response.json()
