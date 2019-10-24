# bot.py
import os
import random

import discord
#from dotenv import load_dotenv



#load_dotenv()
token = 'NjM2ODk4MDQ5ODY3OTA3MDcz.XbGpvw.rxA5qbfmN3whWoFt6pVpAjza9qI'#os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
	rn = random.randint(1,20)
	print(rn)
	if rn<6:
		await message.channel.send('hi')
    

client.run(token)
