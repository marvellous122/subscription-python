"""send-email sample for Microsoft Graph"""
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.
import mimetypes
import sys


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
    print(flask.request.args, file=sys.stdout)
    if 'validationToken' in flask.request.args:
        print(flask.request.args['validationToken'], file=sys.stdout)
        with open("test.txt","wb") as fo:
   	        fo.write("Validated".encode())
        return flask.Response(flask.request.args['validationToken'], status=200, mimetype='text/plain')
    else:
        print('failed', file=sys.stdout)
        with open("test.txt","wb") as fo:
   	        fo.write("Request".encode())
        return flask.Response('Request')

if __name__ == '__main__':
    APP.run()
