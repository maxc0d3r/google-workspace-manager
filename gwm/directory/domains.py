from urllib import request
from googleapiclient.discovery import build
import gwm.auth.authenticator as auth
from time import sleep
from gwm.dns.godaddy import addDNSRecord

def getDomainVerificationToken(domain):
    verificationService = build(serviceName='siteVerification',version='v1',credentials=auth.authenticate())

    response = verificationService.webResource().getToken(
        body={
            "site": {
                "type": "INET_DOMAIN",
                "identifier": domain
            },
            "verificationMethod": "DNS_CNAME"
        }).execute()
    token = response["token"]
    return token

def verifyDomain(domain):
    verificationService = build(serviceName='siteVerification',version='v1',credentials=auth.authenticate())
    resource = verificationService.webResource().insert(
        verificationMethod="DNS_CNAME",
        body={
            "site": {
            "type": "INET_DOMAIN",
            "identifier": domain
        },
        "owners": ["tech@10000companiesin10years.com"]
    }).execute()
    print("Verified domain - {}".format(domain))

def list_domains(customer_id):
    admin_service = build('admin','directory_v1',credentials=auth.authenticate())
    query = admin_service.domains().list(customer=customer_id).execute()
    domains = query.get('domains', [])
    return {"data": {"domains": domains }}


def add_domain(customer_id,request_body):
    admin_service = build('admin','directory_v1',credentials=auth.authenticate())
    query = admin_service.domains().insert(customer=customer_id,body=request_body).execute()
    verification_token = getDomainVerificationToken(request_body['domainName'])
    print(request_body['domainName'])
    print(verification_token)
    query['verificationToken'] = verification_token
    addDNSRecord(request_body['domainName'],verification_token)
    sleep(600)
    verifyDomain(request_body['domainName'])
    return {"data": query}

def delete_domain(customer_id, domain_name):
    admin_service = build('admin','directory_v1',credentials=auth.authenticate())
    query = admin_service.domains().delete(customer=customer_id,domainName=domain_name).execute()
    return {"data": "deleted"}
