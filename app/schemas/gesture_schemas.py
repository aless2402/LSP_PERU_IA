from pydantic import BaseModel
from typing import Optional

class GestureSchema(BaseModel):
    name: str
    meaning: str
    confidence: Optional[float] = None

class GestureCreate(GestureSchema):
    video_path: str

class GestureOut(GestureSchema):
    id: int
