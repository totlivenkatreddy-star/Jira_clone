from fastapi import APIRouter

router= APIRouter()

@router.get("/")
def land_page():
    return {"message":"this is a landing page"}