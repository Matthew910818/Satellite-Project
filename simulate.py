# simulate.py
import asyncio
import websockets
import json
import random

async def send_data():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            data = {
                "temperature": round(random.uniform(31, 33), 1),
                "humidity": round(random.uniform(75, 79), 1),
                "pm25": round(random.uniform(10, 50), 1)
            }
            await websocket.send(json.dumps(data))
            await asyncio.sleep(5)  # 每5秒發送一次數據

if __name__ == "__main__":
    asyncio.run(send_data())
