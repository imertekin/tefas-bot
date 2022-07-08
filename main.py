from discord.ext import commands
from api import get_fon
from dotenv import load_dotenv
import os
load_dotenv()

words=[]

with open('tefas_kod.csv', 'r') as f:
    for line in f:
        words.append(line.split(","))
    words=words[0]


bot = commands.Bot(command_prefix='$')


@bot.command()
async def fon(ctx, *args):
    for i in args:
        i = i.upper()
        if i in words:
            result = get_fon([i])
        await ctx.send(f'```json\n{result}\n```')

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
            await message.channel.send(f'```json\n{result}\n```')
        else:
            await message.channel.send('Aradiginiz fon bulunamadi')
    await bot.process_commands(message)

bot.run(os.getenv('TOKEN'))