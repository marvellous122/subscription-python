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

@APP.route('/')
def homepage():
    """Render the home page."""
    return flask.Response('Homepage')

@APP.route('/getsubs', methods=['GET', 'POST'])
def getsubs():
    if flask.request.method == 'POST':
        if 'validationToken' in flask.request.values:
            print(flask.request.values.get('validationToken'), file=sys.stdout)
            return flask.Response(flask.request.values.get('validationToken'), status=200, mimetype='text/plain')
        else:
            head = {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            parameters = {
                'client_id': '18dc9c86-97a5-437c-9633-144b2b58dfe8',
                'scope': 'https://graph.microsoft.com/.default',
                'client_secret': 'ilFMVQ65_^mmaxuZKM126(]',
                'grant_type': 'client_credentials'
            }
            raw_data = urllib.parse.urlencode(parameters)
            response = requests.post(
                'https://login.microsoftonline.com/edbc9891-0028-40dc-85f5-e975817aacd7/oauth2/v2.0/token',
                data=raw_data, headers=head)
            access_type = response.json()['token_type']
            access_token = response.json()['access_token']
            get_head = {
                'Authorization': access_type + " " + access_token
            }
            get_response = requests.get(
                'https://graph.microsoft.com/v1.0/drives/b!gxrWhwkPiUyAY9Eg1m2Q9N2fK1qOkDxBqEBp7YFQ1Gxolc6ts_J6QonfoofL9q0U/root/delta',
                headers=get_head)
            print(get_response.json(), file=sys.stdout)
            return flask.Response(status=200)
    else:
        return flask.Response(flask.request.get_json())

if __name__ == '__main__':
    APP.run()
