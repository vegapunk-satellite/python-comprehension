import asyncio
import websockets


async def message():
    async with websockets.connect("ws://localhost:5555") as socket:
        communication = input("Player chat box: ")
        await socket.send(communication)
        print(await socket.recv())


asyncio.get_event_loop().run_until_complete()
