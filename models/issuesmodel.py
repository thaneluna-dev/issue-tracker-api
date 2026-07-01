from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from app.routes.storage import engine as storage_engine

Base = declarative_base()

class Issues(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=True)
    priority = Column(Enum("low", "medium", "high", name="priority_enum"), nullable=False)
    status = Column(Enum("open", "in_progress", "closed", name="status_enum"), nullable=False)
    
Base.metadata.create_all(bind=storage_engine)