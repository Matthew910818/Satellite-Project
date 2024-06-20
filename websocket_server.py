# websocket_server.py
import asyncio
import websockets
import json
import random

async def send_data(websocket, path):
    while True:
        data = {
            "temperature": random.uniform(31, 33),
            "humidity": random.uniform(75, 79),
            "pm25": random.uniform(10, 50)
        }
        await websocket.send(json.dumps(data))
        await asyncio.sleep(5)  # 每5秒發送一次數據

start_server = websockets.serve(send_data, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
