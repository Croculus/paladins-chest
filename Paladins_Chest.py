import datetime, discord, os, asyncio
from discord.ext import commands

token ='MTA0NjQ2NjIyMDE5NjY0MjkzNw.GQwPs6.sh6Dn5frRAfH0GWt4Iyaup9mwsYScKS3VAtdiY'
hours = [datetime.time(i) for i in range(0, 23)]


intents = discord.Intents().all()
client = commands.Bot(command_prefix='/', intents=intents) 

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

async def load_ext():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')


async def main():
    async with client:
        await load_ext()
        await client.start(token)

asyncio.run(main())