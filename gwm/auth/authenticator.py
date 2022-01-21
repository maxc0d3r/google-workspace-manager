import os
from dotenv import load_dotenv
from google.auth import credentials

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.user',
    'https://www.googleapis.com/auth/admin.directory.group',
    'https://www.googleapis.com/auth/admin.directory.domain',
    'https://www.googleapis.com/auth/siteverification'
]

load_dotenv()

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json',SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.getenv('OAUTH_CREDENTIALS'),SCOPES)
            creds = flow.run_local_server(host='localhost',port=9000,redirect_uri_trailing_slash=False)
        with open('token.json','w') as token:
            token.write(creds.to_json())
    return creds
