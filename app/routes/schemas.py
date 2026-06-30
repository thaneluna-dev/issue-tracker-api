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