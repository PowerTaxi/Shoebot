import discord
from discord.ext import commands
try: # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
import requests

class Scraper(object):
    def __init__(self):
        self.s = requests.Session()

    def update_headers(self, headers):
        self.s.headers.update(headers)

    def make_request(self, url=None):
        return self.s.get(url)

class ffxiv:
    def __init__(self,bot):
        self.bot = bot
        self.lodestone_domain = 'eu.finalfantasyxiv.com'
        self.lodestone_url = 'http://%s/lodestone' % self.lodestone_domain

    @commands.command()
    async def news(self):
        url = self.lodestone_url + '/news/'
        await self.bot.say(url)

    @commands.command()
    async def topics(self):
        url = self.lodestone_url + '/topics/'
        await self.bot.say(url)

    @commands.command()
    async def characters(self):
        url = self.lodestone_url + '/character/'
        await self.bot.say(url)

    @commands.command()
    async def ftest(self, name: str):
        url = self.lodestone_url + '/character/'
        if name == "RobinWalker":
            char_url = url + '2691513/'
            await self.bot.say(char_url)
        if name == "SpydIgg":
            char_url = url + '3334848/'
            await self.bot.say(char_url)



        # async with aiohttp.get(url) as response:
        #     soup = BeautifulSoup(await response.text(), "html.parser")
        # try:
        #     online = soupObject.find(class_='home-stats').find('li').find('strong').get_text()
        #     await self.bot.say(online + ' players are playing this game at the moment')
        # except:
        #     await self.bot.say("Couldn't load amount of players. No one is playing this game anymore or there's an error.")

def setup(bot):
    bot.add_cog(ffxiv(bot))
