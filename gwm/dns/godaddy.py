import requests
import os

headers = {"Authorization": "sso-key {}:{}".format(os.getenv('GODADDY_API_KEY'),os.getenv('GODADDY_SECRET_KEY'))}

# The token is for CNAME record is a two word string with first word as name and second as value
def addDNSRecord(domain,token,ttl=600):
    recordName = token.split()[0]
    value = token.split()[1]
    print(recordName + " " + value)
    payload = [
        {
            'name': recordName, 
            'type': 'CNAME',
            'ttl': ttl, 
            'data':value
        }
    ]
    uri = os.getenv('GODADDY_BASE_URL') + '/v1/domains/{}/records'.format(domain) 
    response = requests.patch(uri, json=payload, headers=headers)
    if response.status_code == 200:
        return True
    return False
