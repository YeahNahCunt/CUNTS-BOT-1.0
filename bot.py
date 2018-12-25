import Auth #File contains login and token#
import configparser
import discord
import random
import ctx
import json
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from imgurpython import ImgurClient

#clients or defining variables#

client = commands.Bot(command_prefix = '*')
client.remove_command('help')


#For Bot Debug and status#
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='*help'))
    print('Bot is ready.')
    print(discord.__version__)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('*******************')


@client.command()
async def ping(ctx):
    async with ctx.typing():
        await asyncio.sleep(.05)
            
        await ctx.send('Pong!')

@client.command()
async def pingNSFW(ctx):
    async with ctx.typing():
        await asyncio.sleep(.05)

    if  ctx.channel.is_nsfw():
        await ctx.send("Go for it you filthy animal")
    else : 
        await ctx.send("You can't use that command here idiot! GO to a NSFW room!")


#help command#
@client.command()
async def help(ctx):
    async with ctx.typing():
        await asyncio.sleep(.05)
            
    embed = discord.Embed(
        description = 'Below you will find a list of commands that you can use with me',
        colour = discord.Colour.purple()
    )

    embed.set_author(name='Cunts Bot Helpcenter')
    embed.set_thumbnail(url='https://www.nydailynews.com/resizer/gVvubfLWIcXCqhWyJYTiVte36V4=/800x0/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/3UXXG5RXAOTFCM4K4QXN6WL3SM.jpg')
    embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
    embed.add_field(name=':spy: General :spy:', value=
    '`ping               :` Ping bot to see if online\n'+
    '`pingNSFW           :` Ping bot to see if channel is NSFW', inline=False)
    embed.add_field(name=':baby_bottle: Safe for work commands :baby_bottle:', value=
    '`iwant memes        :` For dank Memes\n'+
    '`iwant gifs         :` For dank Gifs', inline=False)
    embed.add_field(name=':underage: General NSFW :underage:', value=
    '`nsfw amateur       :` Amateur girls\n'+
    '`nsfw anal          :` For your anal fixations\n'+
    '`nsfw ass           :` For some sweet booty\n'+
    '`nsfw boobs         :` Mmmmhhh boobs\n'+
    '`nsfw gonewild      :` random image from gonewild subreddit\n'
    '`nsfw milf          :` Hot mommas\n'+
    '`nsfw gifs          :` Sexy gifs\n'+
    '`nsfw petite        :` Petite cute girls\n'+
    '`nsfw teen          :` Legal teens', inline=False)
    embed.add_field(name=':fire: KINK NSFW :fire:', value=
    '`nsfw blowjob       :` Sexy BJs\n'+
    '`nsfw BDSM          :` Hot, sweaty and rough\n'+
    '`nsfw celeb         :` Celebs and their best nude/sexy content\n'+
    '`nsfw cum           :` We got your protein fix here\n'+
    '`nsfw fit           :` Female Body Perfection\n'
    '`nsfw gay           :` A place for sexy guys\n'+
    '`nsfw lesbian       :` Girl on girl action\n'+
    '`nsfw orgasm        :` "O" Faces. Faces of Ecstasy\n'+
    '`nsfw outfits       :` Hot pics of people in NSFW Outfits\n'+
    '`nsfw pussy         :` It is not about cats\n'+
    '`nsfw thicc         :` Sexy curves\n'+
    '`nsfw thigh         :` Thick thighs and luscious curves\n'+
    '`nsfw trans         :` Traps and trans\n'+
    '`nsfw hentai        :` Rule 34 an dother weeb trash', inline=False)
    embed.add_field(name=':earth_africa: Ethnic NSFW :earth_asia:', value=
    '`nsfw ethnic        :` For your random exotic cravings\n'+
    '`nsfw arab          :` Middle eastern hotties\n'+
    '`nsfw asian         :` For that Eastern taste\n'+
    '`nsfw black         :` Tastes like chocolate\n'+
    '`nsfw latino        :` Hot blooded latin girls\n'
    '`nsfw indian        :` Spicy indian girls\n'+
    '`nsfw white         :` Pale cuties'
    , inline=False)
    embed.add_field(name='\u200b', value='More commands to be added soon :wink:', inline=False)

    await ctx.send(embed=embed)


##Load Cogs##
client.load_extension('cogs.SFWCommands')
client.load_extension('cogs.NSFW')

client.run(Auth.discord_token)