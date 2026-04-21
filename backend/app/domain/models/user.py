from typing import Optional 
from pydantic import BaseModel, Field


class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    first_name: str
    last_name: str
    email: str
    password_hash: str

    model_config = {"populate_by_name": True}
