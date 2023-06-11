import json
import httpx
import asyncio


# 读取JSON文件的异步函数
async def load_json():
    with open('payload_50k.json', 'r') as file:
        return json.load(file)


# 发送POST请求的异步函数
async def send_request(contracts):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8080/spaceship/optimize", json=contracts, timeout=100)

    # 如果请求成功，返回结果应该是200，您可以打印出来看看
    print("Response Status Code: ", response.status_code)

    # 打印返回的数据
    if response.status_code == 200:
        print("Response Data: ", response.json())
    else:
        print("Error Occurred: ", response.text)


# 主异步函数
async def main():
    contracts = await load_json()
    await send_request(contracts)

# 运行主异步函数
asyncio.run(main())
