from typing import Optional
from pydantic import BaseModel

class Fridge(BaseModel):
    id: Optional[int]
    timestamp: str
    chillerStatus: int
    temperature: float
    humidity: float
    power: float