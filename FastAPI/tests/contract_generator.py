import json
import random

n = 500000
contracts = []

for i in range(1, n+1):
    contract = {
        "name": "Contract" + str(i),
        "start": random.randint(0, 400000),
        "duration": random.randint(1, 500),
        "price": random.randint(1, 10000)
    }
    contracts.append(contract)

print(contracts)
with open('data/payload_500k.json', 'w') as f:
    json.dump(contracts, f, indent=4)
