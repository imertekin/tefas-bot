import discord
from discord.ext import commands
from api import get_fon
from dotenv import load_dotenv
import os
import json
load_dotenv()

words=[]

with open('tefas_kod.csv', 'r') as f:
    for line in f:
        words.append(line.split(","))
    words=words[0]

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='$', intents=intents)

class KAP(discord.ui.View):
    def __init__(self, url: str):
        super().__init__()
        self.add_item(discord.ui.Button(label="KAP",style=discord.ButtonStyle.green, url=url))


@bot.command()
async def fon(ctx,*args):
    flag = args[0]
    for i in args:
        i = i.upper()
        if i in words:
            result = get_fon([i])
            kap = result['KAP']
            result.pop('KAP',None)
            if flag == '-d':
                result = json.dumps(result, ensure_ascii=False,indent = 4)
                await ctx.send(f'```json\n{result}\n```',view = KAP(kap))
            else:
                result = {i:{
                    'Son Fiyat (TL)':result[i]['Son Fiyat (TL)'],
                    'Günlük Getiri (%)':result[i]['Günlük Getiri (%)'],
                    'Son 1 Ay Getirisi':result[i]['Son 1 Ay Getirisi'],
                    'Son 3 Ay Getirisi':result[i]['Son 3 Ay Getirisi'],
                    'Son 6 Ay Getirisi':result[i]['Son 6 Ay Getirisi'],
                    'Son 1 Yıl Getirisi':result[i]['Son 1 Yıl Getirisi']
                }}
                result = json.dumps(result, ensure_ascii=False,indent = 4)
                await ctx.send(f'```json\n{result}\n```',view = KAP(kap))
        

@bot.command()
async def helper(ctx):

        await ctx.send(' Tefas-Bot tefas.gov.tr de ki fon bilgilerini json formatinda tekli ve toplu olarak cekip donen bir bottur.')

@bot.command()
async def cmds(ctx):

        await ctx.send(f'cmds komutu bot un mevcut komutlarini gosterir.\n```\n- $help\n- $cmds\n- $fon\n- ~fonName```')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    msg = message.content.upper()

    if msg.startswith('~'):
        code = msg.split('~')[1]
        code = code.upper()
        if code in words:
            result = get_fon([code])
            result = json.dumps(result, ensure_ascii=False,indent = 4)
            await message.channel.send(f'```json\n{result}\n```')
        else:
            await message.channel.send('Aradiginiz fon bulunamadi')
    await bot.process_commands(message)

bot.run(os.getenv('TOKEN'))