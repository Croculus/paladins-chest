import discord
import paladins_scraper, datetime
from discord.ext import commands, tasks

token ='MTA0NjQ2NjIyMDE5NjY0MjkzNw.GQwPs6.sh6Dn5frRAfH0GWt4Iyaup9mwsYScKS3VAtdiY'
hours = [datetime.time(i) for i in range(0, 23)]
current_chests = set({})

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.bot.user))
        global channel, me
        channel = self.bot.get_channel(1046571039745900616)
        me = await self.bot.fetch_user(310260290128183296)
        self.check.start()
        

    
    @tasks.loop(seconds=5)
    async def check(self):
        global current_chests
        previous_chests = current_chests
        current_chests = paladins_scraper.main()
        if "Heart's Delights Chest" in current_chests:
            await channel.send(content = "It's here" + me.mention)
        if previous_chests == {} or current_chests == previous_chests:
            await channel.send(content = "Working")
            return
        
        leaving = previous_chests.difference(current_chests)
        new = current_chests.difference(previous_chests)
        embedVar = discord.Embed(title="New Chests in Store")
        embedVar.add_field(name="Leaving Chests", value = str(leaving))
        embedVar.add_field(name="New Chests", value= str(new)) 
        await channel.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(MyCog(bot))

intents = discord.Intents().all()
client = commands.Bot(command_prefix='/', intents=intents)

client.run(token)