import requests
import discord
import asyncio
import bs4
from bs4 import BeautifulSoup
from discord.ext import commands


#####testing code####


# hadith_book_list = ['bukhari', 'muslim', 'tirmidhi', 'abudawud', 'nasai', 'ibnmajah', 'malik', 'riyadussaliheen',
#                     'adab', 'bulugh', 'qudsi', 'nawawi']


# hadith_name = 'tirmidhi'
# book = '3'
# hadith_number = '5'

# #parsing
# webPage = requests.get("https://sunnah.com/"+ hadith_name + "/" + book + "/" + hadith_number)
# dataSet = BeautifulSoup(webPage.content,"html.parser")
# hadithBooks = dataSet.find_all(class_ = "collection_title")



# # specific
# bookname_english = dataSet.find_all(class_ = "book_page_english_name")

# bookname_arabic = dataSet.find_all(class_ = "book_page_arabic_name arabic")

# hadith_parsed_english = dataSet.find_all(class_ = "english_hadith_full")

# hadith_parsed_arabic = dataSet.find_all(class_ = "arabic_hadith_full arabic")

# hadith_reference = dataSet.find_all(class_ = "hadith_reference")


# # stripped data
# stripped_bookname_english = [bookE.text.strip() for bookE in bookname_english]

# stripped_bookname_arabic = [bookA.text.strip() for bookA in bookname_arabic]

# stripped_hadith_english = [hadithE.text.strip() for hadithE in hadith_parsed_english]

# stripped_hadith_arabic = [hadithA.text.strip() for hadithA in hadith_parsed_arabic]

# stripped_reference = [hadith_ref.text.strip() for hadith_ref in hadith_reference]

# print(stripped_bookname_english)
# print(stripped_bookname_arabic)
# print(stripped_hadith_english)
# print(stripped_hadith_arabic)
# print(stripped_reference)

class Hadith:
    def __init__(self, client):
        self.client = client
    
    async def on_ready(self):
        print('Hadith is Prepared')

    @commands.command(
        pass_context=True
        )
    async def hadith(self, ctx): 
          
        async with ctx.typing():
            await asyncio.sleep(.05)

        hadith_name = 'bukhari'
        book = '1'
        hadith_number = '1'

        #parsing
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
        webPage = requests.get("https://sunnah.com/"+ hadith_name + "/" + book + "/" + hadith_number, headers= headers)
        dataSet = bs4.BeautifulSoup(webPage.content,"html.parser")
        # hadithBooks = dataSet.find_all(class_ = "collection_title")



        # specific
        bookname_english = dataSet.find_all(class_ = "book_page_english_name")

        bookname_arabic = dataSet.find_all(class_ = "book_page_arabic_name arabic")

        hadith_parsed_english = dataSet.find_all(class_ = "english_hadith_full")

        hadith_parsed_arabic = dataSet.find_all(class_ = "arabic_hadith_full arabic")

        hadith_reference = dataSet.find_all(class_ = "hadith_reference")


        # stripped data
        stripped_bookname_english = [bookE.text.strip() for bookE in bookname_english]

        stripped_bookname_arabic = [bookA.text.strip() for bookA in bookname_arabic]

        stripped_hadith_english = [hadithE.text.strip() for hadithE in hadith_parsed_english]

        stripped_hadith_arabic = [hadithA.text.strip() for hadithA in hadith_parsed_arabic]

        stripped_reference = [hadith_ref.text.strip() for hadith_ref in hadith_reference]
        
        embed = discord.Embed( title = 'test',
                description = 'test',
                url= 'https://sunnah.com/',
                colour=0x00ff80,
                )
        embed.add_field(name= (stripped_hadith_english) ,value= 'test' , inline=False)

        await ctx.send(embed=embed)
        print(stripped_hadith_english)





def setup(client):
    client.add_cog(Hadith(client))