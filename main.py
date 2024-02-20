import asyncio
import websockets

async def hello(websocket):
    async for message in websocket:
        print(f"Message from client: {message}")
        response = input("Reply: ")
        await websocket.send(response)

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future() #Runs Forever

if __name__ == "__main__":
    asyncio.run(main())