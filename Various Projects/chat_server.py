import asyncio
import json
import warnings

import websockets

warnings.filterwarnings("ignore", category=DeprecationWarning)

# A dictionary from nickname to websocket
users = {}


async def send_to_client(dict_message, user_socket):
    json_message = json.dumps(dict_message)
    await user_socket.send(json_message)


async def handle_messages_from_user(user_socket):
    while True:
        chat_message_raw = await user_socket.recv()
        print("Received message (raw): " + chat_message_raw)
        chat_message = json.loads(chat_message_raw)
        print("Received message (dict): " + str(chat_message))
        match chat_message["type"]:
            case "LOGIN":
                nickname = chat_message["nickname"]
                print("Hey welcome " + nickname)
                users[nickname] = user_socket
            case "LIST_ONLINE_USERS":
                online_users_message = {
                    "online_users": [nickname for nickname in users.keys()]
                }
                asyncio.create_task(send_to_client(online_users_message, user_socket))
            case "CREATE_ROOM":
                from_nickname = chat_message["from"]
                to_nickname = chat_message["to"]
                # TODO
            case "PRIVATE_MESSAGE":
                from_nickname = chat_message["from"]
                to_nickname = chat_message["to"]
                message = chat_message["message"]
                if not (to_nickname in users):
                    print("Error: Cannot find user " + to_nickname)
                    # TODO: Send error message back to the sender
                    continue
                to_user_socket = users[to_nickname]
                print(
                    f"Sending message ({message}) from {from_nickname} to {to_nickname}"
                )
                asyncio.create_task(send_to_client(chat_message, to_user_socket))


async def handle_message(user_socket, path):
    await asyncio.create_task(handle_messages_from_user(user_socket))


start_server = websockets.serve(handle_message, "localhost", 4321)
print("Started server...")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


import tkinter as tk
from tkinter import Text, filedialog

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

login = tk.Button(
    root,
    text="Login",
    padx=10,
    pady=5,
    fg="white",
    bg="263D42",
    command=handle_messages_from_user(),
)
login.pack()

root.mainloop()
