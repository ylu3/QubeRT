from pydantic import BaseModel
from typing import List


class OptimizeResult(BaseModel):
    total_price: int
    contracts: List[str]
