from fastapi import APIRouter
from typing import List
from models.contract import Contract
from models.optimize_result import OptimizeResult
from utils.scheduling import Scheduling

router = APIRouter()


@router.post("/spaceship/optimize", response_model=OptimizeResult)
async def optimize_contracts(contracts: List[Contract]):
    return Scheduling.contract_scheduling(contracts)
