from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from db.database import get_session
from db.models import Contact

router = APIRouter(prefix="/contacts", tags=["Contacts"], status_code=201)

"""
returns list of Contact objects 
"""
@router.get("/", response_model=list[Contact])
def get_contacts(
    session: Session = Depends(get_session)
):
    #TODO: MAKE TO LIST
    return session.exec(select(Contact)).all()
