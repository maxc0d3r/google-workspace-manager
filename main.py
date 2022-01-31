"""
Usage:
    main.py domains list 
    main.py domains add [--body=<request_body>] [--file=<input_file>]
    main.py users list [--domain=<domain_name>]
    main.py users add [--body=<request_body>] [--file=<input_file>]
    main.py (-h | --help)
    main.py (-V | --version)

Options:
    -h --help               Show this screen
    -v --version            Show version
    --body=<request_body>   Request body in JSON format
    --domain=<domain_name>  Domain name
    --file=<input_file>     JSON file
"""

from docopt import docopt
import csv
import os
import json
import random
import string
import gwm.directory.domains
import gwm.directory.users
import gwm.directory.groups
from gwm.directory.domains import list_domains, add_domain, delete_domain
from gwm.directory.users import list_users, add_user, delete_user

APP_VERSION='0.0.0'

def generate_password():
    source = string.ascii_letters + string.digits
    password = ''.join((random.choice(source) for i in range(10)))
    return password

def main(args):
    customer_id = os.getenv('CUSTOMER_ID')
    if args['domains']:
        if args['list']:
            domains = list_domains(customer_id)
            print(json.dumps(domains,indent=1))
        elif args['add']:
            if args['--file']:
                with open(args['--file'],'r') as f:
                    body = json.load(f)
                    response = add_domain(customer_id, body)
            else:
                response = add_domain(customer_id, json.loads(args['--body']))
            print(json.dumps(response,indent=1))
        elif args['get']:
            pass
        elif args['delete']:
            pass
    elif args['users']:
        if args['list']:
            users = list_users(args['--domain'])
            print(json.dumps(users,indent=1))
        elif args['add']:
            if args['--file']:
                with open(args['--file'],'r') as f:
                    body = json.load(f)
                    response = add_user(body)
            else:
                request_body = json.loads(args['--body'])
                response = add_user(request_body)
            print(json.dumps(response,indent=1))
        elif args['get']:
            pass
        elif args['delete']:
            pass
    else:
        pass

if __name__ == "__main__":
    arguments = docopt(__doc__, version='Google Workspace Manager {}'.format(APP_VERSION))
    main(arguments)
