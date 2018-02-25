"""send-email sample for Microsoft Graph"""
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.
import mimetypes

import flask

APP = flask.Flask(__name__)
APP.debug = True
APP.secret_key = 'development'

@APP.route('/')
def homepage():
    """Render the home page."""
    return flask.Response('Homepage')

@APP.route('/getsubs')
def getsubs():
    if 'validationtoken' in flask.request.args:
        return flask.Response('Validated', status=200, mimetype='text/plain')
    else:
        return flask.Response('Request')

if __name__ == '__main__':
    APP.run()
