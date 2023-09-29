import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6343012621:AAEwvbrs5QXCYfzl3C4mQcqDwFdAzns9je8")

API_ID = int(os.environ.get("API_ID", "7787348"))

API_HASH = os.environ.get("API_HASH", "82d0ac02a96bfa8469fde897429a4135")

STRING = os.environ.get("STRING", "BQA4i8K_sf4TI5U_Vx03qloMXETCn6jgdORU6eI0kt_nlb5ImD-g3FWqTNObWIVhOgp7ibC27rFZRA3vLNHxukm57m5uoa2GBLCF95ro5HliEaD7-Jn1Z8LOc4F9I0Td98pxN9MFNA9U8bMxYjZsaJD-Nbe0k_l7uo1Ix3qTEFRVRUsZ2yk1WG7elvxYxufEjtyFaJ3J4hQpFYYhs04Lxuw5wvZYyJ_dnnRjiEejWx-9DO6D2s9e-vVP2BLUbgLettdByRVXraNA1PqcPFQX8i4aAeu2gUmWzc6UimQgolYjABXh0vSZXq5fbHy8wPlHab_L89YxKCjrmsMY-CqA1DXwAAAAAXv2bOwA")


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
