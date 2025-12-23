from fastapi import APIRouter, Depends
from sqlmodel import Session
from data.interactor import get_session
from data.models import Contact



router = APIRouter(prefix="/contacts", tags=["Contacts"])

"""create contact
    gets:
        name,phone number
        generates id
        inserts to the db
        returns new contact ID (queried from DB) 
"""
@router.post("/", response_model=Contact, status_code=201)
def create_contact(
    contact: Contact,
    session: Session = Depends(get_session)
):
    session.add(contact)
    session.commit()
    session.refresh(contact)
    #TODO: check that we get the id and not need to request it 
    return {  
    f"message": "Contact created successfully",  
    "id": {contact.id}  
}


"""
update_contact
returns success boolean
"""


"""
delete_contact
returns success boolean
"""