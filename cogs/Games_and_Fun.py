import discord
import random
import asyncio
import requests
from discord.ext import commands
from discord import Game
from random import choice

####INSULTS##### add insults to a json file later

insults = [
    ("Yo Mama so dumb I told her Christmas was around the corner and she went looking for it."),
    ("You're so dumb it took you 2 hours to watch 60 minutes."),
    ("Yo Mama so dumb she bought tickets to Xbox Live."),
    ("You're so dumb that you thought The Exorcist was a workout video."),
    ("You're so ugly that you went to the salon and it took 3 hours just to get an estimate."),
    ("You're so ugly that even Scooby Doo couldn't solve that mystery."),
    ("What is the weighted center between Planet X and Planet Y? Oh it's YOU!"),
    (":eggplant: :eggplant: :eggplant:"),
    ("Your birth certificate is an apology letter from the condom factory."),
    ("I wasn't born with enough middle fingers to let you know how I feel about you."),
    ("You must have been born on a highway because that's where most accidents happen."),
    ("I'm jealous of all the people that haven't met you."),
    ("I bet your brain feels as good as new, seeing that you never use it."),
    ("I'm not saying I hate you, but I would unplug your life support to charge my phone."),
    ("You're so ugly, when your mom dropped you off at school she got a fine for littering."),
    ("You bring everyone a lot of joy, when you leave the room."),
    ("What's the difference between you and eggs? Eggs get laid and you don't."),
    ("You're as bright as a black hole, and twice as dense."),
    ("I tried to see things from your perspective, but I couldn't seem to shove my head that far up my ass."),
    ("Two wrongs don't make a right, take your parents as an example."),
    ("You're the reason the gene pool needs a lifeguard."),
    ("If laughter is the best medicine, your face must be curing the world."),
    ("You're so ugly, when you popped out the doctor said \"Aww what a treasure\" and your mom said \"Yeah, lets bury it.\""),
    ("I have neither the time nor the crayons to explain this to you."),
    ("You have two brains cells, one is lost and the other is out looking for it."),
    ("How many times do I have to flush to get rid of you?"),
    ("I don't exactly hate you, but if you were on fire and I had water, I'd drink it."),
    ("You shouldn't play hide and seek, no one would look for you."),
    ("Some drink from the fountain of knowledge; you only gargled."),
    ("Roses are red violets are blue, God made me pretty, what happened to you?"),
    ("It's better to let someone think you are an Idiot than to open your mouth and prove it."),
    ("Somewhere out there is a tree, tirelessly producing oxygen so you can breathe. I think you owe it an apology."),
    ("The last time I saw a face like yours I fed it a banana."),
    ("The only way you'll ever get laid is if you crawl up a chicken's ass and wait."),
    ("Which sexual position produces the ugliest children? Ask your mother."),
    ("If you really want to know about mistakes, you should ask your parents."),
    ("At least when I do a handstand my stomach doesn't hit me in the face."),
    ("If I gave you a penny for your thoughts, I'd get change."),
    ("If I were to slap you, it would be considered animal abuse."),
    ("Do you know how long it takes for your mother to take a crap? Nine months."),
    ("What are you going to do for a face when the baboon wants his butt back?"),
    ("Well I could agree with you, but then we'd both be wrong."),
    ("You're so fat, you could sell shade."),
    ("It looks like your face caught on fire and someone tried to put it out with a hammer."),
    ("You're not funny, but your life, now that's a joke."),
    ("You're so fat the only letters of the alphabet you know are KFC."),
    ("Oh my God, look at you. Was anyone else hurt in the accident?"),
    ("What are you doing here? Did someone leave your cage open?"),
    ("You're so ugly, the only dates you get are on a calendar."),
    ("I can explain it to you, but I can't understand it for you."),
    ("You are proof that God has a sense of humor."),
    ("If you spoke your mind, you'd be speechless."),
    ("Why don't you check eBay and see if they have a life for sale."),
    ("If I wanted to hear from an asshole, I'd fart."),
    ("You're so fat you need cheat codes to play Wii Fit"),
    ("You're so ugly, when you got robbed, the robbers made you wear their masks."),
    ("Do you still love nature, despite what it did to you?"),
    ("You are proof that evolution CAN go in reverse."),
    ("I'll never forget the first time we met, although I'll keep trying."),
    ("Your parents hated you so much your bath toys were an iron and a toaster"),
    ("Don't feel sad, don't feel blue, Frankenstein was ugly too."),
    ("You're so ugly, you scared the crap out of the toilet."),
    ("It's kinda sad watching you attempt to fit your entire vocabulary into a sentence."),
    ("I fart to make you smell better."),
    ("You're so ugly you make blind kids cry."),
    ("You're a person of rare intelligence. It's rare when you show any."),
    ("You're so fat, when you wear a yellow rain coat people scream ''taxi''."),
    ("I heard you went to a haunted house and they offered you a job."),
    ("You look like a before picture."),
    ("If your brain was made of chocolate, it wouldn't fill an M&M."),
    ("Aww, it's so cute when you try to talk about things you don't understand."),
    ("I heard your parents took you to a dog show and you won."),
    ("You stare at frozen juice cans because they say, \"concentrate\"."),
    ("You're so stupid you tried to wake a sleeping bag."),
    ("Am I getting smart with you? How would you know?"),
    ("We all sprang from apes, but you didn't spring far enough."),
    ("I'm no proctologist, but I know an asshole when I see one."),
    ("When was the last time you could see your whole body in the mirror?"),
    ("You must have a very low opinion of people if you think they are your equals."),
    ("So, a thought crossed your mind? Must have been a long and lonely journey."),
    ("You're the best at all you do - and all you do is make people hate you."),
    ("Looks like you fell off the ugly tree and hit every branch on the way down."),
    ("Looks aren't everything; in your case, they aren't anything."),
    ("You have enough fat to make another human."),
    ("You're so ugly, when you threw a boomerang it didn't come back."),
    ("You're so fat a picture of you would fall off the wall!"),
    ("Your hockey team made you goalie so you'd have to wear a mask."),
    ("Ordinarily people live and learn. You just live."),
    ("Did your parents ever ask you to run away from home?"),
    ("I heard you took an IQ test and they said your results were negative."),
    ("You're so ugly, you had tinted windows on your incubator."),
    ("Don't you need a license to be that ugly?"),
    ("I'm not saying you're fat, but it looks like you were poured into your clothes and someone forgot to say \"when\""),
    ("I've seen people like you, but I had to pay admission!"),
    ("I hear the only place you're ever invited is outside."),
    ("Keep talking, someday you'll say something intelligent!"),
    ("You couldn't pour water out of a boot if the instructions were on the heel."),
    ("Even if you were twice as smart, you'd still be stupid!"),
    ("You're so fat, you have to use a mattress as a maxi-pad."),
    ("I may be fat, but you're ugly, and I can lose weight."),
    ("I was pro life before I met you."),
    ("What's the difference between you and Hitler? Hitler knew when to kill himself."),
    ("You're so fat, your double chin has a double chin."),
    ("If ignorance is bliss, you must be the happiest person on earth."),
    ("You're so stupid, it takes you an hour to cook minute rice."),
    ("Is that your face? Or did your neck just throw up?"),
    ("You're so ugly you have to trick or treat over the phone."),
    ("I'd hit you but we don't hit girls around here."),
    ("Dumbass."),
    ("Bitch."),
    ("I'd give you a nasty look but you've already got one."),
    ("If I wanted a bitch, I'd have bought a dog."),
    ("Scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons."),
    ("Why is it acceptable for you to be an idiot but not for me to point it out?"),
    ("Did you know they used to be called \"Jumpolines\" until your mum jumped on one?"),
    ("You're not stupid; you just have bad luck when thinking."),
    ("I thought of you today. It reminded me to take the garbage out."),
    ("I'm sorry I didn't get that - I don't speak idiot."),
    ("Hey, your village called \u2013 they want their idiot back."),
    ("I just stepped in something that was smarter than you\u2026 and smelled better too."),
    ("If you were any less intelligent we'd have to water you three times a week.."),
    ("If your IQ was 3 points higher, you'd be a rock."),
    ("I would insult you but nature did a better job."),
    ("Does your ass get jealous of all the shit that comes out of your mouth?"),
    ("If I ate a bowl of alphabet soup, I could shit out a smarter sentence than any of yours."),
    ("You're not pretty enough to be this stupid."),
    ("That little voice in the back of your head, telling you you'll never be good enough? It's right."),
    ("You look like you're going to spend your life having one epiphany after another, always thinking you've finally figured out what's holding you back, and how you can finally be productive and creative and turn your life around. But nothing will ever change. That cycle of mediocrity isn't due to some obstacle. It's who you *are*. The thing standing in the way of your dreams is; that the person having them is *you*."),
    ("May your day and future be as pleasant as you are."),
    ("I would agree with you but then we would both be wrong."),
    ("I bite my thumb at you, sir."),
    ("I'd call you a tool, but that would imply you were useful in at least one way."),
    ("I hope you outlive your children."),
    ("Are you and your dick having a competition to see who can disappoint me the most?"),
    ("Yo mamma is so ugly her portraits hang themselves."),
    ("Your birth certificate is an apology from the abortion clinic."),
    ("If you were anymore inbred you'd be a sandwich."),
    ("Say hello to your wife and my kids for me."),
    ("You are thick-headed bastards with a bloated bureaucracy, designed to compensate for your small and poor self-esteem, cocksuckers. You have the brains to ban the person who has come to support channel your bot, accusing him of violating the ephemeral ephemeral rules, stupid morons. By the way i have one of the biggest server(5.5k  people, ~30 anytime voiceonline members), and i know something about managing, and of these rules - dont be an asshole. You are fucking asshole, maybe it is product of your life alone, or your life with your mom, anyway - you are retard and your soul is a fucking bunch of stupid self-esteems.")
]


class GameFunCog:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print('GameFunCog is Prepared')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(ctx.author.mention + " umm I think you typed the command wrong somewhere, check the help center")


#random dong length bot generator
    @commands.command()
    async def dong(self,ctx, user1: discord.Member):
        """Detects user's penis length"""
        async with ctx.typing():
            await asyncio.sleep(.01)

            if user1 is None:
                user1 = ctx.message.author

            avatar = ctx.message.author.avatar_url
    
            author = ctx.message.author

            length = ['=', '==', '===', '====', '=====', '======', '=======', '========']
            dong = "8" + (random.choice(length)) + "D"

            if user1.id == 398818242405072896 :
                embed = discord.Embed(
                    title="{}'s Dong Size".format(user1.name), 
                    description="Size: " + "8========D", 
                    colour=discord.Colour.blurple()
                    )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

                await ctx.send(embed=embed)
            
            else:
                embed = discord.Embed(
                    title="{}'s Dong Size".format(author.name), 
                    description="Size: " + dong, 
                    colour=discord.Colour.blurple()
                    )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

                await ctx.send(embed=embed)

#custom 8ball replier
    @commands.command()
    async def oicunt(self, ctx ,error , context):
        async with ctx.typing():
            await asyncio.sleep(.01)

            avatar = ctx.message.author.avatar_url
    
            author = ctx.message.author

            possible_responses = [
                    "As I see it, yes ",
                    "It is decidedly so ",
                    "Without a doubt ",
                    "Yes definitely ",
                    "You may rely on it ",
                    "As I see it yes ",
                    "Most likely ",
                    "She'll be right mate ",
                    "Yes ",
                    "You have a therapist for this ",
                    "I can’t be bothered answering that ",
                    "Ask again later ",
                    "Better not tell you now ",
                    "Get me a Maccas Burger and ask me again ",
                    "Concentrate and ask again ",
                    "Don't count on it ",
                    "My reply is no ",
                    "My sources say no ",
                    "I'm on the piss, gimme a few seconds and ask again ",
                    "Very doubtful ",
                    "I’ve heard just about enough out of you mate, you’d best pull your head in.",
                    "Hey, no one said I knew everything.",
                    "Ask again never ",
                    "Shut up you're drunk ",
                    "Ask ya mum ",
                    "Out of over 7 billion people on this planet, you decided to ask me? ",
                    "Without a doubt. Nah, I’m just messing with you, you’re definitely going to die alone. ",
                    "My sources say no. They also tell me they hate you and hope you burn in hell. ",
                    "Yes, definitely. Unless it doesn’t happen. Listen it’s not my fault your father didn’t love you. Get off my back! ",
                    "All signs point to yes. But on second thought, go fuck yourself. ",
                    "Take a wild guess...",
                    "Without a doubt",
                    "Might be possible",
                    "no... (╯°□°）╯︵ ┻━┻"
                    ]

            embed = discord.Embed(
                    title=(random.choice(possible_responses)),
                    colour=discord.Colour.blurple()
                    )
            embed.set_footer(icon_url= avatar, text='Replying to: ' + author.name)

            await ctx.send(embed=embed)

#uwu ship generator
    @commands.command()
    async def ship(self, ctx, user1: discord.Member, user2: discord.Member = None):
        async with ctx.typing():
            await asyncio.sleep(.01)

        if user2 is None:
            user2 = ctx.message.author

        if user1 is ctx.message.author and user2 is ctx.message.author:
            await ctx.send("Are you really that alone ?")
        
        else:
            avatar = ctx.message.author.avatar_url
            author = ctx.message.author

            score = random.randint(0, 100)
            filled_progbar = round(score / 100 * 10)
            empty_progbar = (10 - filled_progbar)
            counter_ = ('█' * filled_progbar) + ('░' * empty_progbar + '‍ ‍')

            if score < 30:
                message = "I don't know what to say about, they really don't seem to match..."
            elif score < 60:
                message = "Well... give it a shot but I wouldnt count on it working out"
            elif score < 80:
                message = "UWU ... what a Lovely Ship!"
            elif score > 80:
                message = "UWU!! strong candidate for ship of the year!"

            embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
            embed.set_author(name= "%s  ❤  %s" % (user1.name, user2.name,))
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name= message , value= (counter_) , inline=False)
            embed.add_field(name= score , value= 'Percent' , inline=False)

            await ctx.send(embed=embed)

#custom gay checker
    @commands.command()
    async def howgay(self, ctx, user1: discord.Member):
        async with ctx.typing():
            await asyncio.sleep(.01)

        if user1 is None:
            user1 = ctx.message.author

        avatar = ctx.message.author.avatar_url
        author = ctx.message.author

        score = random.randint(0, 100)
        filled_progbar = round(score / 100 * 10)
        empty_progbar = (10 - filled_progbar)
        counter_ = ('█' * filled_progbar) + ('░' * empty_progbar + '‍ ‍')

        if score < 30:
            message = "Aww shit looks like you aint gay, sad !"
        elif score < 60:
            message = "Huh....well you could be Bi, explore that!"
        elif score < 80:
            message = "Yeah you pretty gay mate! :gay_pride_flag: "
        elif score > 80:
            message = "Wow you so gay you probably fart glitter! :gay_pride_flag: "  

        embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
        embed.set_author(name= 'Gay R8 machine')
        embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
        embed.add_field(name= ':gay_pride_flag:  Score percentage: :gay_pride_flag: ' , value= score , inline=False)
        embed.add_field(name= '\u200b' , value= (counter_) , inline=False)
        embed.add_field(name= user1.name + ' ' + message , value= '\u200b' , inline=False)

        await ctx.send(embed=embed)

#coin flip fun ####FIX###########################################################################################
    @commands.command(pass_context=True)
    async def coinflip(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(.01)

        avatar = ctx.message.author.avatar_url
        author = ctx.message.author
        coinsides = ['Heads', 'Tails']
        result = random.choice(coinsides)

        embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
        embed.add_field(name= "I flipped a coin and got:" , text= result , inline=False)
        embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

        await ctx.send(embed=embed)
#####################################################################################################################

##insult command##

    @commands.command()
    async def insult(self, ctx, user1 : discord.Member):
        async with ctx.typing():
            await asyncio.sleep(.01)

        avatar = ctx.message.author.avatar_url
        author = ctx.message.author

        if user1.id == 513017390187937792: #if bot is mentioned
            user = ctx.message.author
            msg = [("How original. No one else had thought of trying to get the bot to insult itself. I applaud your creativity. Yawn. Perhaps this is why you don't have friends. You don't add anything new to any conversation. You are more of a bot than me, predictable answers, and absolutely dull to have an actual conversation with."), 
                    ("The fuck did ya just call me, cunt? I’ll have ya know I graduated top of me class at Sunshine TAFE, I’ve been involved in numerous beer skulling contests against Bob Hawke, and I have over 300 confirmed Cold Chisel albums. I am trained in vocal abuse towards umpires and I am the top snag eater in the entire city of Carlton. You are nothing to me but just another Collingwood fan. I will knock ya the fuck out with VB stubbies the likes of which have never been smashed before on this Earth, mark me fucken words. You reckon ya can get away with flapping ya beak to me over the Internet? Think again, cunt. As we speak I am contacting all me fucken lads across Western Sydney and ya IP is being traced right now so ya better prepare for the thunder, mate. The thunder that wipes out the pathetic little thing you call ya life. You’re fucking dead, prick. I can be anywhere, anytime, drinking anything, and I can glass you in over seven hundred ways, and that’s just with me smashed VB longneck. Not only am I extensively trained in smashing cunts, but I have access to the entire shed of cricket bats of the Melbourne Cricket Ground and I will use it to its full extent to hit ya for 6 and out, ya shitcunt. If only ya coulda known what bullshit your little “clever” backchat was about ta bring down upon ya, maybe ya woulda held your fucking tongue. But ya couldn’t, ya didn’t, and now you’re paying the price, mate. I will shit fury all over ya and you’re gonna drown in it, so ya better run, ya better take cover. You’re fucken dead, mate."),
                    ("I will shit prawn on the barbie all over you and you will drown in it, fair dinkum."),
                    ("Oi what the fuck cunt!"),
                    ("Scurry off cheeky bugger!"),
                    ("Oi yah flamin galah!"),
                    ("GO PUNCH CONES UNDER A BRIDGE OR SOMETHING YOU FUCKEN CUNT.")]
            
            message = choice(msg)
            embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name= user.name , value= message , inline=False)
            await ctx.send(embed=embed)


        elif user1.id == 398818242405072896: ##bot owner ## hehehe
            user = ctx.message.author
            msg = [("You dare insult my creator, ya furking cunt!"), 
                    ("Another cunt that wants to insult my creator, oi guys look we got a smart ass over here!"),
                    ("You dare insult my creator, I will shit prawn on the barbie all over you and you will drown in it, fair dinkum."),
                    ("Oi what the fuck cunt! Dont try insult my creator"),
                    ("Scurry off cheeky bugger!"),
                    ("Oi yah flamin galah!"),
                    ("GO PUNCH CONES UNDER A BRIDGE OR SOMETHING YOU FUCKEN CUNT.")]

            message = choice(msg)

            embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name= user.name , value= message , inline=False)
            await ctx.send(embed=embed)

        else:
            message = choice(insults)

            embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name= user1.name , value= message , inline=False)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(GameFunCog(client))
