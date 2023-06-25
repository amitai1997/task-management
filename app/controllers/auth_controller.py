
from app import oauth
from flask import Blueprint, redirect, session, url_for
from urllib.parse import urlencode
from app.utils.auth import require_auth
from app.security.guards import authorization_guard, permissions_guard
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login')
def login():
    return oauth.auth0.authorize_redirect(redirect_uri=url_for('auth.callback', _external=True))


@auth_bp.route('/callback')
def callback():
    token = oauth.auth0.authorize_access_token()
    resp = oauth.auth0.get('userinfo')
    user_info = resp.json()
    session['profile'] = user_info
    session["user"] = token
    session['jwt_payload'] = user_info
    session['user_id'] = user_info['sub']
    session['roles'] = user_info.get('roles', [])
    session['permissions'] = [],
    session['audience'] = user_info.get('aud', '')

    # Redirect to the desired route after successful authentication
    return redirect("/")


@auth_bp.route('/logout')
def logout():
    session.clear()
    params = {'returnTo': url_for('index', _external=True), 'client_id': oauth.auth0.client_id}
    return redirect(oauth.auth0.api_base_url + '/v2/logout?' + urlencode(params))


@auth_bp.route("/protected")
@authorization_guard
@permissions_guard(['read:data'])
def protected_route():
    return "This is a protected route!."
