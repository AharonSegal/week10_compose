from fastapi import FastAPI
from routers import contacts, utils

app = FastAPI(title="Contacts Manager")

# -------------------- Routers --------------------
app.include_router(utils.router)
app.include_router(contacts.router)

