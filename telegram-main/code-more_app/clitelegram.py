#boshaldik +)
from pyrogram import Client, compose
from config import *


app = [
Client(
    name = "user",
    api_id = api_id,
    api_hash = api_hash,
    session_string = session_string
),
Client(
    name = "user",
    api_id = api_id,
    api_hash = api_hash,
    session_string = session_string
)]

app[0].start()
app[1].start()
app = app[0]
# app.start()

users, bots, groups, channels = [], [], [], []
for dialog in app.get_dialogs():
    try:
        match dialog.chat.type.name:

            case "PRIVATE":
                users.append([dialog.chat.id,
                              dialog.chat.first_name or \
                                dialog.chat.title])
            case "BOT":
                bots.append([dialog.chat.id,
                             dialog.chat.first_name or \
                                dialog.chat.title])
            case "GROUP":
                groups.append([dialog.chat.id,
                               dialog.chat.first_name or \
                                dialog.chat.title])
            case "SUPERGROUP":
                groups.append([dialog.chat.id,
                               dialog.chat.first_name or \
                                dialog.chat.title])
            case "CHANNEL":
                channels.append([dialog.chat.id, 
                                 dialog.chat.first_name or \
                                    dialog.chat.title])
    except: print(dialog.chat.id)

# for i in [users, bots, groups]:
#     print(i, "\n")
    
choice = input("1-user, 2-bot, 3-group\n>")
match int(choice):
    case 1:
        for index, user in enumerate(users):
            print(index, user[1])
        who = users[int(input())][0]
    case 2:
        for index, user in enumerate(bots):
            print(index, user[1])
        who = bots[int(input())][0]
    case 3:
        for index, user in enumerate(groups):
            print(index, user[1])
        who = groups[int(input())][0]

app.send_message(who, "salom")

app.stop()