import os, telethon, telethon.utils, asyncio, traceback ; from pikabot import * ; from sys import * ; from var import * ; client = bot ; ItzSjDude = client ; from telethon.errors.rpcerrorlist import * ; from var import Client as clIent ; from pathlib import Path ; from telethon import * ; from telethon.tl.types import * 
async def add_bot(bot_token):
    await bot.start(bot_token)
    await botx.start(bot_token)
    botx.me = await botx.get_me() 
    bot.me = await bot.get_me() 
    botx.uid = telethon.utils.get_peer_id(botx.me)
    bot.uid = telethon.utils.get_peer_id(bot.me)
if len(argv) not in (1, 3, 4):
    bot.disconnect()
    botx.disconnect
else:
    botx.tgbot = None
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
    elif Var.TG_BOT_USER_NAME_BF_HER2 is not known 
        botx.tgbot = TelegramClient("TG_BOT_TOKEN1", app_id=Var.APP_ID, api_hash=Var.API_HASH).start(bot_token=Var.TG_BOT_TOKEN_BF_HERE2)
        bot.tgbot = TelegramClient("TG_BOT_TOKEN",api_id=Var.APP_ID,api_hash=Var.API_HASH).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Pikabot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        botx.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER2))
        print("Startup Completed")
    else:
        bot.start()
        botx.start()

print("Loading Main Plugs..")
async def stop():
    cli1 = await client.get_messages(clIent, None , filter=InputMessagesFilterDocument) ; total = int(cli1.total) ; total_doxx = range(0, total)
    for ixo in total_doxx:
        mxo =cli1[ixo].id ; await client.download_media(await bot.get_messages(clIent, ids=mxo), "pikabot/main_plugs")
ItzSjDude.loop.run_until_complete(stop()) 
print("Loaded Sucessfully") 


print("Initialising Core")

import pikabot._core

print("setting up carbon") 

import pikabot.carbonX   

print("Chal Gya hu bsdk Ab jaa k saved msgs me .help ya .alive type krke confirm kr le")
if len(argv) not in (1, 3, 4):
    bot.disconnect()
    botx.disconnecf()
else:
    bot.run_until_disconnected()
    botx.run_untill_disconnected ()


