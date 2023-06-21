from app import oauth
from flask import Blueprint, redirect, session, url_for
from urllib.parse import urlencode
from app import app

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login')
def login():
    return oauth.auth0.authorize_redirect(redirect_uri=url_for('auth.callback', _external=True))


@auth_bp.route('/callback')
def callback():
    token = oauth.auth0.authorize_access_token()
    resp = oauth.auth0.get('userinfo')
    resp.raise_for_status()
    user_info = resp.json()
    session['profile'] = user_info
    session["user"] = token

    # Redirect to the desired route after successful authentication
    return redirect("/")


@auth_bp.route('/logout')
def logout():
    session.clear()
    params = {'returnTo': url_for('index', _external=True), 'client_id': oauth.auth0.client_id}
    return redirect(oauth.auth0.api_base_url + '/v2/logout?' + urlencode(params))
