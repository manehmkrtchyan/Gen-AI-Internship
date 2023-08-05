import asyncio
import websockets

connected_clients = set()

async def handle_connection(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast_message(websocket, message)
    finally:
        connected_clients.remove(websocket)

async def broadcast_message(sender, message):
    print(f"Received message from {sender.remote_address}: {message}")
    for client in connected_clients:
        if client != sender:
            await client.send(message)

async def server():
    async with websockets.serve(handle_connection, "localhost", 8765):
        await asyncio.Future()

asyncio.run(server())
