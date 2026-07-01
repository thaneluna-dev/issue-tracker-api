from fastapi import APIRouter, Depends, HTTPException, status
from app.routes.schemas import create_issues, user_response
from app.routes.storage import get_db
from sqlalchemy.orm import Session
from models.issuesmodel import Issues


router = APIRouter(
    prefix="/api/v1/issues", tags=["issues"],
    responses={404: {"description": "Not found"}})

@router.get("/", response_model=list[user_response])
async def get_issues(db:Session=Depends(get_db)):
    return db.query(Issues).all()

@router.post("/createissues", response_model=user_response, status_code=status.HTTP_201_CREATED)
async def create_issue(issue: create_issues, db:Session=Depends(get_db)):
    new_issue = Issues(**issue.dict())
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return new_issue