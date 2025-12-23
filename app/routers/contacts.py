from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from data.interactor import get_connection

router = APIRouter(prefix="/contacts", tags=["Contacts"])

class ContactSchema(BaseModel):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    phone_number: str = Field(min_length=1, max_length=20)

class ContactResponse(ContactSchema):
    id: int

# ---------------- Create Contact ----------------
@router.post("/", response_model=ContactResponse, status_code=201)
def create_contact(contact: ContactSchema):
    ...
# ---------------- Update Contact ----------------
@router.put("/{contact_id}", response_model=dict)
def update_contact(contact_id: int, contact: ContactSchema):
    ...
# ---------------- Delete Contact ----------------
@router.delete("/{contact_id}", response_model=dict)
def delete_contact(contact_id: int):
    ...

# ---------------- View List Contacts ----------------
@router.get("/", response_model=list[ContactResponse], status_code=201)
def get_all_contacts():
    ...