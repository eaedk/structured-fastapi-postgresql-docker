from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import logging
from app.schemas import items as schemas
from app.crud import items as crud
from app.db.session import get_db
from app.core.logging_config import LOGGING_CONFIG

# Initialize logging
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

router = APIRouter()


# Create a new item
@router.post("/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    logger.info("Creating a new item")
    return crud.create_item(db=db, item=item)


# Read an item by ID
@router.get("/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    logger.info(f"Reading item with ID: {item_id}")
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        logger.warning(f"Item with ID {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# Update an existing item
@router.put("/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    logger.info(f"Updating item with ID: {item_id}")
    db_item = crud.update_item(db=db, item_id=item_id, item=item)
    if db_item is None:
        logger.warning(f"Item with ID {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# Delete an item by ID
@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting item with ID: {item_id}")
    result = crud.delete_item(db=db, item_id=item_id)
    if not result:
        logger.warning(f"Item with ID {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
