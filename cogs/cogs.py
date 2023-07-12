import paladins_scraper, discord, datetime, deal_to_txt, os
from discord.ext import commands, tasks

current_chests = set({})
watch_list = []
wanted_chests = []
class chestCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.bot.user))
        global channel, me
        channel = self.bot.get_channel(int(os.getenv('CHANNEL')))
        me = await self.bot.fetch_user(int(os.getenv('USER_ID')))
        self.check.start()
        

    
    @tasks.loop(seconds=5.0)
    async def check(self):
        global current_chests, count
        previous_chests = current_chests
        current_chests = paladins_scraper.main()
        
        if wanted_chests in current_chests:
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

    @commands.Cog.listener()    
    async def on_ready(self):
        self.deals.start()

    @tasks.loop(time=datetime.time(11))
    async def deals(self):
        deals = deal_to_txt.main()
        for deal in deals:
            if any(item in deal for item in watch_list):
                await channel.send(content = "It's here" + me.mention)
        embedVar = discord.Embed(title="Daily Deals")
        embedVar.add_field(name="Deal 1", value = deals[0])
        embedVar.add_field(name="Deal 2", value = deals[1])
        embedVar.add_field(name="Deal 3", value = deals[2])
        await channel.send(embed=embedVar)
    
    
    

    
async def setup(bot):
    await bot.add_cog(chestCheck(bot))
    await bot.add_cog(dailyDealCheck(bot))