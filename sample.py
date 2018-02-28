"""send-email sample for Microsoft Graph"""
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.
import base64
import mimetypes
import os
import pprint
import uuid
import urllib
import sys

import flask
import requests
from flask_oauthlib.client import OAuth

import config

APP = flask.Flask(__name__)
APP.debug = True
APP.secret_key = 'development'
OAUTH = OAuth(APP)
MSGRAPH = OAUTH.remote_app(
    'microsoft',
    consumer_key=config.CLIENT_ID,
    consumer_secret=config.CLIENT_SECRET,
    request_token_params={'scope': config.SCOPES},
    base_url=config.RESOURCE + config.API_VERSION + '/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url=config.AUTHORITY_URL + config.TOKEN_ENDPOINT,
    authorize_url=config.AUTHORITY_URL + config.AUTH_ENDPOINT)

@APP.route('/')
def homepage():
    """Render the home page."""
    return flask.Response('Homepage')

@APP.route('/login')
def login():
    """Prompt user to authenticate."""
    flask.session['state'] = str(uuid.uuid4())
    return MSGRAPH.authorize(callback=config.REDIRECT_URI, state=flask.session['state'])

@APP.route('/login/authorized')
def authorized():
    """Handler for the application's Redirect Uri."""
    if str(flask.session['state']) != str(flask.request.args['state']):
        raise Exception('state returned to redirect URL does not match!')
    response = MSGRAPH.authorized_response()
    flask.session['access_token'] = response['access_token']
    return flask.redirect('/subscription')

@APP.route('/subscription')
def subscription():
    # response = MSGRAPH.post('subscriptions',
    #                         headers=request_headers(),
    #                         data={
    #                             'changeType': 'updated',
    #                             'notificationUrl': 'https://avanandev-hugo.avanan.net/getsubs',
    #                             'resource': '/me/drive/root',
    #                             'expirationDateTime': '2018-02-28T11:23:00.000Z'
    #                         },
    #                         format='json')
    # response_json = pprint.pformat(response.data)
    # response_json = None if response_json == "b''" else response_json
    # return flask.Response(response_json)
    return flask.Response('OK')

@APP.route('/getsubs', methods=['GET', 'POST'])
def getsubs():
    if flask.request.method == 'POST':
        if 'validationToken' in flask.request.values:
            print(flask.request.values.get('validationToken'), file=sys.stdout)
            return flask.Response(flask.request.values.get('validationToken'), status=200, mimetype='text/plain')
        else:
            print(flask.request.get_json()['value'][0]['resource'], file=sys.stdout)
            head = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            parameters = {
                'client_id': '18dc9c86-97a5-437c-9633-144b2b58dfe8',
                'scope': 'Files.ReadWrite',
                'client_secret': 'ilFMVQ65_^mmaxuZKM126(]',
                'grant_type': 'client_credentials'
            }
            raw_data = urllib.parse.urlencode(parameters)
            print('OK')
            response = requests.post('https://login.microsoftonline.com/common/oauth2/v2.0/token', data=raw_data, headers=head)
            access_type = response.json()['token_type']
            access_token = response.json()['access_token']
            get_head = {
                'Authorization': access_type + access_token
            }
            get_response = requests.get('https://graph.microsoft.com/v1.0/drives/b!gxrWhwkPiUyAY9Eg1m2Q9N2fK1qOkDxBqEBp7YFQ1Gxolc6ts_J6QonfoofL9q0U/root', headers=get_head)
            print(get_response.json(), file=sys.stdout)
            return flask.Response(status=200)
    else:
        return flask.Response(flask.request.get_json(), file=sys.stdout)

@MSGRAPH.tokengetter
def get_token():
    """Called by flask_oauthlib.client to retrieve current access token."""
    return (flask.session.get('access_token'), '')

def request_headers(headers=None):
    """Return dictionary of default HTTP headers for Graph API calls.
    Optional argument is other headers to merge/override defaults."""
    default_headers = {'SdkVersion': 'sample-python-flask',
                       'x-client-SKU': 'sample-python-flask',
                       'access-token': get_token(),
                       'client-request-id': str(uuid.uuid4()),
                       'return-client-request-id': 'true'}
    if headers:
        default_headers.update(headers)
    return default_headers

if __name__ == '__main__':
    APP.run()
