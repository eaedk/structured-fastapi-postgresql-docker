import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# Get database URLs from environment variables
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
SQLALCHEMY_DATABASE_URL_TEST = os.getenv("SQLALCHEMY_DATABASE_URL_TEST")

# Determine the appropriate database URL based on the environment
if os.getenv("TESTING"):
    engine = create_engine(SQLALCHEMY_DATABASE_URL_TEST)
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
