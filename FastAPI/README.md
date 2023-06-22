# Project Name

This project is a web application that optimizes contract scheduling for a spaceship. It provides an API endpoint `/spaceship/optimize` that accepts a JSON payload containing a list of contracts. The server calculates the optimal scheduling solution using the `Scheduling.contract_scheduling` method and returns the total revenue and a list of selected contract names in the response.

## Installation

1. Clone the repository:

```
git clone https://github.com/ylu3/QubeRT.git
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Start the server:

```
uvicorn main:app --port 8080
```

2. Make a POST request to `http://localhost:8080/spaceship/optimize` with the following JSON payload:

```json
[
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
    {"name": "Contract4", "start": 5, "duration": 9, "price": 7}
]
```

3. The server will respond with a JSON object containing the total revenue and the path:

```json
{
    "income": 18,
    "path": ["Contract1", "Contract3"]
}
```

## API Endpoint

### `/spaceship/optimize`

- Method: POST
- Request Body: JSON payload containing a list of contracts
- Response: JSON object with the total revenue and selected contract names

## Testing

1. Run the tests:

```
python -m pytest
```

The tests are located in the `tests/` directory and cover various scenarios to ensure the correctness of the contract scheduling algorithm.

## Project Structure

```
project/
├── main.py
├── models/
│   ├── contract.py
│   └── optimize_result.py
├── routes/
│   └── spaceship.py
├── tests/
│   ├── test_spaceship.py
│   └── contract_data.json
└── utils/
    └── scheduling.py
```

The project structure follows the MVC (Model-View-Controller) pattern:

- `main.py` is the entry point of the application.
- `models/` directory contains the Pydantic models used for request and response validation.
- `routes/` directory contains the route handlers for the API endpoints.
- `tests/` directory contains the test cases.
- `utils/` directory contains the `Scheduling` class with the scheduling algorithm implementation.

## Credits

This project was created by Yan LU.