from pydantic import BaseModel


class Contract(BaseModel):
    """
    This is the Contract class which inherits from pydantic's BaseModel.
    It describes a contract with a name, start time, duration, and price.

    Attributes:
    name (str): The name of the contract.
    start (int): The start time of the contract represented as an integer.
    duration (int): The duration of the contract in some integer units (for example, days or months).
    price (int): The price or cost associated with the contract.
    """
    name: str  # Contract name
    start: int  # Start time of the contract
    duration: int  # Duration of the contract
    price: int  # Contract price
