from typing import Optional
import uuid
from pydantic import BaseModel, Field


class TaskModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name : str = Field(...)
    completed: bool = False

    class Config:
        allow_population_by_field_name = True

    
class UpdateTaskModel(BaseModel):
    name: Optional[str]
    completed: Optional[bool]