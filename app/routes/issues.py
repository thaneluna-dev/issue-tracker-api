from fastapi import APIRouter, Depends, HTTPException, status
from app.routes.schemas import user_response


router = APIRouter(
    prefix="/api/v1/issues", tags=["issues"],
    responses={404: {"description": "Not found"}})

@router.get("/", response_model=list[user_response])
async def get_issues():
    return []