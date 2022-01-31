from urllib import request
from googleapiclient.discovery import build
import gwm.auth.authenticator as auth

def list_users(domain):
    adminService = build('admin','directory_v1',credentials=auth.authenticate())

    results = adminService.users().list(domain=domain,orderBy='email').execute()
    users = results.get('users', [])
    return {"data": {"users": users }}

def get_user(domain,email):
    pass

def add_user(request_body):
    adminService = build('admin','directory_v1',credentials=auth.authenticate())

    result = adminService.users().insert(body=request_body).execute()
    return(result)

def delete_user(domain,customer_id,email):
    pass

def update_user(domain,customer_id,request_body):
    pass
