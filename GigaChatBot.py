import discord
from discord.ext import commands, tasks
from itertools import cycle
import aiohttp
import random

TOKEN = 'ur discord bot token'

description = """GigaChatBot to super giga maszyna która przejmie kontrolę nad światem! buahahaha!"""

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())
bot.remove_command('help')
bot_status = cycle(['.help', 'Jebac Zielarza! hatfu!'])


@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(bot_status)))


@bot.event
async def on_ready():
    print(f'Bot {bot.user} dziala i ma sie dobrze :D')
    print('----------------')
    change_status.start()


# nie działa i mi się nie chce XD
"""@bot.event
async def on_raw_reaction_add(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, bot.guilds)
    print('err01')
    if payload.emoji.name == '😹' and payload.message_id == '1060718012338028576':
        print('err02.1')
        role = discord.utils.get(guild.roles, name='GigaChad')
        print('err02')
        if role is not None:
            print('err03')
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
    guild = discord.utils.find(lambda x: x.id == payload.guild_id, bot.guilds)

    if payload.emoji.name == '😹' and payload.message_id == '1060718012338028576':
        role = discord.utils.get(guild.roles, name='GigaChad')
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)


@bot.command()
async def react(ctx):
    message = 'Zostań GigaChadem jak ja!\nDawaj emotke szefie'
    react_message = await ctx.send(message)
    await react_message.add_reaction('😹')"""


@bot.command(aliases=['dog', 'pies', 'piesek'])
async def doggo(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/animal/dog')
        dog = await request.json()

    embed = discord.Embed(title='Aww... so cutee!', colour=discord.Colour.green())
    embed.set_image(url=dog['image'])
    embed.set_footer(text=dog['fact'])

    await ctx.send(embed=embed)


@bot.command(aliases=['lis', 'lisek'])
async def fox(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/animal/fox')
        lis = await request.json()

    embed = discord.Embed(title='Aww... so cutee!', colour=discord.Colour.green())
    embed.set_image(url=lis['image'])
    embed.set_footer(text=lis['fact'])

    await ctx.send(embed=embed)


@bot.command(aliases=['kitty', 'kot', 'kotek'])
async def cat(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/animal/cat')
        kitty = await request.json()

    embed = discord.Embed(title='Aww... so cutee!', colour=discord.Colour.green())
    embed.set_image(url=kitty['image'])
    embed.set_footer(text=kitty['fact'])

    await ctx.send(embed=embed)


@bot.command(aliases=['ptaszek', 'ptak'])
async def bird(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/animal/bird')
        ptak = await request.json()

    embed = discord.Embed(title='Aww... so cutee!', colour=discord.Colour.green())
    embed.set_image(url=ptak['image'])
    embed.set_footer(text=ptak['fact'])

    await ctx.send(embed=embed)


@bot.command(aliases=['RedPanda', 'najpiękniejszezwierzenaświecie'])
async def redpanda(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/animal/red_panda')
        rp = await request.json()

    embed = discord.Embed(title='Aww... so cutee!', colour=discord.Colour.green())
    embed.set_image(url=rp['image'])
    embed.set_footer(text=rp['fact'])

    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command(aliases=['pomoc', 'help'])
async def pomocy(ctx):
    with open('help.txt', 'r', encoding='utf-8') as f:
        file = f.read()

    await ctx.send(file)


@bot.command(aliases=['rps', 'kpn'])
async def rock_paper_scissors(ctx, usr_msg: str):
    usr_msg = usr_msg.lower()
    if usr_msg == 'kamień':
        usr_msg = 'kamien'
    elif usr_msg == 'nożyce':
        usr_msg = 'nozyce'

    opcje = ['papier', 'kamien', 'nozyce']
    losowanko = random.choice(opcje)

    if usr_msg == losowanko:
        await ctx.send(f'{losowanko.upper()}!\nAjaj, remis. Jeszcze raz?')
    elif usr_msg == 'kamien':
        if losowanko == 'papier':
            await ctx.send(f'{losowanko.upper()}!\nWygrałeeem! Nooob ahhahahahxXDDXDXdxD11!1!!!1')
        else:
            await ctx.send(f'{losowanko.upper()}!\nNieeee...! Pokonałeś mnie :CCCC')
    elif usr_msg == 'papier':
        if losowanko == 'nozyce':
            await ctx.send(f'{losowanko.upper()}!\nWygrałeeem! Nooob ahhahahahxXDDXDXdxD11!1!!!1')
        else:
            await ctx.send(f'{losowanko.upper()}!\nNieeee...! Pokonałeś mnie :CCCC')
    elif usr_msg == 'nozyce':
        if losowanko == 'kamien':
            await ctx.send(f'{losowanko.upper()}!\nWygrałeeem! Nooob ahhahahahxXDDXDXdxD11!1!!!1')
        else:
            await ctx.send(f'{losowanko.upper()}!\nNieeee...! Pokonałeś mnie :CCCC')
    else:
        await ctx.send('Umiesz pisać???')


@bot.command(aliases=['r'])
async def roll(ctx, throw: str):
    times, dice = map(int, throw.split('d'))
    if dice > 100:
        if times > 200:
            await ctx.send('Mam tylko 200 kości!\nA największa kostka to d100')
        else:
            await ctx.send('Największa kostka to d100!')
    elif times > 200:
        await ctx.send(f'Mam tylko 200 kostek d{dice}!')
    else:
        rolls = [random.randint(1, dice) for i in range(times)]
        odp = ''
        last_roll = rolls.pop(-1)
        try:
            for i in range(-1, times):
                odp += f'{str(rolls[i+1])}, '
        except Exception:
            odp += f'{last_roll}\nSuma wynosi: {sum(rolls) + last_roll}'

        rolls.append(last_roll)

        await ctx.send(odp)
        await ctx.send(f'Najwyższa wartość: {max(rolls)}')

@bot.command()
async def sus(ctx):
    await ctx.send('***Amogus***')


bot.run(TOKEN)
