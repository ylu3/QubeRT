import pytest
import json
import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
test_data = os.path.join(os.path.dirname(__file__), "data/payloads.json")


# Function to read test contract data from a JSON file
def read_contract_data(file_path):
    """Reads a JSON file and returns its contents as a Python data structure.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        A Python data structure (list, dict, etc.) representing the content of the JSON file.
    """
    with open(file_path) as file:
        contract_data = json.load(file)
    return contract_data


# Pytest decorator to enable parametrized tests
@pytest.mark.parametrize(
    "test_case",  # Argument name for the test function
    read_contract_data(test_data)  # List of argument values
)
# Test function to test the "/spaceship/optimize" endpoint of the FastAPI application
def test_optimize_contracts(test_case):
    """Tests the '/spaceship/optimize' endpoint of the FastAPI application.

    This function makes a POST request to the '/spaceship/optimize' endpoint,
    using the 'contracts' field of the test case as the request body.
    Then, it checks the response status code and the contents of the response body.

    Args:
        test_case (dict): A dictionary representing a test case.
        It should contain the following keys: 'contracts', 'expected_income', 'expected_path'.
    """
    # Send POST request
    response = client.post("/spaceship/optimize", json=test_case["contracts"])
    # Parse response body as JSON
    data = response.json()

    # Check response status code
    assert response.status_code == 200
    # Check 'income' field in the response
    assert data["income"] == test_case["expected_income"]
    # Check 'contracts' field in the response (order doesn't matter)
    assert sorted(data["path"]) == sorted(test_case["expected_path"])
