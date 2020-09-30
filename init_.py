from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import workflow_image_utils
from random import choice
from asyncio import sleep

import json


# Remember to use your own values from my.telegram.org!
api_id = int(input("Enter app id : "))
api_hash = input("Enter api hash id : ")
string = input("Enter string session id : ")


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
	    await sleep(20)

with client:
	client.loop.run_until_complete(main())
