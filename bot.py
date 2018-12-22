import Auth #File contains login and token#
import configparser
import discord
import ctx
from discord.ext import commands

#clients or defining variables#

client = commands.Bot(command_prefix = '.')
client.remove_command('help')


#For Bot Debug and status#
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='.help'))
    print('Bot is ready.')
    print(discord.__version__)

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def pingNSFW(ctx):
    if  ctx.channel.is_nsfw():
        await ctx.send("Go for it you filthy animal")
    else : 
        await ctx.send("You can't use that command here idiot! GO to a NSFW room!")


#help command#
@client.command()
async def help(ctx):
    embed = discord.Embed(
        description = 'Below you will find a list of commands that you can use with me',
        colour = discord.Colour.purple()
    )

    embed.set_author(name='Cunts Bot Helpcenter')
    embed.set_thumbnail(url='https://www.nydailynews.com/resizer/gVvubfLWIcXCqhWyJYTiVte36V4=/800x0/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/3UXXG5RXAOTFCM4K4QXN6WL3SM.jpg')
    embed.set_footer(text='Any reccomendations/requests/bugs can be directed to Cunt ( Disturbed#3853 )')
    embed.add_field(name=':spy: General :spy:', value=
    '`ping      :` Ping bot to see if online\n'+
    '`pingNSFW  :` Ping bot to see if channel is NSFW', inline=False)
    embed.add_field(name=':baby_bottle: Safe for Commands :baby_bottle:', value=
    '`meme      :` For dank Memes\n'+
    '`gifs      :` For dank Gifs', inline=False)
    embed.add_field(name=':underage: General NSFW :underage:', value=
    '`amateur   :` Amateur girls\n'+
    '`anal      :` For your anal fixations\n'+
    '`ass       :` For some sweet booty\n'+
    '`boobs     :` Mmmmhhh boobs\n'+
    '`gonewild  :` random image from gonewild subreddit\n'
    '`milf      :` Hot mommas\n'+
    '`NSFWgifs  :` Sexy gifs\n'+
    '`petite    :` Petite cute girls\n'+
    '`teen      :` Legal teens', inline=False)
    embed.add_field(name=':fire: KINK NSFW :fire:', value=
    '`blowjob   :` Sexy BJs\n'+
    '`BDSM      :` Hot, sweaty and rough\n'+
    '`celeb     :` Celebs and their best nude/sexy content\n'+
    '`cum       :` We got your protein fix here\n'+
    '`fit       :` Female Body Perfection\n'
    '`gay       :` A place for sexy guys\n'+
    '`lesbian   :` Girl on girl action\n'+
    '`orgasm    :` "O" Faces. Faces of Ecstasy\n'+
    '`outfits   :` Hot pics of people in NSFW Outfits\n'+
    '`pussy     :` It is not about cats\n'+
    '`thicc     :` Sexy curves\n'+
    '`thigh     :` Thick thighs and luscious curves\n'+
    '`trans     :` Traps and trans\n'+
    '`hentai    :` Rule 34 an dother weeb trash', inline=False)
    embed.add_field(name=':earth_africa: Ethnic NSFW :earth_asia:', value=
    '`ethnic    :` For your random exotic cravings\n'+
    '`arab      :` Middle eastern hotties\n'+
    '`asian     :` For that Eastern taste\n'+
    '`black     :` Tastes like chocolate\n'+
    '`latino    :` Hot blooded latin girls\n'
    '`indian    :` Spicy indian girls\n'+
    '`white     :` Pale cuties'
    , inline=False)

    await ctx.send(embed=embed)

##Load Cogs##
client.load_extension('cogs.SFWCommands')
client.load_extension('cogs.NSFW')

client.run(Auth.discord_token)