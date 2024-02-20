import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("Reply: ")
            await websocket.send(message)

            response = await websocket.recv()
            print(f"Message from server: {response}")

async def main():
    await hello()

if __name__ == "__name__":
    asyncio.run(main())