from fastapi import APIRouter, Depends, HTTPException, status
from app.routes.schemas import issue_out


router = APIRouter(
    prefix="/api/v1/issues", tags=["issues"],
    responses={404: {"description": "Not found"}})

@router.get("/", response_model=list[issue_out])
def get_issues():
    return []