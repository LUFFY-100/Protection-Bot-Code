import discord
from discord.ext import commands 
import json
######################
prefix = '!'
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=prefix,intents=intents)
token = 'Your Bot Token'
############################
@client.event
async def on_ready():
    print("Bot Ready")
###########################
@client.command()
async def antibots_on(ctx):
    with open('antibots.json','r',encoding='utf-8') as f:
        key = json.load(f)
    key[str(ctx.guild.id)]=str("on")
    with open('antibots.json','w',encoding='utf-8') as f:
        json.dump(key,f,indent=4,ensure_ascii=False)
    await ctx.reply("Antibots is On")
@client.command() 
async def antibots_off(ctx):
    with open('antibots.json','r') as f:
        key = json.load(f)
    if f'{ctx.guild.id}' not in key:
        pass
    else:
        del key[f'{ctx.guild.id}']
        key['off']='off'
    with open('antibots.json','w') as f:
        json.dump(key,f,indent=2)
    await ctx.reply("Antibots Are Off")
@client.event
async def on_member_join(member):
    if (member.bot):
        with open('antibots.json', 'r') as f:
            key = json.load(f)
        if f'{member.guild.id}' not in key:
            pass
        else:
            print(f"{member.name} Has Been Kicked")
            await member.kick()                                       
        



















client.run(token)
