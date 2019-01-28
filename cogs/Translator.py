import discord
from discord.ext import commands

from googletrans import Translator

# from textblob import TextBlob

client = discord.Client()
# detect_lang = blob.detect_language()

# translate_eng = blob.translate(to= 'en')

class Translate:
    def __init__(self, client):
        self.client = client
    
    async def on_ready(self):
        print('Translator is Prepared')

    async def on_reaction_add(self, reaction, user):
        channel_react = reaction.message.channel

        avatar = reaction.message.author.avatar_url
        author = reaction.message.author

            
        if reaction.emoji == '🇬🇧':  # United Kingdom flag (english translation)
            translator = Translator()
            reply = translator.translate(reaction.message.content, dest='en').text
            lang_detect= translator.detect(reaction.message.content)
            embed = discord.Embed(
                title = author.name + " said:",
                description = reaction.message.content,
                color=0xff00ff,
                )
            embed.set_thumbnail(url= avatar)
            # embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name="From that I've translated the following:", value=reply , inline=False)

            await channel_react.send(embed=embed)
            # await channel_react.send(lang_detect.lang + lang_detect.confidence)

        if reaction.emoji == '🇸🇦':  # Saudi flag (Arab translation)
            translator = Translator()
            reply = translator.translate(reaction.message.content, dest='ar').text
            lang_detect= translator.detect(reaction.message.content)
            embed = discord.Embed(
                title = author.name + " said:",
                description = reaction.message.content,
                color=0xff00ff,
                )
            embed.set_thumbnail(url= avatar)
            # embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name="From that I've translated the following:", value=reply , inline=False)

            await channel_react.send(embed=embed)
            # await channel_react.send(lang_detect.lang + lang_detect.confidence)




def setup(client):
    client.add_cog(Translate(client))