"""send-email sample for Microsoft Graph"""
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.
import mimetypes
import sys
import pprint


import flask
import requests

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
            response = requests.get('https://graph.microsoft.com/v1.0/me/drive/root/delta')
            response_json = pprint.pformat(response.data)
            print(response_json, file=sys.stdout)
            return flask.Response(status=200)
    else:
        return flask.Response(flask.request.get_json(), file=sys.stdout)

@APP.route('/api/v1/customer_info/remote_sql', methods=['GET', 'POST'])
def getapis():
    if flask.request.method == 'POST':
        if 'validationToken' in flask.request.values:
            print(flask.request.values.get('validationToken'), file=sys.stdout)
            return flask.Response(flask.request.values.get('validationToken'), status=200, mimetype='text/plain')
        else:
            print(flask.request.get_json(), file=sys.stdout)
            return flask.Response(status=200)
    else:
        return flask.Response(flask.request.get_json(), file=sys.stdout)

if __name__ == '__main__':
    APP.run()
