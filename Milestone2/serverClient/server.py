import asyncio
import websockets

async def schoolResponse(websocket):
    name = await websocket.recv()
    print("Server Ran")
    greeting = "Message from CS361"
    await websocket.send(greeting)

async def main():
    async with websockets.serve(schoolResponse, "localhost", 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())