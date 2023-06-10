from pydantic import BaseModel


class Contract(BaseModel):
    name: str
    start: int
    duration: int
    price: int
