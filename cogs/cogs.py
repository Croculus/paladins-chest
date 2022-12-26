import paladins_scraper, discord
from discord.ext import commands, tasks

current_chests = set({})

class chestCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.bot.user))
        global channel, me
        channel = self.bot.get_channel(1046571039745900616)
        me = await self.bot.fetch_user(310260290128183296)
        self.check.start()
        

    
    @tasks.loop(seconds=5.0)
    async def check(self):
        global current_chests, count
        previous_chests = current_chests
        current_chests = paladins_scraper.main()
        
        if "Cyber Tech Chest" in current_chests:
            await channel.send(content = "It's here" + me.mention)

        elif current_chests == previous_chests:
            return
        leaving = previous_chests.difference(current_chests)
        new = current_chests.difference(previous_chests)
        embedVar = discord.Embed(title="New Chests in Store")
        embedVar.add_field(name="Leaving Chests", value = str(leaving))
        embedVar.add_field(name="New Chests", value= str(new)) 
        
        await channel.send(embed=embedVar)

class dailyDealCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    

    
async def setup(bot):
    await bot.add_cog(chestCheck(bot))