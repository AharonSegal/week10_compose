from fastapi import APIRouter

router = APIRouter(prefix="/utils", tags=["Utils"])

@router.get("/health", status_code=201)
def health():
    return {"status": "ok"}
