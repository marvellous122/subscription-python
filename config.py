"""Configuration settings for running the Python auth samples locally.

In a production deployment, this information should be saved in a database or
other secure storage mechanism.
"""

CLIENT_ID = '18dc9c86-97a5-437c-9633-144b2b58dfe8'
CLIENT_SECRET = 'ilFMVQ65_^mmaxuZKM126(]'
TENANT_KEY = 'edbc9891-0028-40dc-85f5-e975817aacd7'
DRIVE_ID = 'b!gxrWhwkPiUyAY9Eg1m2Q9N2fK1qOkDxBqEBp7YFQ1Gxolc6ts_J6QonfoofL9q0U'
DRIVE_ID_USER2 = 'b!avGeFcbVzUSf6ByXZi8DxAG48vPxJkZFlIB1FE5Xedg1cmoSbFbWSYWKDPYu-X4i'
REDIRECT_URI = 'https://avanandev-hugo.avanan.net/login/authorized'
# REDIRECT_URI = 'http://localhost:5000/login/authorized'

# AUTHORITY_URL ending determines type of account that can be authenticated:
# /organizations = organizational accounts only
# /consumers = MSAs only (Microsoft Accounts - Live.com, Hotmail.com, etc.)
# /common = allow both types of accounts
AUTHORITY_URL = 'https://login.microsoftonline.com/common'

AUTH_ENDPOINT = '/oauth2/v2.0/authorize'
TOKEN_ENDPOINT = '/oauth2/v2.0/token'

RESOURCE = 'https://graph.microsoft.com/'
API_VERSION = 'v1.0'
SCOPES = ['User.Read', 'Mail.Send', 'Files.ReadWrite'] # Add other scopes/permissions as needed.

# This code can be removed after configuring CLIENT_ID and CLIENT_SECRET above.
if 'ENTER_YOUR' in CLIENT_ID or 'ENTER_YOUR' in CLIENT_SECRET:
    print('ERROR: config.py does not contain valid CLIENT_ID and CLIENT_SECRET')
    import sys
    sys.exit(1)
