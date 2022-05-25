import discord
from user import test, User
from modal import VerificationModal
import os
from dotenv import load_dotenv
load_dotenv()

bot = discord.Bot(debug_guilds=[978391125431812116])

@bot.event
async def on_ready():
    print(f'{bot.user} has logged on.')
    
@bot.slash_command(name='help', description='Get instructions on how to verify and what to do next!')
async def help(ctx):
    await ctx.respond('Get your unique verification code from any **Games But Blue** Experience in the Settings menu under "Social Link"! Then use the `/verify` command to enter your code and link your accounts!')
    
@bot.slash_command(name='verify', description='Link your Roblox and Discord accounts for access to the server!')
async def testing(ctx):
    
    modal = VerificationModal(title='Test')
    
    usertest = User(roblox_id=1, discord_id=0)
    test2 = test()
    print(test2)
    print(usertest)
    await ctx.send_modal(modal)

bot.run(os.getenv('BOT_TOKEN'))