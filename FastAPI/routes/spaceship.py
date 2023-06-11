from fastapi import APIRouter
from typing import List
from models.contract import Contract
from models.optimize_result import OptimizeResult
from utils.scheduling import Scheduling

# Create an APIRouter instance
router = APIRouter()


@router.post("/spaceship/optimize", response_model=OptimizeResult)
# This route is a POST endpoint at '/spaceship/optimize'.
# It expects a list of Contract objects as input, and returns an OptimizeResult object.
async def optimize_contracts(contracts: List[Contract]):
    """
    This function optimizes contracts and returns the optimization result.

    Args:
    contracts (List[Contract]): A list of Contract objects to be optimized.

    Returns:
    OptimizeResult: The optimization result containing total price and contract names.
    """
    # Call the contract_scheduling function from the Scheduling utility and return its result
    return Scheduling.contract_scheduling(contracts)
