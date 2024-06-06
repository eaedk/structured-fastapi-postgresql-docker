from fastapi import FastAPI
from app.api import items
from app.db.session import engine
from app.db import models

# Initialize FastAPI app
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Include items router
app.include_router(items.router, prefix="/items", tags=["items"])
