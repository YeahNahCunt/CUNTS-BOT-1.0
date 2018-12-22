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
                colour = discord.Colour.blue()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!") 
 #anal#
    @commands.command(pass_context=True)
    async def anal(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'anal',
            'analgw',
            'painal',
            'masterofanal',
            'buttsharpies'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.blue()
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
            'showing_off_her_ass',
            'thickthighs'
            'ass',
            'facedownassup',
            'assinthong',
            'bigasses',
            'buttplug',
            'TheUnderbun',
            'pawg'
            'paag',
            'cutelittlebutts',
            'hipcleavage',
            'frogbutt',
            'HungryButts',
            'cottontails',
            'lovetowatchyouleave'
            'celebritybutts',
            'cosplaybutts',
            'asshole',
            'AssholeBehindThong',
            'assholegonewild',
            'spreadem',
            'girlsinyogapants',
            'yogapants'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.blue()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #boobs#
    @commands.command(pass_context=True)
    async def boobs(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'massivetitsnass',
            'boobies',
            'TittyDrop',
            'boltedontits',
            'boobbounce',
            'boobs',
            'downblouse',
            'homegrowntits',
            'cleavage',
            'breastenvy',
            'torpedotits',
            'thehangingboobs',
            'page3glamour',
            'BustyPetite',
            'hugeboobs',
            'stacked',
            'burstingout',
            'BigBoobsGW',
            'bigboobsgonewild',
            '2busty2hide',
            'bigtiddygothgf',
            'engorgedveinybreasts',
            'pokies',
            'ghostnipples',
            'nipples',
            'puffies',
            'tinytits',
            'aa_cups'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.blue()
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
            'gifsgonewild',
            'PetiteGoneWild',
            'gonemild',
            'altgonewild',
            'treesgonewild',
            'gifsgonewild',
            'GWNerdy',
            'analgw',
            'gonewildsmiles',
            'onstageGW'
            'RepressedGoneWild',
            'UnderwearGW',
            'LabiaGW',
            'TributeMe',
            'WeddingsGoneWild',
            'gwpublic',
            'assholegonewild',
            'leggingsgonewild',
            'dykesgonewild',
            'snapchatgw',
            'goneerotic',
            'gonewildhairy',
            'gonwild',
            'ratemynudebody',
            'onmww',
            'gonewild18',
            'GWCouples',
            'gonewildcouples',
            'gwcumsluts',
            'WouldYouFuckMyWife',
            'gonewildcurvy',
            'GoneWildplus',
            'BigBoobsGW',
            'bigboobsgonewild',
            'mycleavage',
            'workgonewild',
            'GoneWildScrubs',
            'swingersgw',
            'militarygonewild',
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.blue()
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
            'onmww'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.blue()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #NSFWgifs#
    @commands.command(pass_context=True)
    async def NSFWgifs(self, ctx):
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
                colour = discord.Colour.blue()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #Petite#
    @commands.command(pass_context=True)
    async def petite(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'BustyPetite',
            'dirtysmall',
            'petitegonewild',
            'xsmallgirls',
            'funsized',
            'hugedicktinychick'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.blue()
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
                colour = discord.Colour.blue()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")

### Kinks NSFW ###
 #Blowjobs# 
    @commands.command(pass_context=True)
    async def blowjob(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'blowjobs',
            'lipsthatgrip',
            'deepthroat',
            'onherknees',
            'blowjobsandwich'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #BDSM# 
    @commands.command(pass_context=True)
    async def BDSM(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'BDSM',
            'Bondage',
            'BDSMcommunity',
            'bdsmgw',
            'nsfwhardcore',
            'SheLikesItRough',
            'strugglefucking',
            'jigglefuck',
            'freeuse',
            'whenitgoesin',
            'outercourse',
            'gangbang',
            'breeding',
            'pegging',
            'insertions',
            'passionx',
            'pronebone',
            'facesitting',
            'nsfw_plowcam',
            'facefuck'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #celebrity# 
    @commands.command(pass_context=True)
    async def celeb(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'celebnsfw',
            'WatchItForThePlot',
            'nsfwcelebarchive',
            'celebritypussy',
            'oldschoolcoolNSFW',
            'extramile',
            'jerkofftocelebs',
            'celebritybutts',
            'onoffcelebs'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #Cum#
    @commands.command(pass_context=True)
    async def cum(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'creampies',
            'throatpies',
            'FacialFun',
            'cumonclothes',
            'oralcreampie',
            'cumsluts',
            'GirlsFinishingTheJob',
            'cumfetish',
            'amateurcumsluts',
            'cumcoveredfucking',
            'cumhaters',
            'before_after_cumsluts',
            'pulsatingcumshots',
            'impressedbycum'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #Fit# 
    @commands.command(pass_context=True)
    async def fit(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'SexyTummies',
            'theratio',
            'fitgirls',
            'bodyperfection',
            'samespecies',
            'athleticgirls',
            'volleyballgirls',
            'Ohlympics',
            'hardbodies',
            'asianfitgirls'
            'Deathbysnusnu',
            'fbb_NSFW',
            'SkinnyWithAbs',
            'CrossfitGirls'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #gay# 
    @commands.command(pass_context=True)
    async def gay(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'ladybonersgw',
            'massivecock',
            'chickflixxx',
            'gaybrosgonewild'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #Lesbian# 
    @commands.command(pass_context=True)
    async def lesbian(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'twingirls',
            'groupofnudegirls',
            'Ifyouhadtopickone',
            'dykesgonewild',
            'lesbians',
            'StraightGirlsPlaying',
            'girlskissing',
            'mmgirls',
            'Lesdom'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #Masterbation# 
    @commands.command(pass_context=True)
    async def orgasm(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'holdthemoan',
            'O_faces',
            'jilling',
            'gettingherselfoff',
            'quiver',
            'GirlsHumpingThings',
            'forcedorgasms',
            'mmgirls',
            'ruinedorgasms',
            'suctiondildos',
            'baddragon',
            'grool',
            'squirting'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #outfits# 
    @commands.command(pass_context=True)
    async def outfits(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'OnOff',
            'nsfwoutfits',
            'girlswithglasses',
            'collared',
            'seethru',
            'sweatermeat',
            'cfnm',
            'nsfwfashion',
            'leotards',
            'bikinis',
            'bikinibridge',
            'nsfwcosplay',
            'nsfwcostumes',
            'girlsinschooluniforms',
            'WtSSTaDaMiT',
            'tightdresses',
            'upskirt',
            'stockings',
            'thighhighs',
            'leggingsgonewild',
            'Bottomless_Vixens',
            'tightshorts',
            'girlsinyogapants',
            'yogapants',
            'lingerie',
            'assinthong',
            'AssholeBehindThong',
            ''
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #Pussy# 
    @commands.command(pass_context=True)
    async def pussy(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'pussy',
            'rearpussy',
            'innie',
            'simps',
            'pelfie',
            'LabiaGW',
            'godpussy',
            'presenting',
            'cameltoe',
            'hairypussy',
            'moundofvenus',
            'pussymound'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #THICC#
    @commands.command(pass_context=True)
    async def thicc(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'pawgtastic',
            'gonewildcurvy',
            'GoneWildplus',
            'indiansgonewild',
            'latinasgw',
            'pawg',
            'curvy',
            'thick',
            'juicyasians',
            'voluptuous',
            'biggerthanyouthought',
            'jigglefuck',
            'chubby',
            'SlimThick',
            'massivetitsnass',
            'thicker',
            'thickthighs',
            'tightsqueeze',
            'casualjiggles',
            'bbw'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #Thigh# 
    @commands.command(pass_context=True)
    async def thigh(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'girlsinyogapants',
            'stockings',
            'legs',
            'tightshorts',
            'datgap',
            'thighhighs',
            'thickthighs',
            'thighdeology'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #Trans# 
    @commands.command(pass_context=True)
    async def trans(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'Tgirls',
            'traps',
            'futanari',
            'gonewildtrans',
            'tgifs',
            'sissies'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")
 #Hentai# 
    @commands.command(pass_context=True)
    async def hentai(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'rule34',
            'ecchi',
            'futanari',
            'doujinshi',
            'yiff',
            'furry',
            'monstergirl',
            'rule34_comics',
            'sex_comics',
            'hentai',
            'hentai_gif',
            'WesternHentai',
            'hentai_irl',
            'overwatch_porn',
            'pokeporn',
            'bowsette',
            'rule34lol',
            'rule34overwatch'
            ])
            rand = random.randint(0, 59)  # 60 results generated per page
            items = grab.subreddit_gallery(subreddit =sub_rand)
            image = (items[rand].link)
            imagename = (items[rand].title)

            embed = discord.Embed(
                title = imagename,
                colour = discord.Colour.magenta()
                )
            embed.set_image(url=image)
            embed.add_field(name=':underage:',value='From : r/'+ sub_rand)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)
        else : 
            await ctx.send("You can't use that command here idiot! GO to a NSFW room!")

### Ethnic NSFW ###
 #Ethnicity Random#
    @commands.command(pass_context=True)
    async def ethnic(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'WomenOfColor',
            'damngoodinterracial',
            'gonewildcolor',
            'RepressedGoneWild',
            'ArabPorn',
            'SexyArabGirls',
            'MiddleEasternHotties',
            'EasternEuropeanGirls'
            'kpopfap',
            'NSFW_Korea',
            'NSFW_Japan',
            'javdownloadcenter',
            'juicyasians',
            'AsianNSFW',
            'AsianHotties',
            'asianfitgirls',
            'phgonewild'
            'darkangels',
            'blackchickswhitedicks',
            'ebony',
            'Afrodisiac',
            'ebonyamateurs',
            'PinkChocolate',
            'blackgirlpics',
            'strictlyafrican',
            'blackandbusty',
            'bigblackasses',
            'bigblackbootygifs',
            'ebonyasshole',
            'blackandpink',
            'blackgirlspinkpussy',
            'chocolatemilf',
            'bluebones',
            'sodomizedsoulsisters',
            'blacksluts',
            'EbonyBDSM',
            'latinas',
            'latinasgw',
            'latinacuties',
            'latinaporn',
            'Mexicana',
            'LatinaMilfs',
            'hotlatinas',
            'IndianBabes',
            'indiansgonewild',
            'DesiBoners',
            'IndianBabes',
            'IndianPorn',
            'IndianTeens',
            'IndianFetish',
            'indiangirls',
            'sosaree',
            'hqdesi'
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
 #Arab#
    @commands.command(pass_context=True)
    async def arab(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'RepressedGoneWild',
            'ArabPorn',
            'SexyArabGirls',
            'MiddleEasternHotties',
            'EasternEuropeanGirls'
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
 #Asian# 
    @commands.command(pass_context=True)
    async def asian(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'kpopfap',
            'NSFW_Korea',
            'NSFW_Japan',
            'javdownloadcenter',
            'juicyasians',
            'AsianNSFW',
            'AsianHotties',
            'asianfitgirls',
            'phgonewild'
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
 #Black#
    @commands.command(pass_context=True)
    async def black(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'darkangels',
            'blackchickswhitedicks',
            'ebony',
            'Afrodisiac',
            'ebonyamateurs',
            'PinkChocolate',
            'blackgirlpics',
            'strictlyafrican',
            'blackandbusty',
            'bigblackasses',
            'bigblackbootygifs',
            'ebonyasshole',
            'blackandpink',
            'blackgirlspinkpussy',
            'chocolatemilf'
            'bluebones',
            'sodomizedsoulsisters',
            'blacksluts',
            'EbonyBDSM'
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
 #Latino# 
    @commands.command(pass_context=True)
    async def latino(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'latinas',
            'latinasgw',
            'latinacuties',
            'latinaporn',
            'Mexicana',
            'LatinaMilfs',
            'hotlatinas'
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
 #Indian#
    @commands.command(pass_context=True)
    async def indian(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'IndianBabes',
            'indiansgonewild',
            'DesiBoners',
            'IndianBabes',
            'IndianPorn',
            'IndianTeens',
            'IndianFetish',
            'indiangirls',
            'sosaree',
            'hqdesi'
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
 #White#
    @commands.command(pass_context=True)
    async def white(self, ctx):
        if  ctx.channel.is_nsfw():
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            sub_rand = random.choice([
            'palegirls',
            'pawg',
            'snowwhites',
            'ginger',
            'redheads',
            'blonde'
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