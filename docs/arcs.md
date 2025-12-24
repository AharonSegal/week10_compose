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

{
  "first_name": "aharon",
  "last_name": "segal",
  "phone_number": "052-719-3536"
}

[
  {"first_name": "Alice", "last_name": "Johnson", "phone_number": "123-456-7890"},
  {"first_name": "Bob", "last_name": "Smith", "phone_number": "234-567-8901"},
  {"first_name": "Charlie", "last_name": "Brown", "phone_number": "345-678-9012"},
  {"first_name": "Diana", "last_name": "Miller", "phone_number": "456-789-0123"},
  {"first_name": "Ethan", "last_name": "Davis", "phone_number": "567-890-1234"},
  {"first_name": "Fiona", "last_name": "Garcia", "phone_number": "678-901-2345"},
  {"first_name": "George", "last_name": "Martinez", "phone_number": "789-012-3456"},
  {"first_name": "Hannah", "last_name": "Lopez", "phone_number": "890-123-4567"},
  {"first_name": "Ian", "last_name": "Wilson", "phone_number": "901-234-5678"},
  {"first_name": "Julia", "last_name": "Anderson", "phone_number": "012-345-6789"},
  {"first_name": "Kevin", "last_name": "Thomas", "phone_number": "123-098-4567"},
  {"first_name": "Laura", "last_name": "Taylor", "phone_number": "234-109-5678"},
  {"first_name": "Michael", "last_name": "Moore", "phone_number": "345-210-6789"},
  {"first_name": "Nina", "last_name": "Jackson", "phone_number": "456-321-7890"},
  {"first_name": "Oscar", "last_name": "White", "phone_number": "567-432-8901"},
  {"first_name": "Paula", "last_name": "Harris", "phone_number": "678-543-9012"},
  {"first_name": "Quentin", "last_name": "Martin", "phone_number": "789-654-0123"},
  {"first_name": "Rachel", "last_name": "Thompson", "phone_number": "890-765-1234"},
  {"first_name": "Steven", "last_name": "Garcia", "phone_number": "901-876-2345"},
  {"first_name": "Tina", "last_name": "Martinez", "phone_number": "012-987-3456"}
]
