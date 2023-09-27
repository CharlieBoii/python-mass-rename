import discord
import random
import time

words = open("/usr/share/dict/words").read().splitlines()

client = discord.Client(intents=discord.Intents.all())
bannedDudes = [] # Eg 091845323124 (User id)
async def change_nickname(member, nickname):
    if member.id in bannedDudes:
        return
    await member.edit(nick=nickname)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    while True:
        for member in client.get_all_members():
            print(member)
            await change_nickname(member, random.choice(words))
            time.sleep(0.5)


client.run('[Discord bot token]')
