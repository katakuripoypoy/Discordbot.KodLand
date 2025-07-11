import discord 
from discord.ext import commands
from python.challange import tas_kagit_makas
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="The_Fraud/", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    #if message.content.startswith('The_Fraud/merhaba'):
        #await message.channel.send("Selam")
    #elif message.content.startswith('$bye'):
        #await message.channel.send("\U0001f642")
    #elif message.content.startswith("$The_Fraud/challage"):
        #await message.channel.send(tas_kagit_makas())
    #elif message.content.startswith("$The_Fraud/ReNewable_Energy"):
        #await message.channel.send("Interesting... renewable energy is essential!")
    #else:
        #await message.channel.send(message.content)

    await bot.process_commands(message)

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")
@bot.command()
async def Renewable_Energy(ctx):
    await ctx.send("Interesting... 'renewable energy' a new found way to produce electrical power which is essential to make the devices that works with it. Right now humans do not understand the value of this there for it cannot have the upgrade... Very Very Interesting topic")


bot.run("YOUR OWN TOKEN")