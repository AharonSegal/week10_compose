from fastapi import FastAPI
from app.routers.db_test import router as db_test_router

app = FastAPI(title="Contacts Manager")

# register routers
app.include_router(db_test_router)

