with open('token.txt', 'r') as file:
    TOKEN = file.read().replace('\n', '')

import discord
import asyncio
from discord.ext import commands
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='%', intents=intents)

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
    await done.edit(content="We are done! Deleting this message in 1 seconds")
    await asyncio.sleep(1)
    await done.edit(content="We are done! Deleting this message now")
    await asyncio.sleep(1)
    await done.delete()


@bot.command()
async def poll(ctx, arg1: str, *args: str):
    role_ids = [1091406351550390295, 1091717942112166069]
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

@bot.command()
async def pollto(ctx, message: int, subcommand: str, *args: str):
    role_ids = [1091406351550390295, 1091717942112166069]
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

@bot.command()
async def cache(ctx):
    if ctx.author.id == 827176666320207872:
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
        await user.kick(reason=reason)
        if reason:
            await ctx.send(f"{user.mention} has been kicked for reason: {reason}")
        else:
            await ctx.send(f"{user.mention} has been kicked.")


@bot.command()
async def checkroles(ctx):
    if ctx.author.id == 827176666320207872:
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

@bot.command()
async def cmds(ctx):
    role_ids = [1091406351550390295, 1091717942112166069]
    banned_role = None
    for role_id in role_ids:
        banned_role = discord.utils.get(ctx.guild.roles, id=role_id)
        if banned_role:
            break
    if banned_role in ctx.author.roles:
        await ctx.send(f"{ctx.author.mention}, **You are banned from using this bot!**")
        return
    staff_id = 1053364516928364544
    staff_role = None
    staff_role = discord.utils.get(ctx.guild.roles, id=role_id)
    if staff_role in ctx.author.roles:
        await ctx.send(f"")
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
    if staff_role in ctx.author.roles:
        embed.add_field(name="%kick [member]", value="Kicks the specified member", inline=False)
        return
    await ctx.send(embed=embed)

bot.run(TOKEN)
