import os
import random
import time
import discord

from keep_alive import keep_alive
client = discord.Client()
bot = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    @client.event
    async def on_message(message):
      if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')


token = os.environ.get("TOKEN")
client.run(token)
