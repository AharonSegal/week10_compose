from sqlmodel import SQLModel
from app.routers.data.interactor import engine
import data.models


SQLModel.metadata.create_all(engine)

print("Database tables created")
