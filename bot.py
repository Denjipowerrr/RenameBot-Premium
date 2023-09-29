import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6343012621:AAEwvbrs5QXCYfzl3C4mQcqDwFdAzns9je8")

API_ID = int(os.environ.get("API_ID", "7787348"))

API_HASH = os.environ.get("API_HASH", "82d0ac02a96bfa8469fde897429a4135")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
