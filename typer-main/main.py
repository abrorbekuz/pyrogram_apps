from pyrogram import Client, filters
from os import environ
import time, random
from pyrogram.errors import FloodWait

API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
SESSION_NAME = environ["SESSION_NAME"]

app = Client(SESSION_NAME, API_ID, API_HASH)

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def main(_, msg):
	typertext = msg.text.split(".type ", maxsplit=1)[1]
	symbol = "|"

	for i in range(1, len(typertext) + 1):
		try:
			msg.edit(typertext[:i] + symbol)
			time.sleep(random.uniform(0, 0.1))
			
			msg.edit(typertext[:i])
			time.sleep(random.uniform(0, 0.1))

		except FloodWait as b:
			print(b.x)
			time.sleep(b.x)

app.run()
