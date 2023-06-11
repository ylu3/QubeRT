from pydantic import BaseModel
from typing import List


class OptimizeResult(BaseModel):
    """
    This is the OptimizeResult class which inherits from pydantic's BaseModel.
    It describes the optimization result including total price and a list of contract names.

    Attributes:
    total_price (int): The total price or cost associated with the optimized result.
    contracts (List[str]): A list of contract names included in the optimized result.
    """
    total_price: int  # Total price of the optimized result
    contracts: List[str]  # List of contract names
