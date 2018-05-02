import discord
import datetime
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time


Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Connected to Discord API.")
    print("Connected to " + client.user.name + " client.")
    print("User ID: " + client.user.id + ".")
    await client.change_presence(game=discord.Game(name="!help"), status=discord.Status.dnd, afk=False)

#lfg autoroles

    if message.content.upper() == '<@391023589463162880> SPAWNALL':
        if isadminrole(message.author.roles, adminroleidlist):
            await client.delete_message(message)
            await client.send_message(message.channel, "**_Looking For Group (LFG) Roles._**")
            await asyncio.sleep(1)
            await client.send_message(message.channel, "!spawnxbox")
            await asyncio.sleep(1)
            await client.send_message(message.channel, "!spawnpc")
            await asyncio.sleep(1)
            await client.send_message(message.channel, "!spawnps4")

    if message.content.upper() == '!SPAWNXBOX' and message.author.id == dobbyuserid:
        roleEmbed = makeroleembed("Xbox")
        roleEmbed.set_thumbnail(url="https://cdn2.iconfinder.com/data/icons/metro-uinvert-dock/256/XBox_360.png")
        await client.delete_message(message)
        msg = await client.send_message(message.channel, embed=roleEmbed)
        await client.add_reaction(msg, discord.utils.get(client.get_all_emojis(), id='388402362735394828'))
        await asyncio.sleep(2)
        await client.add_reaction(msg, discord.utils.get(client.get_all_emojis(), id='388402335501647875'))
        await asyncio.sleep(2)
        while True:
            res = await client.wait_for_reaction([discord.utils.get(client.get_all_emojis(), id='388402362735394828'),
                                                 discord.utils.get(client.get_all_emojis(), id='388402335501647875')],
                                                 message=msg)
            if res.reaction.emoji == discord.utils.get(client.get_all_emojis(), id='388402362735394828'):
                await client.remove_reaction(msg, discord.utils.get(client.get_all_emojis(), id='388402362735394828'),
                                             res.user)  #removes the useradded join pvp reaction
                await asyncio.sleep(0.1)
                await client.add_roles(res.user, get_role(msg.server.roles, "Xbox"))
                await asyncio.sleep(0.1)
                await client.send_message(res.user, "Added **Xbox** <:check:388402362735394828>")
            if res.reaction.emoji == discord.utils.get(client.get_all_emojis(), id='388402335501647875'):
                await client.remove_reaction(msg, discord.utils.get(client.get_all_emojis(), id='388402335501647875'),
                                             res.user)  #removes the useradded join pvp reaction
                await asyncio.sleep(0.1)
                await client.remove_roles(res.user, get_role(msg.server.roles, "Xbox"))
                await asyncio.sleep(0.1)
                await client.send_message(res.user, "Removed **Xbox** <:xmark:388402335501647875>")
    if message.content.upper() == '!SPAWNPC' and message.author.id == dobbyuserid:
        roleEmbed = makeroleembed("PC")
        roleEmbed.set_thumbnail(url="http://upload2.inven.co.kr/upload/2016/12/28/per/i13407358112.png")
        await client.delete_message(message)
        msg = await client.send_message(message.channel, embed=roleEmbed)
        await client.add_reaction(msg, emoji=discord.utils.get(client.get_all_emojis(), id='388402362735394828'))
        await asyncio.sleep(2)
        await client.add_reaction(msg, discord.utils.get(client.get_all_emojis(), id='388402335501647875'))
        await asyncio.sleep(2)
        while True:
            res = await client.wait_for_reaction([discord.utils.get(client.get_all_emojis(), id='388402362735394828'),
                                                 discord.utils.get(client.get_all_emojis(), id='388402335501647875')],
                                                 message=msg)
            if res.reaction.emoji == discord.utils.get(client.get_all_emojis(), id='388402362735394828'):
                await client.remove_reaction(msg, discord.utils.get(client.get_all_emojis(), id='388402362735394828'),
                                             res.user)  #removes the useradded join pvp reaction
                await asyncio.sleep(0.1)
                await client.add_roles(res.user, get_role(msg.server.roles, "PC"))
                await asyncio.sleep(0.1)
                await client.send_message(res.user, "Added **PC** <:check:388402362735394828>")
            if res.reaction.emoji == discord.utils.get(client.get_all_emojis(), id='388402335501647875'):
                await client.remove_reaction(msg, discord.utils.get(client.get_all_emojis(), id='388402335501647875'),
                                             res.user)  #removes the useradded join pvp reaction
                await asyncio.sleep(0.1)
                await client.remove_roles(res.user, get_role(msg.server.roles, "PC"))
                await asyncio.sleep(0.1)
                await client.send_message(res.user, "Removed **PC** <:xmark:388402335501647875>")
    if message.content.upper() == '!SPAWNPS4' and message.author.id == dobbyuserid:
        roleEmbed = makeroleembed("PS4")
        roleEmbed.set_thumbnail(url="http://pluspng.com/img-png/playstation-png-png-file-name-playstation-512.png")
        await client.delete_message(message)
        msg = await client.send_message(message.channel, embed=roleEmbed)
        await client.add_reaction(msg, discord.utils.get(client.get_all_emojis(), id='388402362735394828'))
        await asyncio.sleep(2)
        await client.add_reaction(msg, discord.utils.get(client.get_all_emojis(), id='388402335501647875'))
        await asyncio.sleep(2)
        while True:
            res = await client.wait_for_reaction([discord.utils.get(client.get_all_emojis(), id='388402362735394828'),
                                                 discord.utils.get(client.get_all_emojis(), id='388402335501647875')],
                                                 message=msg)
            if res.reaction.emoji == discord.utils.get(client.get_all_emojis(), id='388402362735394828'):
                await client.remove_reaction(msg, discord.utils.get(client.get_all_emojis(), id='388402362735394828'),
                                             res.user)  #removes the useradded join pvp reaction
                await asyncio.sleep(0.1)
                await client.add_roles(res.user, get_role(msg.server.roles, "Playstation"))
                await asyncio.sleep(0.1)
                await client.send_message(res.user, "Added *Playstation** <:check:388402362735394828>")
            if res.reaction.emoji == discord.utils.get(client.get_all_emojis(), id='388402335501647875'):
                await client.remove_reaction(msg, discord.utils.get(client.get_all_emojis(), id='388402335501647875'),
                                             res.user)  #removes the useradded join pvp reaction
                await asyncio.sleep(0.1)
                await client.remove_roles(res.user, get_role(msg.server.roles, "Playstation"))
                await asyncio.sleep(0.1)
                await client.send_message(res.user, "Removed **Playstation** <:xmark:388402335501647875>")

#token

client.run("")
