from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class issue_status(str, Enum):
    open="open"
    in_progress="in_progress"
    resolved="resolved"
    
class issue_priority(str, Enum):
    low="low"
    medium="medium"
    high="high"

# Creates a new issue with required fields
class create_issues(BaseModel):
    title: str = Field(min_length=2, max_length=100, example="Issue Title")
    description: Optional[str] = Field(None, max_length=100, example="Issue Description")
    priority: issue_priority = issue_priority.medium

# Want every field to be optional for update, so that user can update any field they want
class update_issues(BaseModel):
    title: Optional[str] = Field(None, min_length=2, max_length=100, example="Issue Title")
    description: Optional[str] = Field(None, max_length=1000, example="Issue Description")
    priority: Optional[issue_priority] = None
    status: Optional[issue_status] = None

class user_response(BaseModel):
    id: str
    title: str
    description: str
    priority: issue_priority
    status: issue_status