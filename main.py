import os
import discord
import asyncio
import random
import json
import requests
import unicodedata
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
OWNER = os.getenv('OWNER')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='%', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print('Bot is ready.')
    await bot.change_presence(activity=discord.Game(name='with Polls'))

async def find_message(client, message_id):
    for guild in client.guilds:
        for channel in guild.text_channels:
            try:
                message = await channel.fetch_message(message_id)
                return message
            except discord.NotFound:
                pass
    return None

async def delete_message(ctx):
    done = await ctx.send("We are done! Deleting this message in 5 seconds")
    await asyncio.sleep(1)
    await done.edit(content="We are done! Deleting this message in 4 seconds")
    await asyncio.sleep(1)
    await done.edit(content="We are done! Deleting this message in 3 seconds")
    await asyncio.sleep(1)
    await done.edit(content="We are done! Deleting this message in 2 seconds")
    await asyncio.sleep(1)
    await done.edit(content="We are done! Deleting this message now")
    await asyncio.sleep(1)
    await done.delete()

async def get_emoji_from_unicode(unicode_sequence):
    emoji_name = unicodedata.name(unicode_sequence).lower().replace(' ', '_')
    emoji_sequence = f'\\N{{{emoji_name}}}'
    return emoji_sequence

@bot.command(aliases=['rs'])
async def roblox_status(ctx):
    response = requests.get("https://apis.roblox.com/maintenance-status/v1/alerts/alert-info")

    asset_info = json.loads(response.text)
    # Get the status code of the response
    status_code = response.status_code

    if status_code == 200:
        try:
            isVisible = asset_info['IsVisible']
            if isVisible == False:
                await ctx.send("The website banner is not visible, so there is no issues!")
            else:
                text = asset_info['Text']
                linkurl = asset_info['LinkUrl']
                await ctx.send(f"There is an issue in Roblox. Here is the details: \n Message from Roblox: {text} \n Link of the URL: {linkurl}")
        except KeyError as e:
            await ctx.send(f"An error has occurred. The key {e} does not exist.")
        except Exception as e:
            await ctx.send(f"An error has occured. {e}")

    else:
        await ctx.send(f"Error has occured. Error {status_code}")

@bot.command()
async def view_reactions(ctx):
    if ctx.author.id == OWNER:
        with open('reaction_roles.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print("opened reaction_roles.txt")
        print("reading it")
        print(lines)
        await ctx.send("Sent to console.")
        await ctx.send(f"```json\n{str(lines)}```")
    else:
        await ctx.send("You do not have permission to use this command.")
        
@bot.command(aliases=['add'])
@commands.has_permissions(manage_roles=True)
async def add_reaction(ctx, message_id, emoji, role: discord.Role):
    print("called add reaction command")
    message = await ctx.channel.fetch_message(int(message_id))
    await message.add_reaction(emoji)
    await ctx.send(f'Reaction {emoji} has been added to message {message_id}.')
    emoji_str = str(emoji).encode('unicode_escape').decode('utf-8')
    with open("reaction_roles.txt", "a", encoding="utf-8") as f:
        f.write(f'{message_id},{emoji_str},{role.id}\n')
        print("opened reaction_roles.txt")
        print("writing to it")
    print(role)
    
@bot.command()
async def trollip(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("Please mention a user to generate a troll IP address for.")
        return

    if not member.guild == ctx.guild:
        await ctx.send("That user is not in this server.")
        return

    number = random.randint(1, 255)
    number2 = random.randint(0, 255)
    number3 = random.randint(0, 255)
    number4 = random.randint(0, 255)

    await ctx.send(f"Troll IP of {member.mention} is {number}.{number2}.{number3}.{number4}")
    
@bot.command(aliases=['hg'])
async def how_gay(ctx, user: discord.User=None):
    number = random.randint(0, 100)
    if user is None:
        await ctx.send(f"You are {number}% gay!")
        return
    member = ctx.message.mentions[0]
    await ctx.send(f"{member.mention} is {number}% gay!")
    return

@bot.event
async def on_raw_reaction_add(payload):
    print("called reaction add")
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
    with open('reaction_roles.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print("opened reaction_roles.txt")
    print("reading it")
    for line in lines:
        line = line.strip().split(',')
        if payload.message_id == int(line[0]):
            print("message_id match")
            emoji = line[1]
            print(f'comparing {str(payload.emoji)} with {emoji}')
            if str(payload.emoji) == emoji:
                print("emoji match")
                role = discord.utils.get(guild.roles, id=int(line[2]))
                print(role)  # add this line
                if role is not None:
                    member = await guild.fetch_member(payload.user_id)
                    if member is not None:
                        try:
                            await member.add_roles(role)
                            print(f"{member} was given the {role} role")
                        except discord.Forbidden:
                            print(f"{bot.user} does not have permission to add roles to {member}")
                            channel = bot.get_channel(payload.channel_id)
                            await channel.send(f"Couldn't add role {role} to {member}, try moving the bot's role all the way up, and giving it the MANAGE_ROLE permission if it doesn't have it")

@bot.event
async def on_raw_reaction_add(payload):
    print("called reaction add")
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
    with open('reaction_roles.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print("opened reaction_roles.txt")
    print("reading it")
    for line in lines:
        line = line.strip().split(',')
        if payload.message_id == int(line[0]):
            print("message_id match")
            emoji = line[1]
            print(f'comparing {str(payload.emoji)} with {emoji}')
            if str(payload.emoji) == emoji:
                print("emoji match")
                role = discord.utils.get(guild.roles, id=int(line[2]))
                print(role)  # add this line
                if role is not None:
                    member = await guild.fetch_member(payload.user_id)
                    if member is not None:
                        try:
                            await member.remove_roles(role)
                            print(f"Removed {role} role from {member}")
                        except discord.Forbidden:
                            print(f"{bot.user} does not have permission to add roles to {member}")
                            channel = bot.get_channel(payload.channel_id)
                            await channel.send(f"Couldn't remove role {role} of {member}, try moving the bot's role all the way up, and giving it the MANAGE_ROLE permission if it doesn't have it")
                           
@bot.command(aliases=['p'])
async def poll(ctx, arg1: str, *args: str):
    role_ids = [ROLE, IDS, HERE]
    banned_role = None
    for role_id in role_ids:
        banned_role = discord.utils.get(ctx.guild.roles, id=role_id)
        if banned_role:
            break
    if banned_role in ctx.author.roles:
        await ctx.send(f"{ctx.author.mention}, **You are banned from using this bot!**")
        return
    if banned_role in ctx.author.roles:
        await ctx.send(f"{ctx.author.mention}, **You are banned from using this bot!**")
        return
    if ctx.author.bot:
        print("Bot detected, tried %poll")
        return
    if arg1.lower() == 'number-10':
        print("executed %poll number-ten [text]")
        text = ' '.join(args)
        await ctx.message.delete()  # delete the original message
        embed = discord.Embed(title="Poll", description=text)
        author = ctx.author.display_name + "#" + ctx.author.discriminator
        embed.set_author(name=author)
        poll_text = await ctx.send(embed=embed)  # send the poll text
        emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        for emoji in emojis:
            await poll_text.add_reaction(emoji)
        print("added all")
        delete_message(ctx)
    elif arg1.lower() == 'number':
        print("executed %poll number [number] [text]")
        if len(args) < 2:
            await ctx.send("Invalid command format. Use '%poll number [num] [text]'")
            return
        try:
            num = int(args[0])
        except ValueError:
            await ctx.send("Invalid command format. Use '%poll number [num] [text]'")
            return
        if num < 1 or num > 9:
            await ctx.send("Invalid number, please choose a number between 1 and 9.")
            return
        text = ' '.join(args[1:])
        await ctx.message.delete()  # delete the original message
        embed = discord.Embed(title="Poll", description=text)
        author = ctx.author.display_name + "#" + ctx.author.discriminator
        embed.set_author(name=author)
        poll_text = await ctx.send(embed=embed)  # send the poll text
        emojis = [f'{i}\N{combining enclosing keycap}' for i in range(1, num+1)]  # create the list of emojis
        for emoji in emojis:
            await poll_text.add_reaction(emoji)  # add the reactions to the poll message
            print("added one emoji")
        print("added all")
        await delete_message(ctx)
    elif arg1.lower() == 'regular':
        print("executed %poll regular [text]")
        if len(args) < 1:
            await ctx.send("Invalid command format. Use '%poll regular [text]'")
            return
        text = ' '.join(args)
        await ctx.message.delete()  # delete the original message
        embed = discord.Embed(title="Poll", description=text)
        author = ctx.author.display_name + "#" + ctx.author.discriminator
        embed.set_author(name=author)
        poll_text = await ctx.send(embed=embed)  # send the poll text
        emojis = ["✅", "🤷", "❌"]
        for emoji in emojis:
            await poll_text.add_reaction(emoji)
        print("added reactions ✅🤷❌")
        await delete_message(ctx)
    else:
        await ctx.send("Invalid command format. Use !cmds for help.")

@bot.command(aliases=['p2'])
async def pollto(ctx, message: int, subcommand: str, *args: str):
    role_ids = [ROLE, IDS, HERE]
    banned_role = None
    for role_id in role_ids:
        banned_role = discord.utils.get(ctx.guild.roles, id=role_id)
        if banned_role:
            break
    if banned_role in ctx.author.roles:
        await ctx.send(f"{ctx.author.mention}, **You are banned from using this bot!**")
        return
    if banned_role in ctx.author.roles:
        await ctx.send(f"{ctx.author.mention}, **You are banned from using this bot!**")
        return
    if ctx.author.bot:
        print("Bot detected, tried %poll")
        return
    if subcommand.lower() == 'number-10':
        print("executed %pollto [message_id] number-10")
        await ctx.message.delete()  # delete the original message
        poll_message = await ctx.fetch_message(message)  # get the poll message
        emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        for emoji in emojis:
            await poll_message.add_reaction(emoji)
        print("added all")
        await delete_message(ctx)
    elif subcommand.lower() == 'number':
        print("executed %pollto [message_id] number [num]")
        if len(args) < 1:
            await ctx.send("Invalid command format. Use '%pollto [message_id] number [num]'")
            return
        try:
            num = int(args[0])
        except ValueError:
            await ctx.send("Invalid command format. Use '%pollto [message_id] number [num]'")
            return
        if num < 1 or num > 9:
            await ctx.send("Invalid number, please choose a number between 1 and 9.")
            return
        await ctx.message.delete()  # delete the original message
        poll_message = await ctx.fetch_message(message)  # get the poll message
        emojis = [f'{i}\N{combining enclosing keycap}' for i in range(1, num+1)]  # create the list of emojis
        for emoji in emojis:
            await poll_message.add_reaction(emoji)  # add the reactions to the poll message
            print("added one emoji")
        print("added all")
        await delete_message(ctx)
    elif subcommand.lower() == 'regular':
        print("executed %pollto [message_id] regular")
        await ctx.message.delete()  # delete the original message
        poll_message = await ctx.fetch_message(message)  # get the poll message
        emojis = ["✅", "🤷", "❌"]
        for emoji in emojis:
            await poll_message.add_reaction(emoji)
        print("added reactions ✅🤷❌")
        await delete_message(ctx)

    else:
        await ctx.send("Invalid command format. Use %cmds for help.")

@bot.command(aliases=['c'])
async def cache(ctx):
    if ctx.author.id == OWNER:
        await ctx.send("Clearing cache...")
        bot.clear()
        await ctx.send("Cache cleared.")
        await ctx.send("Please restart the bot. Any command sent now will be broken.")
    else:
        await ctx.send("You do not have permission to use this command.")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason: str = None):
    if user == ctx.author:
        await ctx.send("You cannot kick yourself!")
    elif user == ctx.guild.me:
        await ctx.send("I cannot kick myself!")
    elif user.top_role >= ctx.author.top_role:
        await ctx.send("You cannot kick this user due to role hierarchy!")
    else:
        try:
            await user.send(f"You were kicked from {ctx.guild.name}" + (f" for reason: {reason}" if reason else ""))
            await ctx.send("Dmed the user successfully")
        except discord.Forbidden:
            await ctx.send("I couldn't dm the user to tell them they were kicked.")
        await user.kick(reason=reason)
        if reason:
            await ctx.send(f"{user.mention} has been kicked for reason: {reason}")
        else:
            await ctx.send(f"{user.mention} has been kicked.")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to use this command.")

@bot.event
async def on_message(message):
    messages = [
        "Fuck you!",
        "Frick you!",
        "You little shit!",
        "Actually, you suck!",
        "You are trash",
        "SHUT YO HALF AUTITISC",
        "LOOKING ASS OUT MY FACE",
        "KETCHUP SUPREME AND POURED HOT SAUCE ON YO FACE",
        ":gun:",
        "YOUR MOM IS FINGERBANING HER SELF TO HENRY DANGER",
        "BITCH",
        "dick sucker",
        "dick rider",
        "dickhead",
        "kys"
    ]
    if message.author == bot.user:
        return
    bad_words = ['bad', 'sucks', 'terrible', 'awful', 'suck', 'trash', 'shit', 'garbage', 'deleted', 'worst', 'shit', 'fuck','kys','horrible','noob']
    swear = random.choice(messages)
    pollbotstrings = "poll bot" in message.content.lower() or "pollbot" in message.content.lower() or bot.user.mentioned_in(message)
    if (pollbotstrings and any(word in message.content.lower() for word in bad_words)):
        await message.channel.send(f"{message.author.mention}, {swear}")
    if message.author == bot.user:
        return
    log_text = f"Server: {message.guild.name} ({message.guild.id}), Author: {message.author.name}#{message.author.discriminator}, Message: {message.content}, Channel: #{message.channel.name}"
    print(log_text)
    with open("message_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_text + "\n")
    await bot.process_commands(message)

@bot.command()
async def clearlogs(ctx):
    if ctx.author.id == OWNER:
        await ctx.send("Clearing message log file...")
        with open("message_log.txt", "w") as log_file:
            pass
        await ctx.send("Cleared.")
    else:
         await ctx.send("You do not have permission to use this command.")
    
@bot.command(aliases=['cr'])
async def checkroles(ctx):
    if ctx.author.id == OWNER:
        await ctx.send("Sending..")
        role_ids = [r.id for r in ctx.author.roles if r is not None]
        num_roles = len(role_ids)
        print(f"Number of roles: {num_roles}")
        print(f"Role IDs: {role_ids}")
        await ctx.send("Your roles have been sent to this bot's console. ({} Roles found)".format(num_roles))
    else:
        role_ids = [r.id for r in ctx.author.roles if r is not None]
        num_roles = len(role_ids)
        print(f"Number of roles: {num_roles}")
        print(f"Role IDs: {role_ids}")
        await ctx.send("You do not have permission to use this command. The roles are still sending to console. Which is {} roles".format(num_roles))

@bot.command(aliases=['help'])
async def cmds(ctx):
    role_ids = [ROLE, IDS, HERE]
    banned_role = None
    for role_id in role_ids:
        banned_role = discord.utils.get(ctx.guild.roles, id=role_id)
        if banned_role:
            break
    if banned_role in ctx.author.roles:
        await ctx.send(f"{ctx.author.mention}, **You are banned from using this bot!**")
        return
    if ctx.author.bot:
        print("bot detected tried %cmds")
        return
    embed = discord.Embed(title="Commands", description="You can use all of these commands.", color=0x00ff00)
    author = ctx.author.display_name + "#" + ctx.author.discriminator
    embed.set_author(name=author)
    embed.add_field(name="%poll number [num] [text]", value="Create a poll with a specified number of options from 1 to 9", inline=False)
    embed.add_field(name="%poll number-10 [text]", value="Create a poll with 10 options", inline=False)
    embed.add_field(name="%poll regular [text]", value="Create a poll with two options (yes/no)", inline=False)
    embed.add_field(name="%pollto [message_id] number [num]", value="Create a poll on a already existing message with a specified number of options", inline=False)
    embed.add_field(name="%pollto [message_id] number-10", value="Create a poll on a already existing message with 10 options", inline=False)
    embed.add_field(name="%pollto [message_id] regular", value="Create a poll on a already existing message with three options (yes/don't know/no)", inline=False)
    embed.add_field(name="%kick [member]", value="Kicks the specified member", inline=False)
    embed.add_field(name="%cmds", value="Shows this.", inline=False)
    embed.add_field(name="%help", value="Shows this.",inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=['komas19'])
async def owner(ctx):
    if ctx.author.id == OWNER:
        embed = discord.Embed(title="Commands", description="You can use all of these commands.", color=0x00ff00)
        author = ctx.author.display_name + "#" + ctx.author.discriminator
        embed.set_author(name=author)
        embed.add_field(name="%cache", value="Clears the cache of the bot",inline=False)
        embed.add_field(name="%checkroles", value="Checks the roles",inline=False)
        embed.add_field(name="%owner", value="Shows this",inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("You do not have permission to use this command.")

bot.run(TOKEN)
