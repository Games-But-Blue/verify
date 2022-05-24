import discord
import os
from dotenv import load_dotenv
load_dotenv()

bot = discord.Bot(debug_guilds=[978391125431812116])

@bot.event
async def on_ready():
    print(f'{bot.user} has logged on.')
    
@bot.slash_command(name='helloworld', description='Hello world function')
async def testing(ctx):
    await ctx.respond('Hello World')
   
bot.run(os.getenv('BOT_TOKEN'))