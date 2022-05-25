import discord
import os
from dotenv import load_dotenv
load_dotenv()

bot = discord.Bot(debug_guilds=[967051592329232494])

@bot.event
async def on_ready():
    print(f'{bot.user} has logged on.')
    
@bot.slash_command(name='helloworld', description='Hello world function')
async def testing(ctx):
    await ctx.respond('Hello World')
   
bot.run(os.getenv('BOT_TOKEN'))