import discord
from discord.ext import commands
import requests

#http://www.giantbomb.com/api/search?api_key=[YOUR-KEY]
#&format=[RESPONSE-DATA-FORMAT]&query=[YOUR-SEARCH]&resources=[SOME-TYPES]
key = " "
search_url = 'https://www.giantbomb.com/api/search/?api_key=' + key + '&format=json&query='

home_url = 'https://www.giantbomb.com'
headers = {'User-Agent': 'PowerTaxiDiscordBot. Making this to help me learn Python'}

class giantbomb():
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def wiki(self):
        url = home_url + '/games/'
        await self.bot.say(url)

    @commands.command()
    async def search(self, ctx:str, ctx2:str):

        if ctx2 == "game":
            try:
                game = ctx.replace("-"," ")
                game_url = search_url + game + '&resources=game'
                r = requests.get(game_url,headers=headers).json()
                releaseDate = r['results'][0]['original_release_date']
                name = r['results'][0]['name']
                siteLink = r['results'][0]['site_detail_url']
                deck = r['results'][0]['deck']
                embed = discord.Embed(title="{}'s Information".format(name),description="Stuff", color=0xff0000)
                embed.add_field(name="Name", value = name, inline = True)
                embed.add_field(name="Release Date", value = releaseDate, inline = True)
                embed.add_field(name="Site Link", value = siteLink, inline = True)
                embed.add_field(name="Description", value = deck, inline = True)
                embed.set_thumbnail(url=r['results'][0]['image']['thumb_url'])
                await self.bot.say(embed=embed)
            except IndexError:
                await self.bot.say("You sure you didn't fuck up the spelling there mate?")

        if ctx2 == "franchise":
            try:
                franchise = ctx.replace("-"," ")
                game_url = search_url + franchise + '&resources=franchise'
                r = requests.get(game_url,headers=headers).json()
                name = r['results'][0]['name']
                siteLink = r['results'][0]['site_detail_url']
                deck = r['results'][0]['deck']
                embed = discord.Embed(title="{}'s Information".format(name),description="Stuff", color=0xff0000)
                embed.add_field(name="Name", value = name, inline = True)
                embed.add_field(name="Site Link", value = siteLink, inline = True)
                embed.add_field(name="Description", value = deck, inline = True)
                embed.set_thumbnail(url=r['results'][0]['image']['thumb_url'])
                await self.bot.say(embed=embed)
            except IndexError:
                await self.bot.say("You sure you didn't fuck up the spelling there mate?")

        if ctx2 == "character":
            try:
                person = ctx.replace("-"," ")
                person_url = search_url + person + '&resources=character'
                r = requests.get(person_url,headers=headers).json()
                firstGame = r['results'][0]['first_appeared_in_game']['name']
                name = r['results'][0]['name']
                siteLink = r['results'][0]['site_detail_url']
                deck = r['results'][0]['deck']
                embed = discord.Embed(title="{}'s Information".format(name),description="Stuff", color=0xff0000)
                embed.add_field(name="Name", value = name, inline = True)
                embed.add_field(name="Game", value = firstGame, inline = True)
                embed.add_field(name="Site Link", value = siteLink, inline = True)
                embed.add_field(name="Description", value = deck, inline = True)
                embed.set_thumbnail(url=r['results'][0]['image']['thumb_url'])
                await self.bot.say(embed=embed)
            except IndexError:
                await self.bot.say("You sure you didn't fuck up the spelling there mate?")

        if ctx2 == "company":
            try:
                company = ctx.replace("-"," ")
                company_url = search_url + company + '&resources=company'
                r = requests.get(company_url,headers=headers).json()
                date = r['results'][0]['date_founded']
                name = r['results'][0]['name']
                siteLink = r['results'][0]['site_detail_url']
                deck = r['results'][0]['deck']
                embed = discord.Embed(title="{}'s Information".format(name), color=0xff0000)
                embed.add_field(name="Name", value = name, inline = True)
                embed.add_field(name="Founded", value = date, inline = True)
                embed.add_field(name="Site Link", value = siteLink, inline = True)
                embed.add_field(name="Description", value = deck, inline = True)
                embed.set_thumbnail(url=r['results'][0]['image']['thumb_url'])
                await self.bot.say(embed=embed)
            except IndexError:
                await self.bot.say("You sure you didn't fuck up the spelling there mate?")

        if ctx2 == "person":
            try:
                person = ctx.replace("-"," ")
                person_url = search_url + person + '&resources=person'
                r = requests.get(person_url,headers=headers).json()
                name = r['results'][0]['name']
                country = r['results'][0]['country']
                birthday = r['results'][0]['birth_date']
                siteLink = r['results'][0]['site_detail_url']
                deck = r['results'][0]['deck']
                firstGame = r['results'][0]['first_credited_game']['name']
                embed = discord.Embed(title="{}'s Information".format(name),description="Stuff", color=0xff0000)
                embed.add_field(name="Name", value = name, inline = True)
                embed.add_field(name="Country", value = country, inline = True)
                embed.add_field(name="Date Of Birth", value = birthday, inline = True)
                embed.add_field(name="Site Link", value = siteLink, inline = True)
                embed.add_field(name="First Credited Game", value = firstGame, inline = True)
                embed.add_field(name="Description", value = deck, inline = True)
                embed.set_thumbnail(url=r['results'][0]['image']['thumb_url'])
                await self.bot.say(embed=embed)
            except IndexError:
                await self.bot.say("You sure you didn't fuck up the spelling there mate?")

def setup(bot):
    bot.add_cog(giantbomb(bot))
