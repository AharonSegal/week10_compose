from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from data.data_interactor import (
    create_contact as db_create_contact,
    get_all_contacts as db_get_all_contacts,
    update_contact as db_update_contact,
    delete_contact as db_delete_contact,
    Contact as ContactModel,
)

router = APIRouter(prefix="/contacts", tags=["Contacts"])


class ContactSchema(BaseModel):
    first_name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=50)
    phone_number: str = Field(min_length=1, max_length=20)


class ContactResponse(ContactSchema):
    id: int


@router.post("/", status_code=201)
def create_contact(contact: ContactSchema):
    try:
        new_id = db_create_contact(
            contact.first_name,
            contact.last_name,
            contact.phone_number,
        )
        return {"message": "Contact created successfully", "id": new_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=list[ContactResponse])
def list_contacts():
    try:
        contacts = db_get_all_contacts()
        return [c.to_dict() for c in contacts]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{contact_id}")
def update_contact(contact_id: int, contact: ContactSchema):
    try:
        ok = db_update_contact(
            contact_id,
            contact.first_name,
            contact.last_name,
            contact.phone_number,
        )
        if not ok:
            raise HTTPException(status_code=404, detail="Contact not found")
        return {"message": "Contact updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{contact_id}")
def delete_contact(contact_id: int):
    try:
        ok = db_delete_contact(contact_id)
        if not ok:
            raise HTTPException(status_code=404, detail="Contact not found")
        return {"message": "Contact deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))