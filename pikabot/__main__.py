import os, telethon, telethon.utils, asyncio, traceback ; from pikabot import * ; from sys import * ; from var import * ; client = bot ; ItzSjDude = client ; from telethon.errors.rpcerrorlist import * ; from var import Client as clIent ; from pathlib import Path ; from telethon import * ; from telethon.tl.types import * 
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)
async def alt():
    LOGS.info("Connecting to telegram servers...")
    if client2:
        try:
            await client2.start()
            LOGS.info("String 2 Connected")
        except:
            LOGS.info("String Session 2 expired. Please create new one")
            quit(1)
bot.loop.run_until_complete(alt())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        bot.tgbot = TelegramClient("TG_BOT_TOKEN",api_id=Var.APP_ID,api_hash=Var.API_HASH).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Pikabot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

async def start():
  cli1 = await client.get_messages(clIent, None , filter=InputMessagesFilterDocument) ; total = int(cli1.total) ; total_doxx = range(0, total)
  for ixo in total_doxx:
       mxo =cli1[ixo].id ; await client.download_media(await bot.get_messages(clIent, ids=mxo), "pikabot/main_plugs")
       print("Loaded Sucessfully") 
ItzSjDude.loop.run_until_complete(start())

print("Initialising Core")

import pikabot._core

print("setting up carbon") 

import pikabot.carbonX   

print("Chal Gya hu bsdk Ab jaa k saved msgs me .help ya .alive type krke confirm kr le")
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()

