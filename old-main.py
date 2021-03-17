import discord
import os
import requests
import json
import time
import asyncio
import sys
import re
from replit import db
from keep_alive import keep_alive

client = discord.Client()

  #reg
#quotes #inspire
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -  " + json_data[0]['a']
    return (quote)

def get_app():
    response = requests.get("http://tech4help.org/random")
    json_data = json.loads(response.text)
    app = json_data[0]['q'] + " -  " + json_data[0]['a']
    return (app)


@client.event
async def on_ready():
    os.system('ruby startup.rb') #startup info

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )



@client.event
async def on_message(message):

    

    if message.content.startswith('>Help'):  #caps lock >commands
        await message.channel.send("Hi, Please click or tap the black spoiler box for you to type it:  ||>commands||")

        
        time.sleep(1)
        quote = get_quote()
        await message.channel.send('Your Quote: {}'.format(quote))

    if message.content.startswith('>inspire'):
        await message.channel.send(
            "Please Give Us 2 Seconds So We Can Generate Your Inspiring Quote! "
        )
        time.sleep(1)
        quote = get_quote()
        await message.channel.send('Your Quote: {}'.format(quote))

        #other
    if message.content.startswith('>commands'):
        embedVar = discord.Embed(
            title=">commands <:Owner:813476023416127529>",
            description="Shows All Of The >commands This Bot Has!",
            color=0x00ff00)
        embedVar.add_field(
            name=">commands",
            value=
            ">inspire >loading , >cmd >start7, , >start10/8 , >startxp ,>startvista , >invite , >start95 , >virus , >memz , >lol , >fail ,  >botname, >google, >senddata,>start1/2,>start3/3.1, >startnyan,>startcool,>bsod,, >avatar,>connectioninfo,>windows, >devs , >hack , >unhack",
            inline=False)
        embedVar.add_field(
            name="Advanced Commands",
            value=
            ">purge , >ban , >kick ",
            inline=False)
        embedVar.set_footer(text="Check out the repo! https://github.com/ThioTech/Discord.js and https://github.com/ThioTech/Discord.py")
        await message.channel.send(embed=embedVar)
        member = message.author
        channel = await member.create_dm()
        await channel.send('Thanks for using >commands!')
        time.sleep(1)


#cmd
    if message.content.startswith('>cmd'):
        await message.channel.send(
            "https://user-images.githubusercontent.com/7687556/105182045-dda1f700-5b2c-11eb-9f36-f98e39695503.gif"
        )
        
    if message.content.startswith('>devs'): 
        await message.channel.send("People that have developed this bot : Tech4Help , ThioTech ")


    if message.content.startswith('>hack'): 
        
        await message.channel.send("Hacking target's  Google account")
        time.sleep(1)
        await message.channel.send("Hacking target's  replit account")
        time.sleep(1)
        await message.channel.send("Hacking target's  Twitter account")
        time.sleep(1)
        await message.channel.send("Hacking target's  Facebook account")
        time.sleep(1)
        await message.channel.send("Successfully hacked. ")
        await message.channel.send("There has been unauthorized activity on your Google Account. Review this activity now.  ")
        time.sleep(2)
        await message.channel.send("There has been unauthorized activity on your Microsoft Account. Review this activity now.  ")
        await message.channel.send("Oh no! Microsoft AND Google's Recovery tools are not working. What will you do? ")
        await message.channel.send(">Hacking target's Discord account. ")
        await message.channel.send("Advertisement : auth : https://replit-auth.mobileworld.repl.co/ | Backend is hosted on our site , https://backend.mobileworld.repl.co/ . ")
        await message.channel.send("OMGG!! Am I causing spam? I must be dreaming. Tell me below. V")
        await message.channel.send(">hacking is needed!")
        
        
      
        
        
        
#loading
    if message.content.startswith('>loading'):
        await message.channel.send(
            "https://media1.tenor.com/images/7058defdfeb87905e1c47aafbded385e/tenor.gif?itemid=17209283"
        )
        if message.content.startswith('>unhack'):
          await message.channel.send(
            "Unhacking..."
        )
        if message.content.startswith('>loading'):
           await message.channel.send(
            "https://media1.tenor.com/images/7058defdfeb87905e1c47aafbded385e/tenor.gif?itemid=17209283"
        )
    if message.content.startswith('>Loading'):
        await message.channel.send(
            "https://media1.tenor.com/images/7058defdfeb87905e1c47aafbded385e/tenor.gif?itemid=17209283"
        )
#start7
    if message.content.startswith('>start7'):
        await message.channel.send(
            "https://thumbs.gfycat.com/FlimsyRewardingCorydorascatfish-mobile.mp4")

    if message.content.startswith('>Start7'):
        await message.channel.send(
            "https://thumbs.gfycat.com/FlimsyRewardingCorydorascatfish-mobile.mp4")
#start10/8
    if message.content.startswith('>start10/8'):
        await message.channel.send(
            "https://thumbs.gfycat.com/BothTanIbadanmalimbe-size_restricted.gif"
        )

    if message.content.startswith('>Start10/8'):
        await message.channel.send(
            "https://thumbs.gfycat.com /BothTanIbadanmalimbe-size_restricted.gif"
        ) 
#fail
    if message.content.startswith('>fail'):
        await message.channel.send(
            "https://tenor.com/view/erro-gif-20071624"
        )
        if message.content.startswith('>virus'):
          await message.channel.send(
            "https://tenor.com/view/windows98-memz-gif-9207842"
        )
       
        #startxp
    if message.content.startswith('>startxp'):
        await message.channel.send(
            "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/d1ebab8b-2b0b-4d87-a313-481d83d85afa/d9rjn08-805677ef-47a2-44a0-90e0-ef254f59085e.gif"
        )
#lol
    if message.content.startswith('>lol'):
        await message.channel.send(
            "https://tenor.com/view/microsoft-windows-windows-retro-screensaver-lol-gif-18222035"
        )
#startvista
    if message.content.startswith('>startvista'):
        await message.channel.send(
            "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/d1ebab8b-2b0b-4d87-a313-481d83d85afa/dd2oj50-6e909e0b-a743-4b35-b595-5a28b0a84196.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvZDFlYmFiOGItMmIwYi00ZDg3LWEzMTMtNDgxZDgzZDg1YWZhXC9kZDJvajUwLTZlOTA5ZTBiLWE3NDMtNGIzNS1iNTk1LTVhMjhiMGE4NDE5Ni5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.1KjP5lT4zS-njUc3C7wq4Ic8ohXI_QagXnKonQ_SFA0"
        )

#start95
    if message.content.startswith('>start95'):
        await message.channel.send(
            "https://tenor.com/view/microsoft-windows95-bill-gates-windows95vaporwave-start-up-gif-14688826"
        )

        #virus
    if message.content.startswith('>virus'):
        await message.channel.send(
            "https://tenor.com/view/windows-error-virus-alert-downloading-virus-shut-down-download-c plete-gif-16142328")
            
#memz
    if message.content.startswith('>memz'):
        await message.channel.send(
            "https://tenor.com/view/memz-gif-19511718 ")
            
#invite
    if message.content.startswith('>invite'):
        await message.channel.send(
            "Invite me to your server here : https://discord.com/api/oauth2/authorize?client_id=813229816278286346&permissions=2146958847&scope=bot"
        )
        #grabber 

#botname
    if message.content.startswith('>botname'):
        await message.channel.send('I Am {}'.format(client.user.name))
        print(message.author.id)
        print (message.author.name)
        print ("Used The Command!")

    if message.content.startswith('>senddata'):
        await message.channel.send('Hacking Your Account...')
        await message.channel.send('Hacked Successfully!')
        print('User Info:') 
        print('Name: {}'.format(message.author.name))
        print('ID: {}'.format(message.author.id))
        
    if message.content.startswith('>start1/2'):
        await message.channel.send('https://i.pinimg.com/originals/74/07/88/740788575335b4c7ce2b4fdd892690a5.gif')

    if message.content.startswith('>start3/3.1'):
        await message.channel.send('http://25.media.tumblr.com/tumblr_lpl4qm7lGp1qb42o2o1_250.gif')

    if message.content.startswith('>nyan'):
        await message.channel.send('https://media.tenor.com/images/0978d4618a630e35dbfda7f9d04098b1/tenor.gif')
       
    if message.content.startswith('>startcool'):
        await message.channel.send('https://tenor.com/view/windows-xp-gif-19794017')

    if message.content.startswith('>bsod'):
        await message.channel.send('https://tenor.com/view/bsod-error-windows-blue-screen-of-death-gif-8556865')

    if message.content.startswith('>avatar'):
        await message.channel.send('Here Is your avatar {}!'.format(message.author.name))
        UserProfilePicture = message.author.avatar_url 
        await message.channel.send(UserProfilePicture) #send av


    if message.content.startswith('>shutdown'):
        await message.channel.send('Shutting Down Code In 5 Seconds...')
        await asyncio.sleep(1)
        sys.exit()

    if message.content.startswith('>restart'):
        await message.channel.send('We Are Restarting.... (ETA: 5 Seconds)')
        await asyncio.sleep(5)
        await message.channel.send('Bot Restarted')
        await message.channel.send('Invoked By: {}'.format(message.author.name))
        member = message.author
        channel = await member.create_dm()
        await channel.send(quote)
        await message.channel.send('Hello')

    if message.content.startswith('>connectioninfo'):
        await message.channel.send('Please Wait While We Get The Latency ETA: 5 Seconds!')
        await asyncio.sleep(5)
        await message.channel.send(f'Latency: {client.latency}')
        await message.channel.send('Invoked By: {}'.format(message.author.name))

    if message.content.startswith('>windows'):
        await message.channel.send('https://giphy.com/gifs/hJaQNVrOPC4Ja')

    if message.content.startswith('>google'):
        await message.channel.send('https://tenor.com/view/google-gif-7538369') 

    if message.content.startswith('>info'):
        embedVar = discord.Embed(title="Bot Info", description="The Bot Info Like ID And Username Of The Bot!", color=0x00ff00)
        embedVar.add_field(name="Username:", value=('{} '.format(client.user.name)),inline=False)
        embedVar.add_field(name="ID:", value=('{} '.format(client.user.id)),inline=False)
        embedVar.set_footer(text='Command Invoked By: {} '.format(message.author.name))
        await message.channel.send(embed=embedVar)

    if message.content.startswith('>Info'):
        embedVar = discord.Embed(title="Bot Info", description="The Bot Info Like ID And Username Of The Bot!", color=0x00ff00)
        embedVar.add_field(name="Username:", value=('{} '.format(client.user.name)),inline=False)
        embedVar.add_field(name="ID:", value=('{} '.format(client.user.id)),inline=False)
        embedVar.set_footer(text='Command Invoked By: {} '.format(message.author.name))
        await message.channel.send(embed=embedVar)

      
        if message.content.startswith('>membercount'): 
          await message.channel.send(
            "Member Count:")
        await message.channel.send(message.guild.member_count) 



keep_alive()
token = os.environ.get("TOKEN")
client.run(token)
