from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from data.interactor import get_session
from data.models import Contact

router = APIRouter(prefix="/contacts", tags=["Contacts"], status_code=201)

"""
returns list of Contact objects 
"""
@router.get("/", response_model=list[Contact], status_code=201)
def get_contacts(session: Session = Depends(get_session)):
    #TODO: MAKE TO LIST
    return session.exec(select(Contact)).all()
