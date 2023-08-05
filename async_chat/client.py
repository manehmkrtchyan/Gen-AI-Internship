import asyncio
import websockets

async def handle_messages(websocket):
    # try:
        async for message in websocket:
            print("Received:", message)
    # except websockets.ConnectionClosed:
        # print("Connection closed.")

async def client():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await asyncio.gather(
            handle_messages(websocket),
            send_messages(websocket)
        )

async def send_messages(websocket):
    username = input('Enter username: ')
    await websocket.send(f'{username} joined the chat!')
    while True:
        message = input("Enter message: ")
        await websocket.send(message)
        

asyncio.run(client())


# import asyncio
# import websockets

# async def handle_messages(websocket):
#     try:
#         async for message in websocket:
#             print("Received:", message)
#     except websockets.ConnectionClosed:
#         print("Connection closed.")

# async def client():
#     async with websockets.connect("ws://localhost:8765") as websocket:
#         await asyncio.gather(
#             handle_messages(websocket),
#             send_messages(websocket)
#         )

# async def send_messages(websocket):
#     username = input('Enter username: ')
#     await websocket.send(f'{username} joined the chat!')
#     while True:
#         message = input("Enter message: ")
#         await websocket.send(message)

# asyncio.run(client())
