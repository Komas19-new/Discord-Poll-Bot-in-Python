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


@bot.command()
async def poll(ctx, arg1: str, *args: str):
    if ctx.author.bot:
        print("Bot detected, tried !poll")
        return
    if arg1.lower() == 'number-10':
        print("executed !poll number-ten [text]")
        text = ' '.join(args)
        await ctx.message.delete()  # delete the original message
        embed = discord.Embed(title="Poll", description=text)
        poll_text = await ctx.send(embed=embed)  # send the poll text
        await poll_text.add_reaction("1️⃣")
        await poll_text.add_reaction("2️⃣")
        await poll_text.add_reaction("3️⃣")
        await poll_text.add_reaction("4️⃣")
        await poll_text.add_reaction("5️⃣")
        await poll_text.add_reaction("6️⃣")
        await poll_text.add_reaction("7️⃣")
        await poll_text.add_reaction("8️⃣")
        await poll_text.add_reaction("9️⃣")
        await poll_text.add_reaction("🔟")
        print("added all")
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
    elif arg1.lower() == 'number':
        print("executed !poll number [number] [text]")
        if len(args) < 2:
            await ctx.send("Invalid command format. Use '!poll number [num] [text]'")
            return
        try:
            num = int(args[0])
        except ValueError:
            await ctx.send("Invalid command format. Use '!poll number [num] [text]'")
            return
        if num < 1 or num > 9:
            await ctx.send("Invalid number, please choose a number between 1 and 9.")
            return
        text = ' '.join(args[1:])
        await ctx.message.delete()  # delete the original message
        embed = discord.Embed(title="Poll", description=text)
        poll_text = await ctx.send(embed=embed)  # send the poll text
        emojis = [f'{i}\N{combining enclosing keycap}' for i in range(1, num+1)]  # create the list of emojis
        for emoji in emojis:
            await poll_text.add_reaction(emoji)  # add the reactions to the poll message
            print("added one emoji")
        print("added all")
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
    elif arg1.lower() == 'regular':
        print("executed !poll regular [text]")
        if len(args) < 1:
            await ctx.send("Invalid command format. Use '!poll regular [text]'")
            return
        text = ' '.join(args)
        await ctx.message.delete()  # delete the original message
        embed = discord.Embed(title="Poll", description=text)
        poll_text = await ctx.send(embed=embed)  # send the poll text
        await poll_text.add_reaction('✅')  # add the checkmark reaction to the poll message
        await poll_text.add_reaction('🤷')  # add the don't know reaction to the poll message
        await poll_text.add_reaction('❌')  # add the x reaction to the poll message
        print("added reactions ✅🤷❌")
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
    else:
        await ctx.send("Invalid command format. Use !cmds for help.")

@bot.command()
async def pollto(ctx, message: int, subcommand: str, *args: str):
    if ctx.author.bot:
        print("Bot detected, tried !poll")
        return
    if subcommand.lower() == 'number-10':
        print("executed !pollto [message_id] number-10")
        await ctx.message.delete()  # delete the original message
        poll_message = await ctx.fetch_message(message)  # get the poll message
        await poll_message.add_reaction("1️⃣")
        await poll_message.add_reaction("2️⃣")
        await poll_message.add_reaction("3️⃣")
        await poll_message.add_reaction("4️⃣")
        await poll_message.add_reaction("5️⃣")
        await poll_message.add_reaction("6️⃣")
        await poll_message.add_reaction("7️⃣")
        await poll_message.add_reaction("8️⃣")
        await poll_message.add_reaction("9️⃣")
        await poll_message.add_reaction("🔟")
        print("added all")
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
    elif subcommand.lower() == 'number':
        print("executed !pollto [message_id] number [num]")
        if len(args) < 1:
            await ctx.send("Invalid command format. Use '!pollto [message_id] number [num]'")
            return
        try:
            num = int(args[0])
        except ValueError:
            await ctx.send("Invalid command format. Use '!pollto [message_id] number [num]'")
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
    elif subcommand.lower() == 'regular':
        print("executed !pollto [message_id] regular")
        await ctx.message.delete()  # delete the original message
        poll_message = await ctx.fetch_message(message)  # get the poll message
        await poll_message.add_reaction('✅')  # add the checkmark reaction to the poll message
        await poll_message.add_reaction('🤷')  # add the don't know reaction to the poll message
        await poll_message.add_reaction('❌')  # add the x reaction to the poll message
        print("added reactions ✅🤷❌")
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
    else:
        await ctx.send("Invalid command format. Use !cmds for help.")


@bot.command()
async def cmds(ctx):
    if ctx.author.bot:
        print("bot detected tried !cmds")
        return
    embed = discord.Embed(title="Commands", description="You can use all of these commands.", color=0x00ff00)
    embed.add_field(name="%poll number [num] [text]", value="Create a poll with a specified number of options from 1 to 9", inline=False)
    embed.add_field(name="%poll number-10 [text]", value="Create a poll with 10 options", inline=False)
    embed.add_field(name="%poll regular [text]", value="Create a poll with two options (yes/no)", inline=False)
    embed.add_field(name="%pollto [message_id] number [num]", value="Create a poll on a already existing message with a specified number of options", inline=False)
    embed.add_field(name="%pollto [message_id] number-10", value="Create a poll on a already existing message with 10 options", inline=False)
    embed.add_field(name="%pollto [message_id] regular", value="Create a poll on a already existing message with three options (yes/don't know/no)", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)
