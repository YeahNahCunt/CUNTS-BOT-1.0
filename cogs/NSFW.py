import Auth #File contains login and token#
import discord
import random
import ctx
import json
import asyncio
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

#Imgur commands#
    @commands.command(
        pass_context=True,
        description="used for testing JSON file; can be used as .code_test **subtypename**"
        )
    async def nsfw(self, ctx, userinput):
        if  ctx.channel.is_nsfw(): #catching NSFW rooms (may need to build a separate cog for this stuff)
            async with ctx.typing():
                await asyncio.sleep(.05)

                userinput = userinput.lower() # Capitalisation from user won't matter anymore

                avatar = ctx.message.author.avatar_url
    
                author = ctx.message.author

                with open('NSFW_Sublist.json') as f:
                    data = json.load(f)

                for category in data: # Iterate through json file, picks random sub from list
                    if userinput in category["subname"]:
                
                        sub_rand = random.choice(category["sublist"])

                rand = random.randint(0, 59)  # 60 results generated per page

                items = grab.subreddit_gallery(subreddit =sub_rand)

                try:
                    image = (items[rand].link)
                except IndexError:
                    embed_error = discord.Embed(
                        title ="OH NOO! :grimacing: my search couldn't find anything, please try again!",
                        colour= discord.Colour.red()
                        )
                    embed_error.set_image(url='https://i.imgur.com/J4WMX0y.gif')
                
                    await ctx.send(embed=embed_error) ###To handle Index error#
                    print(sub_rand)##to catch subs that often consistantly invoke Index error so I can remove them##

                imagename = (items[rand].title)

                embed = discord.Embed(
                    title = imagename,
                    colour = discord.Colour.teal(),
                    )
 
                if image.startswith(('https://imgur.com/a/')):##to catch album links##
                    embed.add_field(name=':kiss: :sparkling_heart: **WOW! The porn gods have seen fit to grant you a gift of not one but a WHOLE album of smut!**:sparkling_heart::kiss:', value='Click the link below and happy fapping:\n' + image, inline=False)


                if image.endswith(('.jpg','.jpeg','.gif','.png')):
                    embed.set_image(url=image)
                    embed.add_field(name='\u200b', value='Not loading? Here is a link:\n' + image, inline=False)

                embed.add_field(name='\u200b',value='From : r/'+ sub_rand, inline=False) ###'\u200b' HTML cheat to keep field clear##

                if image.endswith('.mp4'):
                    embed.add_field(name=':arrow_down:  :arrow_down:  :arrow_down:  :arrow_down:  :arrow_down:  :arrow_down:  :arrow_down:  :arrow_down:', value='\u200b', inline=False) ###BECAUSE DISCORD DOES NOT SUPPORT VIDEO EMBEDS##.
                    embed.add_field(name='\u200b', value='Not loading? Here is a link:\n' + image, inline=False)

                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

                await ctx.send(embed=embed)            
                if image.endswith('.mp4'):
                    await ctx.send(image)   
            
                print(sub_rand)##to catch subs that often consistantly invoke any other errors such as error so I can remove them##

        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
            


        


def setup(client):
    client.add_cog(NSFWCog(client))