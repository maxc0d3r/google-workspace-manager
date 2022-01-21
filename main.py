"""
Usage:
    main.py domains list [--customer-id=<id>]
    main.py domains ( get | delete ) <domain_name> [--customer-id=<id>]
    main.py domains add <domain> [FILE] [--customer-id=<id>]
    main.py domains bulkadd FILE [--customer-id=<id>]
    main.py users list [domain] [--customer-id=<id>]
    main.py users ( get | delete) <email> [domain] [--customer-id=<id>]
    main.py users add FILE [domain] [--customer-id=<id>]
    main.py users bulkadd FILE [domain] [--customer-id=<id>]
    main.py (-h | --help)
    main.py (-V | --version)

Arguments:
  FILE        optional input file
  DOMAIN      optional domain 

Options:
    -h --help           Show this screen
    -v --version        Show version
    --customer-id=<id>  Google Workspace Customer ID for primary domain
"""

from docopt import docopt
import os
import json
import gwm.directory.domains
import gwm.directory.users
import gwm.directory.groups
from gwm.directory.domains import list_domains, add_domain, delete_domain

APP_VERSION='0.0.0'

def main(args):
    customer_id = args['--customer-id'] or os.getenv('CUSTOMER_ID')
    if args['domains']:
        if args['list']:
            domains = list_domains(customer_id)
            print(json.dumps(domains,indent=1))
        if args['add']:
            if args['FILE']:
                with open(args['FILE'],'r') as f:
                    body = json.load(f)
                    response = add_domain(customer_id, body)
            else:
                response = add_domain(customer_id, {"domainName":args['<domain>']})
            print(json.dumps(response,indent=1))
        if args['get']:
            pass
        if args['delete']:
            pass
    elif args['users']:
        pass
    else:
        pass

if __name__ == "__main__":
    arguments = docopt(__doc__, version='Google Workspace Manager {}'.format(APP_VERSION))
    main(arguments)
