from pydantic import BaseModel

class DepressionRequest(BaseModel):
    query: str
    type: str
    top_k: int

class DepressionUpdate(BaseModel):
    query: str
    type: int
    top_k: int