import json
import httpx
import asyncio


# Asynchronous function to load JSON file
async def load_json():
    """
    Asynchronous function to load and return the data from a JSON file.

    Returns:
    dict: A dictionary containing the data loaded from the JSON file.
    """
    with open('data/payload_30k.json', 'r') as file:
        return json.load(file)


# Asynchronous function to send POST request
async def send_request(contracts):
    """
    Asynchronous function to send a POST request to a specific endpoint.

    Args:
    contracts (dict): A dictionary containing contracts data to be sent in the POST request.

    Returns:
    None
    """
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8080/spaceship/optimize", json=contracts, timeout=300)

    # Print status code of the response
    print("Response Status Code: ", response.status_code)

    # Print returned data if request was successful, else print the error
    if response.status_code == 200:
        print("Response Data: ", response.json())
        print("Total Selected: ", len(response.json()['contracts']))
    else:
        print("Error Occurred: ", response.text)


# Main asynchronous function
async def main():
    """
    Main asynchronous function to load data from a JSON file and send it in a POST request.

    Returns:
    None
    """
    contracts = await load_json()
    await send_request(contracts)

# Run the main asynchronous function
asyncio.run(main())
