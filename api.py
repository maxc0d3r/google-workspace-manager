from fastapi import Request, FastAPI

import gwm.directory.domains
import gwm.directory.users
import gwm.directory.groups
from gwm.directory.domains import list_domains, add_domain, delete_domain

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Google Workspace Manager v0.0.1"}

@app.get("/v1/domains/{customer_id}")
async def listDomains(customer_id):
    return await list_domains(customer_id)

@app.get("/v1/domains/{customer_id}/{domain_name}")
async def get_domain(customer_id,domain_name):
    pass

@app.post("/v1/domains/{customer_id}")
async def addDomain(request: Request, customer_id):
    body = await request.json()
    return await add_domain(customer_id, body)

@app.delete("/v1/domains/{customer_id}/{domain_name}")
async def delete_domain(customer_id,domain_name):
    return await delete_domain(customer_id, domain_name)

@app.put("/v1/domains/{customer_id}/{domain_name}")
async def update_domain(customer_id,domain_name):
    pass

@app.get("/v1/users/{customer_id}")
async def list_users(customer_id):
    pass

@app.get("/v1/users/{customer_id}/{email}")
async def get_user(customer_id,email):
    pass

@app.post("/v1/users/{customer_id}")
async def add_user(customer_id):
    pass

@app.delete("/v1/users/{customer_id}/{email}")
async def delete_user(customer_id,email):
    pass

@app.put("/v1/users/{customer_id}/{email}")
async def update_user(customer_id,email):
    pass
