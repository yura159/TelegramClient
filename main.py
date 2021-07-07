from telethon import TelegramClient, events, sync


def print_all_chats():
    for dialog in client.iter_dialogs():
        dialog
        # print(dialog.name)


def print_users(chat_name):
    print(chat_name)
    print(client.get_participants(chat_name))


api_id = 6711407
api_hash = '66cf1eced9fdaefc6c3ca843bd17a09f'
client = TelegramClient('session_name', api_id, api_hash)


@client.on(events.NewMessage(chats=('@monstr139')))
async def normal_handler(event):
    print(event.message.message)


client.start()
print_all_chats()
client.run_until_disconnected()
