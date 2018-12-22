import Auth #File contains login and token#
import discord
import random
import ctx
from discord.ext import commands
from imgurpython import ImgurClient

#clients or defining variables#
client_id = Auth.client_id
client_secret = Auth.client_secret
grab = ImgurClient(client_id, client_secret) #had to give it a diffrent call to function from client as Discords prefix utilises "client" call to function#
items = grab.gallery()

class NSFWCog:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print('NSFWCog is Prepared')

    @commands.command()
    async def nsfw(self, ctx):
        await ctx.send('nsfw')


### General NSFW ###
 #amateur#
    @commands.command(pass_context=True)
    async def amateur(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'realgirls',
            'amateur',
            'homemadexxx',
            'dirtypenpals',
            'festivalsluts',
            'CollegeAmateurs',
            'amateurcumsluts',
            'nsfw_amateurs',
            'funwithfriends',
            'randomsexiness',
            'amateurporn',
            'normalnudes',
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.gold()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!") 
 #ass#
    @commands.command(pass_context=True)
    async def ass(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'asstastic',
            'booty',
            'tushy',
            'assdrop',
            'booty_gifs',
            'showing_off_her_ass'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.gold()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")         
 #Gonewild#
    @commands.command(pass_context=True)
    async def gonewild(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'gonewild',
            'gonewild30plus',
            'gifsgonewild'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.gold()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #MILF#
    @commands.command(pass_context=True)
    async def milf(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'milf',
            'gonewild30plus',
            'realmoms',
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.gold()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
#Teen#
    @commands.command(pass_context=True)
    async def teen(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'legalteens',
            'collegesluts',
            'adorableporn',
            'legalteensXXX',
            'gonewild18',
            '18_19',
            'just18',
            'PornStarletHQ',
            'fauxbait',
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.gold()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
#NSFWgifs#
    @commands.command(pass_context=True)
    async def NSFWgif(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'GentlemanBonersGifs',
            'gifsofremoval',
            'gifsgonewild',
            'NSFW_GIF',
            'nsfw_gifs',
            'porn_gifs',
            'porninfifteenseconds',
            'CuteModeSlutMode',
            '60fpsporn',
            'NSFW_HTML5',
            'the_best_nsfw_gifs'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.gold()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")

def setup(client):
    client.add_cog(NSFWCog(client))