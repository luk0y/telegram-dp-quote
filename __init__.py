from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import workflow_image_utils
from random import choice
from asyncio import sleep
import os

import json


# Remember to use your own values from my.telegram.org!
api_id, api_hash, string = int(os.environ.get("APP_ID", 6)), os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e"),os.environ.get("STRING_SESSION", None)


with open("quotes/csvjson.json","r") as f:


	data = [i for i in json.load(f) if len(i['QUOTE']) <= 250]


client = TelegramClient(StringSession(string), api_id, api_hash)

async def main():

    while True:

	    workflow_image_utils.quoteGen(choice(data))


	    # Getting information about yourself
	    
	    
	    await client(UploadProfilePhotoRequest(
	    await client.upload_file('sample-imagetext.png')
	))
	    await sleep(3600)

with client:
	client.loop.run_until_complete(main())
