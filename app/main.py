from fastapi import FastAPI
import logging
from app.api import items
from app.db.session import engine
from app.db import models
from app.core.logging_config import LOGGING_CONFIG

# Initialize logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Include items router
app.include_router(items.router, prefix="/items", tags=["items"])

# Log application start
logger.info("Application startup complete")
