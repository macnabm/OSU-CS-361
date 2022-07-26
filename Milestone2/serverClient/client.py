import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = ""
        await websocket.send(name)
        response = await websocket.recv()
        print(response)


if __name__ == "__main__":
    asyncio.run(hello())