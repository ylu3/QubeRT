from models.contract import Contract
import json
import httpx
import asyncio

contracts = []

with open('lc.txt', 'r') as file:
    start_time = json.loads(file.readline())
    end_time = json.loads(file.readline())
    price = json.loads(file.readline())

for i in range(len(start_time)):
    duration = end_time[i] - start_time[i]
    name = f"Contract{i + 1}"
    contract = Contract(name=name, start=start_time[i], duration=duration, price=price[i])
    contracts.append(contract.dict())

# 打印结果
for contract in contracts:
    print(contract)

with open('lc.json', 'w') as json_file:
    json_file.write('[\n')
    for i in range(len(contracts)):
        if i != len(contracts) - 1:  # 如果不是最后一个，添加逗号
            json_file.write('    ' + json.dumps(contracts[i]) + ',\n')
        else:  # 最后一个Contract后面不添加逗号
            json_file.write('    ' + json.dumps(contracts[i]) + '\n')
    json_file.write(']\n')


async def send_request():
    async with httpx.AsyncClient() as client:
        response = await client.post('http://localhost:8080/spaceship/optimize', json=contracts)
        print(response.json())  # 打印响应

# 运行异步函数
asyncio.run(send_request())
