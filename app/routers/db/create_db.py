from sqlmodel import SQLModel
from database import engine
import models 
SQLModel.metadata.create_all(engine)

print("Database tables created")
