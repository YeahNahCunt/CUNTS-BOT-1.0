import Auth #File contains login and token#
import discord
import random
import ctx
import json
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

#Imgur commands#
 #memes and gifs#
    @commands.command(
        pass_context=True,
        description="used for testing JSON file; can be used as .code_test **subtypename**"
        )
    async def iwant(self, ctx, userinput):
            userinput = userinput.lower() # Capitalisation from user won't matter anymore

            avatar = ctx.message.author.avatar_url
    
            author = ctx.message.author

            with open('SFW_SubList.json') as f:
                data = json.load(f)

            for category in data: # Iterate through json file, picks random sub from list
                if userinput in category["subname"]:
                
                    sub_rand = random.choice(category["sublist"])

            rand = random.randint(0, 59)  # 60 results generated per page

            items = grab.subreddit_gallery(subreddit =sub_rand)

            image = (items[rand].link)

            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.blurple(),
                )
 
            if image.endswith(('.jpg','.jpeg','.gif','.gifv')):
                embed.set_image(url=image)

            if image.endswith('.mp4'):
                embed.video(url=image)

            embed.add_field(name='\u200b',value='From : r/'+ sub_rand, inline=False) ###'\u200b' HTML cheat to keep field clear##

            embed.add_field(name='\u200b', value=image, inline=False)

            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(SFWCog(client))