import asyncio
import websockets
from socket import gaierror
import ssl

context = ssl._create_unverified_context()
async def hello():
    uri = "wss://nussh.happydoudou.xyz:8000"
    async with websockets.connect(uri,ssl=context) as websocket:
        await websocket.send("AAAA")

asyncio.get_event_loop().run_until_complete(hello())
