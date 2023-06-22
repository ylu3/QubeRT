from pydantic import BaseModel
from typing import List


class OptimizeResult(BaseModel):
    """
    This is the OptimizeResult class which inherits from pydantic's BaseModel.
    It describes the optimization result including total income and a list of contract names.

    Attributes:
    income (int): The total income or cost associated with the optimized result.
    path (List[str]): A list of contract names included in the optimized result.
    """
    income: int  # total income of the optimized result
    path: List[str]  # List of contract names
