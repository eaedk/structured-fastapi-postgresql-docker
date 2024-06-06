from pydantic import BaseModel


# Shared properties for Item
class ItemBase(BaseModel):
    name: str
    description: str


# Properties to receive via API on creation
class ItemCreate(ItemBase):
    pass


# Properties to return via API
class Item(ItemBase):
    id: int

    class ConfigDict:
        orm_mode = True
