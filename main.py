import discord
from api import get_fon
from dotenv import load_dotenv
import os
load_dotenv()

words=[]

with open('tefas_kod.csv', 'r') as f:
    for line in f:
        words.append(line.split(","))
    words=words[0]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    msg = message.content

    if msg.startswith('$'):
        kod = msg.split('$')[1]
        if kod in words:
            result = get_fon([kod])
            await message.channel.send(f'```json\n{result}\n```')
        else:
            await message.channel.send('Aradiginiz fon bulunamadi')

client.run(os.getenv('TOKEN'))