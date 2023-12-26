import asyncio
import json
import warnings

import websockets

warnings.filterwarnings("ignore", category=DeprecationWarning)

server_socket = None
my_nickname = None


async def send_to_server(dict_message):
    json_message = json.dumps(dict_message)
    await server_socket.send(json_message)


async def recv_from_server():
    json_message = await server_socket.recv()
    dict_message = json.loads(json_message)
    return dict_message


async def send_login(nickname):
    login_message = {"type": "LOGIN", "nickname": nickname}
    await send_to_server(login_message)


async def send_list_online_users():
    list_online_users_message = {"type": "LIST_ONLINE_USERS"}
    await send_to_server(list_online_users_message)
    online_users = await recv_from_server()
    return online_users


async def send_chat_message(other_nickname, message):
    chat_message = {
        "type": "PRIVATE_MESSAGE",
        "from": my_nickname,
        "to": other_nickname,
        "message": message,
    }
    await send_to_server(chat_message)


async def handle_messages_from_server():
    while True:
        chat_message = await recv_from_server()
        if chat_message["type"] == "PRIVATE_MESSAGE":
            from_nickname = chat_message["from"]
            message = chat_message["message"]
            print(f"!!! Message from {from_nickname}: {message}")


async def main_loop():
    global server_socket
    global my_nickname
    uri = "ws://localhost:4321"
    async with websockets.connect(uri) as websocket:
        server_socket = websocket

        my_nickname = input("What is your nickname: ")
        await send_login(my_nickname)
        online_users = await send_list_online_users()
        print("Online users are: " + str(online_users))

        asyncio.create_task(handle_messages_from_server())

        while True:
            other_nickname = input("Whom do you want to chat? ")
            message = input("What do you want to say? ")
            await send_chat_message(other_nickname, message)


asyncio.get_event_loop().run_until_complete(main_loop())
