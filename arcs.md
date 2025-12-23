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
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
            (contact.first_name, contact.last_name, contact.phone_number)
        )
        conn.commit()
        contact_id = cursor.lastrowid
        return {**contact.dict(), "id": contact_id}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# ---------------- Update Contact ----------------
@router.put("/{contact_id}", response_model=dict)
def update_contact(contact_id: int, contact: ContactSchema):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE contacts SET first_name=%s, last_name=%s, phone_number=%s WHERE id=%s",
            (contact.first_name, contact.last_name, contact.phone_number, contact_id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Contact not found")
        return {"success": True}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# ---------------- Delete Contact ----------------
@router.delete("/{contact_id}", response_model=dict)
def delete_contact(contact_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Contact not found")
        return {"success": True}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# ---------------- View List Contacts ----------------
@router.get("/", response_model=list[ContactResponse], status_code=201)
def get_all_contacts():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # return rows as dict
    try:
        cursor.execute("SELECT id, first_name, last_name, phone_number FROM contacts")
        rows = cursor.fetchall()
        return rows  # each row is already a dict matching ContactResponse
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
