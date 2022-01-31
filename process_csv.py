import csv
import json

users = []
with open('domains.csv','r') as f:
    csv_reader = csv.reader(f,delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            domain = row[0]
            givenName = row[2]
            familyName = row[3]
            email_accounts = row[4].split(',')
            for account in email_accounts:
                body = {
                    "kind": "admin#directory#user",
                    "primaryEmail": f"{account}@{domain}",
                    "name": {
                        "givenName": givenName,
                        "familyName": familyName
                    },
                    "password": "P@ssW0rd",
                    "changePasswordAtNextLogin": True
                }
                users.append(body)

for user in users:
    print(json.dumps(user))
