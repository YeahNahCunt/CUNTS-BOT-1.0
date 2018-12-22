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

class SFWCog:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print('SFWCog is Prepared')

    @commands.command()
    async def sfw(self, ctx):
        await ctx.send('sfw')


#Imgur commands#
 #memes#
    @commands.command(pass_context=True)
    async def meme(self, ctx):
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'AdviceAnimals',
            'memes',
            'trippinthroughtime',
            'BikiniBottomTwitter',
            'dankmemes',
            'madlads',
            'bidenbro',
            'memeeconomy',
            'rarepuppers',
            'wholesomememes',
            'dankchristianmemes',
            'terriblefacebookmemes',
            'prequelmemes',
            'dank_meme',
            'trebuchetmemes',
            'deepfriedmemes',
            'Overwatch_Memes',
            'see',
            'SequelMemes',
            'surrealmemes',
            'bonehurtingjuice',
            'bossfight',
            'historymemes',
            'animemes',
            'suddenlygay',
            'absoluteunits',
            'delightfullychubby',
            'Memes_Of_The_Dank',
            'smoobypost',
            'lotrmemes',
            'ilikthebred',
            'meme',
            'garlicbreadmemes',
            'offensivememes',
            'gocommitdie',
            'wholesomegreentext',
            'raimememes',
            'otmemes',
            'kappa',
            'equelmemes',
            'namflashbacks',
            'me_irl',
            'meirl',
            'anime_irl',
            '2meirl4meirl',
            'meow_irl',
            'woof_irl',
            'TooMeIrlForMeIrl',
            'absolutelynotme_irl',
            'absolutelynotmeirl'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)
            sublink =(items[rand].tags)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.blurple(),
                )
            embed.set_image(url=image)
            embed.add_field(name=':poop:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)

 #gifs#
    @commands.command(pass_context=True)
    async def gifs(self, ctx):
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'gifs',
            'behindthegifs',
            'gif',
            'Cinemagraphs',
            'WastedGifs',
            'educationalgifs',
            'perfectloops',
            'highqualitygifs',
            'gifsound',
            'combinedgifs',
            'retiredgif',
            'michaelbaygifs',
            'gifrecipes',
            'mechanical_gifs',
            'bettereveryloop',
            'gifextra',
            'slygifs',
            'gifsthatkeepongiving',
            'wholesomegifs',
            'noisygifs',
            'brokengifs',
            'loadingicon',
            'splitdepthgifs',
            'blackpeoplegifs',
            'whitepeoplegifs',
            'asianpeoplegifs',
            'scriptedasiangifs',
            'reactiongifs',
            'shittyreactiongifs',
            'chemicalreactiongifs',
            'physicsgifs',
            'babyelephantgifs',
            'weathergifs',
            'animegifs',
            'seinfeldgifs',
            'animaltextgifs',
            'babyelephantgifs',
            'happycowgifs',
            'babybigcatgifs',
            'bigcatgifs',
            'catgifs',
            'gifsthatendtoosoon',
            'shittyreactiongifs',
            'dashcamgifs',
            'hmmmgifs'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)
            sublink =(items[rand].tags)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.blurple(),
                )
            embed.set_image(url=image)
            embed.add_field(name=':poop:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)





def setup(client):
    client.add_cog(SFWCog(client))