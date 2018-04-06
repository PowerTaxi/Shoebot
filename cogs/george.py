import discord
import random
from discord.ext import commands

class george:
    """My custom cog that does stuff!"""
    gifsdir = "gifs"
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def giam(self):
        """This does stuff!"""
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='https://media.giphy.com/media/c8bcSH9VQkQRq/giphy.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def ghappy(self):
        #http://www.reactiongifs.com/wp-content/uploads/2013/06/costanza-wink.gif
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='http://www.reactiongifs.com/wp-content/uploads/2013/06/costanza-wink.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def gcool(self):
        #https://giphy.com/gifs/person-showing-constanza-m3MwWDFPxQVSU
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='https://media.giphy.com/media/ly69OqtnnQg2k/giphy.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def gdown(self):
        #https://media.giphy.com/media/ChMy4X2DkiLTy/giphy.gif
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='https://media.giphy.com/media/ChMy4X2DkiLTy/giphy.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def gbat(self):
        #https://.media.giphy.com/media/P4sjB6SI2fErK/giphy.gif
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='https://media.giphy.com/media/P4sjB6SI2fErK/giphy.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def gstaycool(self):
        #await self.bot.say('https://media.giphy.com/media/sNNYg1PEc8ww0/giphy.gif')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='https://media.giphy.com/media/sNNYg1PEc8ww0/giphy.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def gwhat(self):
        #await self.bot.say('http://i.imgur.com/vqz6j7O.gif')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='http://i.imgur.com/vqz6j7O.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def gclap(self):
        #await self.bot.say('http://i.imgur.com/6P0nyKN.gif')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='http://i.imgur.com/6P0nyKN.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def gsexy(self):
        #await self.bot.say('http://i.imgur.com/O6HWZhH.gif')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='http://i.imgur.com/O6HWZhH.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def gnervous(self):
        #await self.bot.say('http://i.imgur.com/MwBWTnW.gif')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='http://i.imgur.com/MwBWTnW.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def gsurprise(self):
        #await self.bot.say('http://imgur.com/2KPWeHt')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='http://i.imgur.com/MwBWTnW.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def jsmug(self):
        #await self.bot.say('https://media.giphy.com/media/e2QYPpUe8WmpG/giphy.gif')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='https://media.giphy.com/media/e2QYPpUe8WmpG/giphy.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def kenter(self):
        #await self.bot.say('https://media.giphy.com/media/sdp6mLGIMbGWA/giphy.gif')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='https://media.giphy.com/media/sdp6mLGIMbGWA/giphy.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def kletsgo(self):
        #await self.bot.say('https://media.giphy.com/media/3o7TKUM3IgJBX2as9O/giphy.gif')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='https://media.giphy.com/media/3o7TKUM3IgJBX2as9O/giphy.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def krunning(self):
        #await self.bot.say('http://www.reactiongifs.com/wp-content/uploads/2013/12/omgwtf.gif')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='http://www.reactiongifs.com/wp-content/uploads/2013/12/omgwtf.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def khi(self):
        #await self.bot.say('http://i.imgur.com/vjg0a26.gif')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='http://i.imgur.com/vjg0a26.gif')
        await self.bot.say(embed=embed)

    @commands.command()
    async def dance(self):
        #await self.bot.say('http://i.imgur.com/caHDSe2.gif')
        embed = discord.Embed(color=0xff0000)
        embed.set_image(url='http://i.imgur.com/caHDSe2.gif')
        await self.bot.say(embed=embed)

    # list = ['ghappy', 'gcool', 'gdown', 'giam', 'gbat', 'staycool', 'gclap', 'gsexy', 'gwhat', 'gnervous',
    # 'khi', 'krunning','kenter', 'kletsgo','dance','jsmug']
    # @commands.command()
    # async def slist(self):
    #     embed = discord.Embed(title="Gif List",description="Stuff", color=0xff0000)
    #     # for i in list:
    #     #     embed.add_field(name= "Gif ", value = list[i], inline = True)
    #
    #     embed.add_field(name="1", value = list[0], inline = True)
    #     embed.add_field(name="2", value = list[1], inline = True)
    #     embed.add_field(name="3", value = list[2], inline = True)
    #     embed.add_field(name="4", value = list[3], inline = True)
    #     embed.add_field(name="5", value = list[4], inline = True)
    #     embed.add_field(name="6", value = list[5], inline = True)
    #     embed.add_field(name="7", value = list[6], inline = True)
    #     embed.add_field(name="8", value = list[7], inline = True)
    #     embed.add_field(name="9", value = list[8], inline = True)
    #     embed.add_field(name="10", value = list[9], inline = True)
    #     embed.add_field(name="11", value = list[10], inline = True)
    #     embed.add_field(name="12", value = list[11], inline = True)
    #     embed.add_field(name="13", value = list[12], inline = True)
    #     embed.add_field(name="14", value = list[13], inline = True)
    #     embed.add_field(name="15", value = list[14], inline = True)
    #     embed.add_field(name="16", value = list[15], inline = True)
    #
    #     await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(george(bot))
