from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.routes.schemas import user_response

app = FastAPI(
    title="Issue Tracker API",
    version="1.0.0")

app.include_router(issues_router)