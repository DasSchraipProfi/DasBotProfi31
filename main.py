from typing import Optional

import discord
from discord.ext import commands, tasks
from discord import app_commands
from discord.utils import get
from discord.ui import View, Button
from itertools import cycle
from discord.ui import Button, View
from googletrans import Translator
intents = discord.Intents.all()
intents.members = True

import datetime

import webcolors

import requests

import inspect

import os

import sqlite3

import pytz

bot_token = 'MTEyNDM4MjkxOTk5NDExODIzNw.GQJqwQ.Z9p-JzhDPKwxo5jU6pM8z7dQ954-KEQb_voUNE'

client = commands.Bot(command_prefix='?', intents=intents)



@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

bot_status = cycle(["Leon ärgern","Clash of Clans","sich an der Nudel","ping me for help", "sich in deinen Account hacken", "die Weltherrschaft an sich reißen", "EARLY ACCESS"])


channel_id = 1134573970268626996


@client.event
async def on_ready():
    print("Verbindung steht: DasBotProfi is back in da hood!")
    print("SERVER:")
    for guild in client.guilds:
        print(f'- {guild.name} (ID: {guild.id})')
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    print(datetime.date.today().strftime("%d.%m.%Y"))
    change_status.start()
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send(':wave:Hey Chef, ich bin wieder online!:white_check_mark:')
    # Präfix aus der Datenbank nach dem Bot-Neustart abrufen und setzen
    for guild in client.guilds:
        cursor.execute('SELECT prefix FROM prefixes WHERE guild_id = ?', (guild.id,))
        result = cursor.fetchone()
        if result:
            guild_prefix = result[0]
            client.command_prefix = get_custom_prefix
            break


import asyncio

import random

#----------ping command----------

@client.command()
async def ping(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title=f"<a:laden:1134179627481432245> Finde Latenz heraus...<a:laden:1134179627481432245>", description=f"<a:loading:1134644133676449923>", color=discord.Color.blurple())
  message = await ctx.send(embed=embed)
  await asyncio.sleep(5)
  if message.embeds:
      embed = message.embeds[0]
      new_description = f":writing_hand:Verfasse Nachricht an Server."
      embed.description = new_description
      await message.edit(embed=embed)
      await asyncio.sleep(5)
      if message.embeds:
          embed = message.embeds[0]
          new_description = f"📲Sende Nachricht an Server"
          embed.description = new_description
          await message.edit(embed=embed)
          await asyncio.sleep(5)
          if message.embeds:
              embed = message.embeds[0]
              new_description = f":white_check_mark:Server hat Nachricht erhalten."
              embed.description = new_description
              await message.edit(embed=embed)
              await asyncio.sleep(5)
              if message.embeds:
                  embed = message.embeds[0]
                  new_description = f"<a:laden:1134179627481432245>Server verarbeitet die Nachricht."
                  embed.description = new_description
                  await message.edit(embed=embed)
                  await asyncio.sleep(5)
                  if message.embeds:
                      embed = message.embeds[0]
                      new_description = f":globe_with_meridians:Sende Antwort an den Bot zurück"
                      embed.description = new_description
                      await message.edit(embed=embed)
                      await asyncio.sleep(5)
                      if message.embeds:
                          embed = message.embeds[0]
                          new_description = f":white_check_mark:Bot hat Antwort erhalten, werte Latenz aus."
                          embed.description = new_description
                          await message.edit(embed=embed)
                          await asyncio.sleep(5)
                          if message.embeds:
                              embed = message.embeds[0]
                              new_title = f":exclamation:Latenz herausgefunden:exclamation:"
                              embed.title = new_title
                              new_description = f":ping_pong:Pong! Hier meine Latenz: {round(client.latency * 1000)}ms.\n:thinking:Deswegen bin ich also so langsam..."
                              embed.description = new_description
                              await message.edit(embed=embed)




#----------Voice commands----------
@client.command()
async def mute(ctx, member: discord.Member):
  await ctx.message.delete()
  if ctx.author.guild_permissions.mute_members:
    await member.edit(mute=True)
    await ctx.send(f'{member.mention} wurde gemuted.')
  else:
    await ctx.send(f':x:Fresse, das darfst du garnicht:exclamation:')

@client.command()
async def unmute(ctx, member: discord.Member):
  await ctx.message.delete()
  if ctx.author.guild_permissions.mute_members:
    await member.edit(mute=False)
    await ctx.send(f'{member.mention} ist nicht mehr gemuted :D!')
  else:
    await ctx.send(':x:Maul halten, denn das kannst du gar nicht machen:exclamation:')

#----------User timeouten----------

@client.command()
async def timeout(ctx, member: discord.Member, duration: int):
    await ctx.message.delete()
    if ctx.author.guild_permissions.manage_roles:
        seconds = duration * 60
        timeout_role = discord.utils.get(ctx.guild.roles, name = 'Timeout')
        if not timeout_role:
            timeout_role = await ctx.guild.create_role(name='Timeout')
            for channel in ctx.guild.channels:
                await channel.set_permissions(timeout_role, send_messages=False)
        await member.edit(roles=[])
        await member.add_roles(timeout_role)
        await ctx.send(f'{member.mention} wurde für {duration} Minuten bzw. {seconds} Sekunden auf die stille Treppe verfrachtet')
        await asyncio.sleep(seconds)
        await member.remove_roles(timeout_role)
        await ctx.send(f'{member.mention} darf wieder teilnehmen.\nDenke dran, ihm wieder seine Rollen zu geben!')
    else:
      await ctx.send('Finger weg! Du darfst das gar nicht')

#----------Rollen commands----------

@client.command()
async def addrole(ctx, member: discord.Member, *roles: discord.Role):
 await ctx.message.delete()
 if ctx.author.guild_permissions.manage_roles:
       await member.add_roles(*roles)
       async with ctx.typing():
           await asyncio.sleep(3)
       await ctx.send(':white_check_mark:Haben fertig!')
 else:
     await ctx.send('Ruhe auf den billigen Plätzen!:angry:')


@client.command()
async def removerole(ctx, member: discord.Member, *roles: discord.Role):
 await ctx.message.delete()
 if ctx.author.guild_permissions.manage_roles:
       await member.remove_roles(*roles)
       async with ctx.typing():
           await asyncio.sleep(3)
       await ctx.send(':white_check_mark:Haben fertig!')
 else:
     await ctx.send('Ruhe auf den billigen Plätzen!:angry:')

#----------User kicken----------

@client.command()
async def kick(ctx, member: discord.Member):
  await ctx.message.delete()
  if ctx.author.guild_permissions.kick_members:
    await member.kick()
    await ctx.send(f'## Tja....das haste nun davon {member.mention}. Du wurdest gekickt. ##')
    embed = discord.Embed(title=f"__{ctx.guild.name}__", color=discord.Color.red())
    embed.add_field(name=f"⚠️Du wurdest vom Server gekickt", value=f"An deiner Stelle würde ich mal mein Benehmen hinterfragen", inline=False)
    await member.send(embed=embed)
  else:
    await ctx.send('Willste auch nen Kick, weil du etwas machen willst was du garnicht darfst?')

#----------würfeln----------

@client.command()
async def würfeln(ctx, sides: int = 6):
  await ctx.message.delete()
  async with ctx.typing():
      await asyncio.sleep(5)
  await ctx.send(':game_die:Zinke die Würfel...', delete_after=5)
  async with ctx.typing():
      await asyncio.sleep(5)
  await ctx.send(':repeat:Würfele die Würfel...', delete_after=5)
  async with ctx.typing():
      await asyncio.sleep(5)
  if sides < 2:
    await ctx.send('Die Anzahl der Seiten muss mindestens 2 sein')
    return

  result = random.randint(1, sides)
  await ctx.send(f':game_die:Du hast eine {result} mit einem {sides} seitigem Würfel gewürfelt :D')

#----------unnütze scheiße----------

@client.command()
async def leonsz(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member !=client.user:
      await member.kick()
  await ctx.send('Selbstzerstörung wurde eingeleitet.')

@client.command()
async def wiederhole(ctx, message: str, times: int = 1):
  await ctx.message.delete()
  if times < 1:
    await ctx.send('Die Zahl muss größer als 1 sein!')
    return

  for _ in range(times):
      await ctx.send(message)

#----------Nachrichten löschen----------

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int):
  await ctx.message.delete()
  await ctx.channel.purge(limit=limit)
  async with ctx.typing():
      await asyncio.sleep(5)
  message = ':white_check_mark:Ich habe fertig{}!'.format(ctx.author.mention)
  await ctx.send(message, delete_after=5)
  await asyncio.sleep(5)
  async with ctx.typing():
      await asyncio.sleep(5)
  embed = discord.Embed(title=f'<:dereinzigwahreerklrbr:1122186264381235274>Kann ich sonst noch was tun?\n:arrow_right:**?menü**', color=discord.Color.green())
  await ctx.send(embed=embed)

#----------Meine user id----------
user_id = 397820734002429953

#----------Blackjack----------

# Define the ranks and suits for the cards
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♠', '♣', '♥', '♦']

# Function to deal a card
def deal_card():
    rank = random.choice(RANKS)
    suit = random.choice(SUITS)
    return f'{rank}{suit}'

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        rank = card[:-1]
        if rank.isdigit():
            value += int(rank)
        elif rank in ['J', 'Q', 'K']:
            value += 10
        else:  # Ace
            value += 11
            num_aces += 1
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value


# Command to start a Blackjack game
@client.command(name='blackjack', help='Start a game of Blackjack.')
async def blackjack(ctx):
    await ctx.message.delete()
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)

    async with ctx.typing():
        await asyncio.sleep(3)
    await ctx.send('# <a:laden:1134179627481432245>Starte eine Runde Blackjack<a:laden:1134179627481432245> #',
                   delete_after=5)
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send(':repeat:Mische die Karten gut durch', delete_after=5)
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send(':leftwards_hand:Teile Karten aus', delete_after=5)
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send(f':person_bowing:Spieler: {", ".join(player_hand)} (Summe: {player_score})')
    await ctx.send(f':robot:Dealer: {dealer_hand[0]}, ?? (Summe: ?) ')

    while True:
        await ctx.send('**:thinking:Willst du noch eine Karte? (h/s)**\n:information_source:h=hit | s=stay')

        def check(m):
            return m.author == ctx.author and m.content.lower() in ['h', 's']

        reply = await client.wait_for('message', check=check)
        choice = reply.content.lower()

        if choice == 'h':
            new_card = deal_card()
            player_hand.append(new_card)
            player_score = calculate_hand_value(player_hand)
            await ctx.send(f':white_check_mark:Du ziehst: {new_card} (Summe: {player_score})')
            if player_score > 21:
                await ctx.send('**:x:Zu viel! Du hast verloren.**')
                break
        elif choice == 's':
            while dealer_score < 17:
                new_card = deal_card()
                dealer_hand.append(new_card)
                dealer_score = calculate_hand_value(dealer_hand)
            await ctx.send(f'Dealer: {", ".join(dealer_hand)} (Summe: {dealer_score})')

            if dealer_score > 21 or dealer_score < player_score:
                await ctx.send('**:partying_face:Glückwunsch! Du hast gewonnen.**')
            elif dealer_score > player_score:
                await ctx.send('**:no_mouth:Blöd gelaufen. Du hast verloren!**')
            else:
                await ctx.send('**:crossed_swords:Unentschieden! Versuchs einfach nochmal:smiling_face_with_tear:**')
            break
        else:
            await ctx.send(
                ':x:Unfültige Eingabe! Schreibe "h" um eine Karte zu ziehen oder "s" um keine Karte mehr zu ziehen:exclamation:')


#----------Serverinfo----------

@client.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    await ctx.send(f'<a:laden:1134179627481432245>', delete_after=10)
    async with ctx.typing():
        await asyncio.sleep(10)
    guild = ctx.guild
    embed = discord.Embed(title=f":information_source:Serverinformationen - {guild.name}:information_source:", color=discord.Color.blurple())
    embed.add_field(name="<:rank:1134854413186510889>Server Name", value=guild.name, inline=False)
    embed.add_field(name="<:nitro:1134854539024011275>Server ID", value=guild.id, inline=False)
    embed.add_field(name="<:discord:1134854925331992686>Erstellt am", value=guild.created_at.strftime("%d.%m.%Y %H:%M:%S"), inline=False)
    embed.add_field(name="<:king:1134854733589401721>Besitzer", value=guild.owner, inline=False)
    embed.add_field(name="<:guard:1134854610562072636>Mitglieder", value=guild.member_count, inline=False)
    embed.add_field(name="<:chat:1134854815458017350>Anzahl der Textkanäle", value=len(guild.text_channels), inline=False)
    embed.add_field(name=":speaker:Anzahl der Sprachkanäle", value=len(guild.voice_channels), inline=False)
    embed.set_thumbnail(url=ctx.guild.icon)
    await ctx.send(embed=embed)
    await ctx.send(':white_check_mark:', delete_after=5)

#----------Userinfo----------

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    await ctx.message.delete()
    member = member or ctx.author

    embed = discord.Embed(title=f":information_source:Benutzerinfo - {member.display_name}:information_source:", color=member.color)
    embed.add_field(name=":name_badge:Name", value=member.name, inline=True)
    embed.add_field(name=":id:ID", value=member.id, inline=False)
    embed.add_field(name=":shield:Status", value=member.status, inline=False)
    embed.add_field(name=":video_game:Spiele", value=member.activity.name if member.activity else "Nichts", inline=True)
    embed.add_field(name="<:time:1137145223550607420>Beigetreten am", value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"), inline=False)
    embed.add_field(name="<:emoji_3:1120084892596846662>Account erstellt am", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"), inline=False)
    embed.set_thumbnail(url=member.display_avatar)
    embed.set_footer(text=f"Angefragt von {ctx.author.name}")
    await ctx.send('<a:laden:1134179627481432245>', delete_after=10)
    async with ctx.typing():
        await asyncio.sleep(10)
    await ctx.send(embed=embed)
    await ctx.send(':white_check_mark:', delete_after=5)

#----------BotInfo----------

@client.command()
async def botinfo(ctx):
    await ctx.message.delete()
    await ctx.send('# <a:laden:1134179627481432245>Lade alle Daten<a:laden:1134179627481432245> #',delete_after=20)
    async with ctx.typing():
        await asyncio.sleep(20)
    embed=discord.Embed(title=':information_source:Informationen über DasBotProfi:information_source:', color=discord.Color.dark_gold())
    embed.add_field(name=':mechanical_arm:Ich bin auf Discord seit dem:', value='30.06.2023', inline=False)
    embed.add_field(name=':lock_with_ink_pen:Mein Schöpfer:', value='dasschraipprofi', inline=False)
    num_commands = len(client.commands)
    embed.add_field(name=f"<:dev:1134854678950183062>Anzahl der Commands, welche ich unterstütze:", value=f"Insgesamt {num_commands} Commands", inline=False)
    total_lines = 0

    for filename in os.listdir('.'):
        if filename.endswith('.py'):
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                total_lines += len(lines)
    embed.add_field(name=f"🗂Anzahl der Codezeilen, die ich beinhalte:", value=f"{total_lines} Zeilen Code", inline=False)
    embed.add_field(name=':bookmark:Ich soll auch auf deinem Server rumgeistern?', value=f"[Dann lade mich ein!](https://discord.com/api/oauth2/authorize?client_id=1124382919994118237&permissions=8&scope=bot)", inline=False)
    embed.add_field(name='<:server2:1134854334845292554>Ich bin aktiv auf folgenden Servern:', value='', inline=False)
    for guild in client.guilds:
        embed.add_field(name='<:partner:1134854865403793469>', value=f'- {guild.name} (ID: {guild.id})')
    embed.set_footer(text="Füge mich gerne deinem Server hinzu. Link siehe mein Profil")
    await ctx.send(embed=embed)

#----------hinzufügen message----------

@client.event
async def on_guild_join(guild):
    welcome_message = f':exclamation:Hey:exclamation:Ich bin gerade {guild.name} (ID: {guild.id}) beigetreten!'
    channel = client.get_channel(1134573970268626996)
    if channel:
        await channel.send(welcome_message)

#----------Taschenrechner----------


@client.command()
async def calculate(ctx, *, expression):
        await ctx.message.delete()
        try:
            result = eval(expression)
            embed = discord.Embed(title='🧮Lösung🧮', color=discord.Color.dark_green())
            embed.add_field(name=f"🆘️Hilfe die Menschheit ist verloren, wenn man für so eine einfache Rechnung mich braucht.", value=f"🤓Naja nevermind, hier dein Ergebnis:\n‼️{result}‼️", inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f":exclamation:Nutze +|-|*|/ {e} !")

#----------On Messages----------


@client.event
async def on_message(message):
  if client.user in message.mentions:
        # Verbindung zur SQLite-Datenbank herstellen
        conn = sqlite3.connect('prefixes.db')
        cursor = conn.cursor()
        guild_id = message.guild.id
        cursor.execute('SELECT prefix FROM prefixes WHERE guild_id = ?', (guild_id,))
        result = cursor.fetchone()
        guild_prefix = result[0] if result else '?'
        embed = discord.Embed(title='💡Ich wurde gerufen?💡', color=discord.Color.dark_magenta())
        embed.add_field(name='ℹ️Du brauchst Hilfe?', value=f'* Mit `{guild_prefix}menü` kannst du all meine schicken Befehle sehen!', inline=False)
        embed.add_field(name=':alarm_clock:Uhrzeit', value= datetime.datetime.now().strftime("%H:%M:%S") , inline=True)
        embed.add_field(name=':calendar_spiral:Datum', value= datetime.date.today().strftime("%d.%m.%Y"), inline=True)
        conn.commit()
        async with message.channel.typing():
            await asyncio.sleep(8)
        await message.channel.send(embed=embed)
  await client.process_commands(message)
  if message.author == client.user:
    return
  if message.channel.name == "dbp-universe" and not message.author.bot:
        embed = discord.Embed(
            description=message.content,
            color=message.author.top_role.color if message.author.top_role else discord.Color(0x2f3136)
        )
        embed.set_author(name=f"{message.author.name} schrieb:", icon_url=message.author.avatar.url)
        embed.set_footer(text=f"Server: {message.guild.name}", icon_url=message.guild.icon.url)

        global_channels = [channel for guild in client.guilds for channel in guild.channels if channel.name == "dbp-universe"]

        for channel in global_channels:
            if channel.id != message.channel.id:
                sent_message = await channel.send(embed=embed)

                try:
                    await message.add_reaction("✅")
                except discord.Forbidden:
                    # Bot doesn't have permission to add reactions to the message
                    pass


@client.command(aliases=["create global"])
async def erstelle_global(ctx):
    await ctx.message.delete()
    existing_global_channel = discord.utils.get(ctx.guild.channels, name="dbp-universe")
    if existing_global_channel:
        await ctx.send("Der globale Chat ist bereits aktiviert.")
    else:
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        channel = await ctx.guild.create_text_channel("dbp-universe", overwrites=overwrites)
        await ctx.send(f"Der globale Chat wurde in {channel.mention} aktiviert.")

#----------tic tac toe----------

board = [' '] * 9
current_player = 'X'

def display_board():
    board_display = f"""
    {board[0]} | {board[1]} | {board[2]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[6]} | {board[7]} | {board[8]}
    """
    return board_display

def is_winner():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True

    if board[2] == board[4] == board[6] != ' ':
        return True

    return False

def is_draw():
    return ' ' not in board

def make_move(player, position):
    if position < 1 or position > 9 or board[position - 1] != ' ':
        return False

    board[position - 1] = player
    return True

@client.command()
async def ttt(ctx):
    await ctx.message.delete()
    global board, current_player
    board = [' '] * 9
    current_player = 'X'
    embed = discord.Embed(title=f"Neues Spiel gestartet! {current_player} ist dran.\n{display_board()}", color=discord.Color.dark_purple())
    await ctx.send(embed=embed)

@client.command()
async def f(ctx, position: int):
    await ctx.message.delete()
    global current_player
    if current_player == 'X':
        other_player = 'O'
    else:
        other_player = 'X'

    if position < 1 or position > 9:
        await ctx.send(":x:Ungültiger Zug! Versuche es erneut:x:")
        return
    if make_move(current_player, position):
        if is_winner():
            await ctx.send(f":partying_face:Glückwunsch! {current_player} hat gewonnen!:partying_face:")
            return
        elif is_draw():
            await ctx.send("😶Unentschieden!😶")
            return
        else:
            current_player, other_player = other_player, current_player
            embed = discord.Embed(title=f"⏭️{current_player} ist dran.\n{display_board()}", color=discord.Color.dark_purple())
            await ctx.send(embed=embed)

    else:
        await ctx.send("Ungültiger Zug! Versuche es erneut.")


#----------Hexcode finden----------

def get_color(color_name_or_hex):
    color_name = color_name_or_hex.lower()
    try:
        color = discord.Color(value=int(color_name.strip("#"), 16))
        return color, True
    except ValueError:
        try:
            rgb = webcolors.name_to_rgb(color_name)
            hex_value = "#%02x%02x%02x" % rgb
            color = discord.Color(value=int(hex_value.strip("#"), 16))
            return color, True
        except ValueError:
            return None, False

@client.command()
async def find_hex(ctx, *, color_name_or_hex):
    await ctx.message.delete()
    color, found = get_color(color_name_or_hex)

    if found:
        hex_code = color.value
        await ctx.send(f"✅️Der Hexcode für '{color_name_or_hex}' ist: #{hex(hex_code)[2:].upper()}")
    else:
        await ctx.send(":x:Ungültige Eingabe:exclamation:\nVersuche es mit der englischen Variante oder einem gültigem Hexcode!")

#----------translater----------

translator = Translator()

@client.command()
async def translate(ctx, target_language, *, text_to_translate):
    await ctx.message.delete()
    try:
        translated_text = translator.translate(text_to_translate, dest=target_language)
        await ctx.send(f"✅️Übersetzung in 🌐{target_language}🌐:\n⏭️Message: {translated_text.text}")
    except ValueError:
        await ctx.send(":x:Ungültige Sprache! Nutze: de, en,....")


# ----------test announcement----------

@client.command()
async def ads(ctx):
    await ctx.message.delete()
    if ctx.author.guild_permissions.administrator:
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send(
            "<:chat:1134854815458017350>In welchen Channel soll die Nachricht gehen?\n:exclamation:Nur den Namen ohne #")
        channel_msg = await client.wait_for('message', check=check)
        channel_name = channel_msg.content

        await ctx.send("📰Welchen Titel soll dein Embed schmücken?")
        title_msg = await client.wait_for('message', check=check)
        title = title_msg.content

        await ctx.send("📝Welche Beschreibung soll dein Embed haben?")
        description_msg = await client.wait_for('message', check=check)
        description = description_msg.content

        await ctx.send("📊Gib einen Farbcode an! (z.B.: 0xRRGGBB [:warning:Nur Hexcodes!])")
        color_msg = await client.wait_for('message', check=check)
        color_input = color_msg.content

        # Parse the color input from the user
        try:
            color = discord.Colour(int(color_input, 16))  # Convert hex to integer
        except ValueError:
            await ctx.send(":x:Ungültige Eingabe! Nutze Standartfarbe stattdessen...")
            color = discord.Colour.blue()

        embed = discord.Embed(
            title=title,
            description=description,
            color=color
        )

        await ctx.send("✅️Dein Embed wurde erstellt!\n↪️Hier für dich die endgültige Version:")
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)

        if channel:
            await channel.send(embed=embed)
        else:
            await ctx.send(f"Channel '{channel_name}' not found in this server.")
        await ctx.send(embed=embed)

    else:
        await ctx.send(
            ':x:Dir fehlt dazu die Berechtigung auf deinem Server!:x:\n:exclamation:Das darf nur ein Administrator:exclamation:')

#----------Mit embed cos----------

@client.command()
async def cos(ctx, player_tag):
    await ctx.message.delete()
    try:
        # API endpoint for player statistics
        api_url = f"https://api.clashofstats.com/players/{player_tag}"

        # Make the API request
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Extract the desired statistics from the JSON data
            player_name = data['name']
            town_hall_level = data.get('townHallLevel', "N/A")
            trophies = data['trophies']
            war_stars = data['warStars']
            player_level = data.get('expLevel', "N/A")
            troops_donated = data.get('donations', "N/A")
            troops_received = data.get('donationsReceived', "N/A")
            attacks_won = data.get('attackWins', "N/A")
            defenses_won = data.get('defenseWins', "N/A")
            league = data.get('league', {}).get('name', "N/A")
            master_builder_level = data.get('builderHallLevel', "N/A")
            builder_base_trophies = data.get('versusTrophies', "N/A")
            if data.get('clan'):
                clan_tag = data['clan']['tag']
                clan_name = data['clan']['name']
            else:
                clan_tag = "N/A"
                clan_name = "N/A"

            # Send the player statistics as a message
            th = "🔴"  # Standardwert, falls keine der Bedingungen erfüllt ist
            clan_badge_url = "https://cdn.discordapp.com/attachments/1135239501900431380/1135240031838162965/580b57fcd9996e24bc43c51c.png"

            if town_hall_level == 2:
               th = "️<:th2:1135316043548594267>"
               clan_badge_url = "https://cdn.discordapp.com/attachments/1135239501900431380/1135340157072056430/Rathaus_2.png"
            elif town_hall_level == 3:
              th = "<:th3:1135316122833526806>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340178270081054/Rathaus_3.png"
            elif town_hall_level == 4:
              th = "<:th4:1135316189959176214>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340191284998154/Rathaus_4.png"
            elif town_hall_level == 5:
              th = "<:th5:1135316369601208441>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340203570122782/Rathaus_5.png"
            elif town_hall_level == 6:
              th = "<:th6:1135316438475870349>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340216253689876/Rathaus_6.png"
            elif town_hall_level == 7:
              th = "<:th7:1135316507157598369>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340228387799170/Rathaus_7.png"
            elif town_hall_level == 8:
             th = "<:th8:1135316575503794276>"
             clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340252458909796/Rathaus_8.png"
            elif town_hall_level == 9:
              th = "<:th9:1135316656109916270>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340264957935757/Rathaus_9.png"
            elif town_hall_level == 10:
              th = "<:th10:1135316721138405456>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340278341980220/Rathaus_10.png"
            elif town_hall_level == 11:
              th = "<:th11:1135316796749119528>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340289016463380/Rathaus_11.png"
            elif town_hall_level == 12:
              th = "<:th12:1135316871424524370>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340300081053766/Rathaus_12_V.png"
            elif town_hall_level == 13:
              th = "<:th13:1135316935949680690>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340321224544286/Rathaus_13_V.png"
            elif town_hall_level == 14:
              th = "<:th14:1135317001976426677>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340335866843156/Rathaus_14_V.png"
            elif town_hall_level == 15:
              th = "<:th15:1135317071102738572>"
              clan_badge_url = "https://media.discordapp.net/attachments/1135239501900431380/1135340345828323328/Rathaus_15_5-1.png"

            embed = discord.Embed(title='<:king:1134854733589401721>Spielerdaten in Clash of Clans<:king:1134854733589401721>',
                          color=discord.Color.purple())
            embed.set_thumbnail(url=clan_badge_url)
            embed.set_image(
        url='https://media.discordapp.net/attachments/1135239501900431380/1135347822393294848/Screenshot_20230731_010557_Google.jpg')
            embed.add_field(name=f"__<:emoji_3:1120084892596846662>Spielername:__", value=f"* {player_name}", inline=True)
            embed.add_field(name=f"__<:levelp:1135198594962563162>Level:__", value=f"* {player_level}", inline=True)
            embed.add_field(name=f"__{th}Rathaus Level:__", value=f"* {town_hall_level}", inline=False)
            embed.add_field(name=f"__<:poki:1135198414364217354>Trophäen:__", value=f"* {trophies}", inline=False)
            embed.add_field(name=f"__<:angriffe:1135198901415194744>Gewonnene__\n__Angriffe:__", value=f"* {attacks_won}", inline=True)
            embed.add_field(name=f"__<:verteidigung:1135198974375108659>Gewonnene__\n__Verteidigungen:__", value=f"* {defenses_won}",
                    inline=True)
            embed.add_field(name=f"__<:cw:1135201072265314324>Clankriegssterne:__", value=f"* {war_stars}", inline=False)
            embed.add_field(name=f"__<:dd:1135214074423169094>Meisterhütte Level:__", value=f"* {master_builder_level}", inline=False)
            embed.add_field(name=f"__<:ddp:1135214139380334622>Trophäen im Nachtdorf:__", value=f"* {builder_base_trophies}",
                    inline=False)
            embed.add_field(name=f"__<:clan:1135201158600851546>Clan:__", value=f"* {clan_name}\n* {clan_tag}", inline=False)
            embed.add_field(name=f"__<:donation:1135198818837729320>Spenden:__", value=f"* {troops_donated}", inline=True)
            embed.add_field(name=f"__<:donation:1135198818837729320>Erhalten:__", value=f"* {troops_received}", inline=True)
            await ctx.send(embed=embed)

        else:
           await ctx.send("Failed to fetch player statistics. Please check the player tag and try again.")
    except:
         await ctx.send("An error occurred while fetching player statistics. Please try again later.")

#----------Command anzahl----------


@client.command()
async def command(ctx):
    await ctx.message.delete()
    # Get the number of commands registered with the bot
    num_commands = len(client.commands)
    await ctx.send(f"Ich unterstütze insgesamt {num_commands} Commands.")

#----------Hangman----------

WORDS = ["Apfel", "Buch", "Computer", "Delfin", "Elefant", "Fahrrad", "Giraffe", "Hut", "Igel", "Jacke", "Kamera", "Lampe", "Maus", "Nase", "Orange", "Pinguin", "Quark", "Regen", "Sonnenbrille", "Tasse", "Uhr", "Vogel", "Wal", "Xylophon", "Yoga", "Zebra", "Ananas", "Banane", "Chaos", "Dach", "Eule", "Feder", "Garten", "Hose", "Igel", "Jaguar", "Kaktus", "Löwe", "Mango", "Nuss", "Ozean", "Papier", "Qualle", "Rakete", "Sonne", "Tiger", "Unterwasser", "Vase", "Wald", "Zitrone", "Affe", "Blume", "Cupcake", "Diamant", "Eis", "Frosch", "Geige", "Hund", "Igel", "Jupiter", "König", "Löwe", "Mond", "Ninja", "Ohr", "Pizza", "Qualle", "Rakete", "Schuh", "Tür", "Vulkan", "Wolke", "Ziege", "Ameise", "Blatt", "Champagner", "Dinosaurier", "Einhorn", "Feder", "Gitarre", "Himmel", "Insel", "Jacke", "Kaktus", "Lippen", "Muschel", "Nacht", "Ozean", "Panda", "Quadrat", "Rakete", "Schloss", "Tasche", "Vogel", "Wolke", "Zucker", "Anker", "Blitz", "Chili", "Drache", "Ente", "Feuer", "Glas", "Hut"]

@client.command()
async def hangman(ctx):
    await ctx.message.delete()
    # Pick a random word from the list
    word = random.choice(WORDS).lower()

    # Initialize the game
    attempts = 6
    guessed_letters = set()
    display_word = '_' * len(word)

    # Send initial message
    embed = discord.Embed(title="📇Lass uns eine Runde Hangman spielen📇", color=discord.Color.green())
    embed.add_field(name=':exclamation:Ich werde dich nach einzelnen Buchstaben fragen.', value='* Also schreibe auch nur einzelne Buchstaben!', inline=False)
    await ctx.send(embed=embed)

    while attempts > 0 and '_' in display_word:
        # Display the current state of the word
        embed = discord.Embed(title=f"{' '.join(display_word)}", color=discord.Color.yellow())
        await ctx.send(embed=embed)

        # Wait for the player's response
        def check(message):
            return message.author == ctx.author and message.content.isalpha() and len(message.content) == 1

        try:
            response = await client.wait_for('message', check=check, timeout=30)
            letter = response.content.lower()

            if letter in guessed_letters:
                await ctx.send(":x:Den Buchstaben hattest du schon erraten!:x:")
            elif letter in word:
                guessed_letters.add(letter)
                display_word = ''.join(char if char in guessed_letters else '_' for char in word)
                embed = discord.Embed(title=f"✅️ '{letter}' befindet sich im gesuchtem Wort!",
                                      color=discord.Color.dark_green())
                await ctx.send(embed=embed)
            else:
                attempts -= 1
                guessed_letters.add(letter)
                embed = discord.Embed(
                    title=f":x:'{letter}' befindet sich nicht im gesuchtem Wort!:x:\n:warning:Dir bleiben noch {attempts} Versuche übrig!:warning:",
                    color=discord.Color.dark_red())
                await ctx.send(embed=embed)
        except asyncio.TimeoutError:
            embed = discord.Embed(title=":x:Zeit ist abgelaufen!:x:", color=discord.Color.dark_red())
            await ctx.send(embed=embed)
            return
            # Game over
    if '_' not in display_word:
        embed = discord.Embed(
             title=f":partying_face:Herzlichen Glühstrumpf! Du hast gewonnen!:partying_face:\n✅️Das gesuchte Wort war: {display_word}",
             color=discord.Color.green())
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=f":x:Ha! Du Looser!:x:\n:exclamation:Das gesuchte Wort war:'{word}'.",
                                  color=discord.Color.red())
        await ctx.send(embed=embed)


#----------Rennspiel----------

FOTO_FINISH = [
"https://media.discordapp.net/attachments/1135239501900431380/1135993561809166376/ConfusedLimpIrishwaterspaniel-size_restricted.gif",
"https://media.discordapp.net/attachments/1135239501900431380/1135993537171832862/BeautifulGlaringBumblebee-size_restricted.gif",
"https://media.discordapp.net/attachments/1135239501900431380/1135993509686558790/BlissfulFloweryHagfish-size_restricted.gif",
"https://media.discordapp.net/attachments/1135239501900431380/1135993417801945179/finish-race-nascar-on-nbc.gif"]

RACE_MESSAGE = ["Gefährliches Überholmanöver!", "Gutes Wetter, trockene Fahrbahn, warmgelaufende Motoren. Was will man mehr?!", "Uuuund da zieht er an ihm vorbei. Wahnsinn!", "Ein schönes Rennen, was wir hier zu sehen bekommen!"]

RACE_IMAGES = [
    "https://media.discordapp.net/attachments/1135239501900431380/1135891805217493012/AbandonedImpartialBlacklemur-size_restricted.gif",
    "https://media.discordapp.net/attachments/1135239501900431380/1135891832593711134/race-car-55_1.gif",
    "https://media.discordapp.net/attachments/1135239501900431380/1135891851392593940/2022-nascar.gif",
    "https://media.discordapp.net/attachments/1135239501900431380/1135888818218733568/E9ik.gif",
    "https://media.discordapp.net/attachments/1135239501900431380/1135891881822277782/6c384d31d2804647c90f90f017cfa386.gif",
    "https://media.discordapp.net/attachments/1135239501900431380/1135891907491418172/6RD.gif",
    "https://media.discordapp.net/attachments/1135239501900431380/1135891926084763678/1aCE.gif",
    "https://media.discordapp.net/attachments/1135239501900431380/1135891964726870046/XjqM.gif",
    # Füge hier weitere Bild-URLs hinzu
]

players_data = {}  # Dictionary, um Spielerdaten zu speichern (Discord ID -> Position)
race_started = False  # Variable, um den Rennstatus zu verfolgen

def add_player(player):
    if not race_started:
        if player.id not in players_data:
            players_data[player.id] = 0  # Startposition auf 0 setzen
        return True
    return False

def remove_player(player):
    if player.id in players_data:
        del players_data[player.id]

def get_random_race_image():
    return random.choice(RACE_IMAGES)

def get_random_message():
    return random.choice(RACE_MESSAGE)

def get_random_finish():
    return random.choice(FOTO_FINISH)

@client.command()
async def rennspiel(ctx):
    await ctx.message.delete()
    global race_started

    if not race_started:
        add_success = add_player(ctx.author)
        if add_success:
            await ctx.send(f"{ctx.author.mention} ist dem Rennen beigetreten! Aktuelle Spieler: {len(players_data)}")
        else:
            await ctx.send(f"{ctx.author.mention}, das Rennen ist bereits gestartet oder du benötigst mindestens 2 Spieler!")

@client.command()
async def rennen_start(ctx):
    await ctx.message.delete()
    global race_started

    if not race_started:
        if len(players_data) >= 2:  # Mindestanzahl von 2 Spielern erreicht
            race_started = True
            await ctx.send("Das Rennen hat begonnen! Wer die beste Positionierung am Ende hat, gewinnt!")

            distance = 10

            while True:
                await asyncio.sleep(1)
                for player_id in players_data:
                    players_data[player_id] += random.randint(1, 3)

                # Sende ein neues Embed mit der aktualisierten Rennanimation
                race_track_embed = discord.Embed(title="🏁 DBP-LIVE | vom 24h Rennen🏁")
                image_url = get_random_race_image()
                race_track_embed.add_field(name="🎧Live-Kommentar🎧", value=get_random_message(), inline=False)
                race_track_embed.set_image(url=image_url)
                await ctx.send(embed=race_track_embed, delete_after=5)

                if len(players_data) > 1 and any(pos >= distance for pos in players_data.values()):
                    race_started = False

                    await asyncio.sleep(2)  # Pause, um den Gewinner anzuzeigen

                    # Ermittle den Gewinner basierend auf der niedrigsten Position
                    winner_id = min(players_data, key=players_data.get)
                    if winner_id:
                        winner_name = ctx.guild.get_member(winner_id).display_name
                        embed = discord.Embed(title="🏁 DBP-LIVE | vom 24h Rennen🏁", color=discord.Color.gold())
                        embed.add_field(name="🎧Live-Kommentar🎧", value='Placeholder für random finish messages',
                                        inline=False)
                        finish_url = get_random_finish()
                        embed.set_image(url=finish_url)
                        await ctx.send(embed=embed)
                        await ctx.send(f"{winner_name}")

                    players_data.clear()
                    break

                await asyncio.sleep(5)  # Wartezeit von 5 Sekunden zwischen den Positionsupdates
            else:
                await ctx.send("Das Rennen kann nicht gestartet werden. Es werden mindestens 2 Spieler benötigt!")

        else:
            await ctx.send("Das Rennen läuft bereits!")

@client.command()
async def rennen_verlassen(ctx):
    await ctx.message.delete()
    if race_started:
        await ctx.send(f"{ctx.author.mention}, du kannst das Rennen nicht verlassen, während es läuft!")
    else:
        remove_player(ctx.author)
        await ctx.send(f"{ctx.author.mention} hat das Rennen verlassen.")

#----------nix----------

@client.command()
async def de(ctx):
    await ctx.message.delete()
    await ctx.send('# 🇩🇪🇩🇪🇩🇪SPRICH DEUTSCH DU HURENSOHN🇩🇪🇩🇪🇩🇪 #')
    await ctx.send('# 🇩🇪🇩🇪🇩🇪SPRICH DEUTSCH DU HURENSOHN🇩🇪🇩🇪🇩🇪 #')
    await ctx.send('# 🇩🇪🇩🇪🇩🇪SPRICH DEUTSCH DU HURENSOHN🇩🇪🇩🇪🇩🇪 #')
    await ctx.send('# 🇩🇪🇩🇪🇩🇪SPRICH DEUTSCH DU HURENSOHN🇩🇪🇩🇪🇩🇪 #')
    await ctx.send('# 🇩🇪🇩🇪🇩🇪SPRICH DEUTSCH DU HURENSOHN🇩🇪🇩🇪🇩🇪 #')
    await ctx.send('# 🇩🇪🇩🇪🇩🇪SPRICH DEUTSCH DU HURENSOHN🇩🇪🇩🇪🇩🇪 #')
    await ctx.send('# 🇩🇪🇩🇪🇩🇪SPRICH DEUTSCH DU HURENSOHN🇩🇪🇩🇪🇩🇪 #')
    await ctx.send('# 🇩🇪🇩🇪🇩🇪SPRICH DEUTSCH DU HURENSOHN🇩🇪🇩🇪🇩🇪 #')
    await ctx.send('# 🇩🇪🇩🇪🇩🇪SPRICH DEUTSCH DU HURENSOHN🇩🇪🇩🇪🇩🇪 #')
    await ctx.send('# 🇩🇪🇩🇪🇩🇪SPRICH DEUTSCH DU HURENSOHN🇩🇪🇩🇪🇩🇪 #')

#----------welcome message----------

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('welcome_channels.db')
cursor = conn.cursor()

# Datenbank-Tabelle erstellen, falls nicht vorhanden
cursor.execute('''
    CREATE TABLE IF NOT EXISTS welcome_channels (
        guild_id INTEGER,
        channel_id INTEGER,
        PRIMARY KEY (guild_id, channel_id)
    )
''')
conn.commit()


@client.command()
async def add_welcome_channel(ctx, channel: discord.TextChannel):
    await ctx.message.delete()
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('welcome_channels.db')
    cursor = conn.cursor()

    # Überprüfe, ob der aufrufende Benutzer die erforderlichen Berechtigungen hat
    if ctx.author.guild_permissions.manage_channels:
        cursor.execute('INSERT OR IGNORE INTO welcome_channels (guild_id, channel_id) VALUES (?, ?)',
                       (ctx.guild.id, channel.id))
        conn.commit()
        await ctx.send(f'{channel.mention} wurde als Willkommenskanal hinzugefügt.')
    else:
        await ctx.send('Du hast nicht die Berechtigung, Willkommenskanäle hinzuzufügen.')

    conn.close()


@client.command()
async def remove_welcome_channel(ctx, channel: discord.TextChannel):
    await ctx.message.delete()
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('welcome_channels.db')
    cursor = conn.cursor()

    # Überprüfe, ob der aufrufende Benutzer die erforderlichen Berechtigungen hat
    if ctx.author.guild_permissions.manage_channels:
        cursor.execute('DELETE FROM welcome_channels WHERE guild_id = ? AND channel_id = ?', (ctx.guild.id, channel.id))
        conn.commit()
        await ctx.send(f'{channel.mention} wurde als Willkommenskanal entfernt.')
    else:
        await ctx.send('Du hast nicht die Berechtigung, Willkommenskanäle zu entfernen.')

    conn.close()


@client.command()
async def list_welcome_channels(ctx):
    await ctx.message.delete()
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('welcome_channels.db')
    cursor = conn.cursor()

    cursor.execute('SELECT channel_id FROM welcome_channels WHERE guild_id = ?', (ctx.guild.id,))
    rows = cursor.fetchall()

    if rows:
        channels_mentions = [ctx.guild.get_channel(row[0]).mention for row in rows]
        channels_text = '\n'.join(channels_mentions)
        await ctx.send(f'Folgender Kanal wurde als Willkommenskanal festgelegt:\n{channels_text}')
    else:
        await ctx.send('Es wurde kein Willkommenskanal festgelegt.')

    conn.close()


@client.event
async def on_member_join(member):
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('welcome_channels.db')
    cursor = conn.cursor()
    guild = member.guild
    cursor.execute('SELECT channel_id FROM welcome_channels WHERE guild_id = ?', (guild.id,))
    rows = cursor.fetchall()

    for row in rows:
        welcome_channel_id = row[0]
        welcome_channel = client.get_channel(welcome_channel_id)

        if welcome_channel:
            embed = discord.Embed(
                title=f'🛬Frischfleisch ist gelandet: {member.display_name}!🛬',
                description=f'🤏🕶👀 Seid lieb zu unserem Frischling!',
                color=discord.Color.green()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_image(
                url='https://media.discordapp.net/attachments/1135239501900431380/1139616609430933604/wilkmn-5.gif')

            await welcome_channel.send(embed=embed)
    conn.close()


# ----------User  warnen---------

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('warnings.db')
cursor = conn.cursor()

# Datenbank-Tabelle erstellen, falls nicht vorhanden
cursor.execute('''
    CREATE TABLE IF NOT EXISTS warnings (
        guild_id INTEGER,
        user_id INTEGER,
        mod_id INTEGER,
        reason TEXT
    )
''')
conn.commit()


def is_mod(ctx):
    return ctx.author.guild_permissions.manage_messages


@client.command()
async def warn(ctx, user_id: int, *, reason: str):
    await ctx.message.delete()
    if ctx.author.guild_permissions.administrator:
        # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect('warnings.db')
        cursor = conn.cursor()

        # Warnung in die Datenbank eintragen
        cursor.execute('INSERT INTO warnings (guild_id, user_id, mod_id, reason) VALUES (?, ?, ?, ?)',
                       (ctx.guild.id, user_id, ctx.author.id, reason))
        conn.commit()

        user = await client.fetch_user(user_id)
        await ctx.send(f'{user.mention} wurde verwarnt: {reason}')
        embed = discord.Embed(title=f"__{ctx.guild.name}__", color=discord.Color.red())
        embed.add_field(name=f"⛔️Du wurdest verwarnt und registriert!", value=f"* Grund: {reason}", inline=False)
        await user.send(embed=embed)

        conn.close()
    else:
        await ctx.send("Maul halten!")


@client.command()
async def warnings(ctx, user_id: int):
    await ctx.message.delete()
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('warnings.db')
    cursor = conn.cursor()

    # Warnungen für den Benutzer abrufen
    cursor.execute('SELECT mod_id, reason FROM warnings WHERE guild_id = ? AND user_id = ?',
                   (ctx.guild.id, user_id))
    rows = cursor.fetchall()

    if rows:
        user = await client.fetch_user(user_id)
        warn_list = '\n'.join([f'{ctx.guild.get_member(row[0]).mention}: {row[1]}' for row in rows])
        embed = discord.Embed(title=f"📋Strafakte von {user.mention}📋", color=discord.Color.blurple())
        embed.add_field(name=f"🏷User ID:", value=f"{user.id}", inline=False)
        embed.add_field(name=f"🗃Hier sind sämtliche Warns:", value="`Zuständiger Admin` | `Warn Begründung`",
                        inline=False)
        embed.add_field(name=f"{warn_list}", value="", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f':x: Keine Warnungen für Benutzer mit ID {user_id}. :x:')

    conn.close()


@client.command()
async def clear_warnings(ctx, user_id: int):
    await ctx.message.delete()
    if ctx.author.guild_permissions.administrator:
        # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect('warnings.db')
        cursor = conn.cursor()

        # Warnungen für den Benutzer löschen
        cursor.execute('DELETE FROM warnings WHERE guild_id = ? AND user_id = ?',
                       (ctx.guild.id, user_id))
        conn.commit()

        user = await client.fetch_user(user_id)
        await ctx.send(f'Warnungen für {user.mention} (ID: {user.id}) wurden gelöscht.')
        embed = discord.Embed(title=f"__{ctx.guild.name}__", color=discord.Color.green())
        embed.add_field(name=f"✅️Sämtliche Verwarnungen wurden gelöscht!", value=f"Deine Strafakte ist nun rein.",
                        inline=False)
        await user.send(embed=embed)

        conn.close()

#----------Zeilen anzeigen---------

@client.command()
async def codelines(ctx):
    await ctx.message.delete()
    total_lines = 0

    for filename in os.listdir('.'):
        if filename.endswith('.py'):
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                total_lines += len(lines)

    await ctx.send(f'Leon hat sich bis jetzt mit insgesamt\n# {total_lines} #\n Zeilen Code gequält!')

#----------User bannen----------

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('banned_users.db')
cursor = conn.cursor()

# Tabelle für gebannte Benutzer erstellen
cursor.execute('''CREATE TABLE IF NOT EXISTS banned_users (
                  id INTEGER PRIMARY KEY,
                  user_id INTEGER,
                  username TEXT,
                  discriminator TEXT,
                  reason TEXT)''')
conn.commit()


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete()
    if ctx.author.guild_permissions.ban_members:
        # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect('banned_users.db')
        cursor = conn.cursor()
        await member.ban(reason=reason)

        # Benutzer in der Datenbank speichern
        cursor.execute('''INSERT INTO banned_users (user_id, username, discriminator, reason)
                           VALUES (?, ?, ?, ?)''', (member.id, member.name, member.discriminator, reason))
        conn.commit()

        await ctx.send(f'{member.mention} wurde gebannt und in der Datenbank gespeichert.')
        embed = discord.Embed(title=f"__{ctx.guild.name}__", color=discord.Color.red())
        embed.add_field(name=f"🔴Du wurdest gebannt!🔴", value=f"ℹ️Grund: {reason}", inline=False)
        await member.send(embed=embed)
        conn.close()
    else:
        # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect('warnings.db')
        cursor = conn.cursor()

        # Warnung in die Datenbank eintragen
        cursor.execute('INSERT INTO warnings (guild_id, user_id, mod_id, reason) VALUES (?, ?, ?, ?)',
                       (ctx.guild.id, user_id, 1124382919994118237, 'Ban-Missbrauch'))
        conn.commit()

        user = await client.fetch_user(user_id)
        await ctx.send(
            f'{user.mention} wurde verwarnt: Du Idiot willst wen bannen, obwohl dir die Rechte fehlen? Und lässt dich erwischen!?')
        embed = discord.Embed(title=f"__{ctx.guild.name}__", color=discord.Color.red())
        embed.add_field(name=f"⛔️Du wurdest verwarnt und registriert!", value=f"* Grund: Ban-Missbrauch", inline=False)
        await user.send(embed=embed)

        conn.close()


@client.command()
async def unban(ctx, user_id: int):
    await ctx.message.delete()
    if ctx.author.guild_permissions.ban_members:
        # Verbindung zur Datenbank herstellen
        conn = sqlite3.connect('banned_users.db')
        cursor = conn.cursor()
        # Den Benutzer versuchen zu entbannen (einfach als Beispiel - in Wirklichkeit hängt es von der tatsächlichen Implementierung ab)
        try:
            user = await client.fetch_user(user_id)
            await ctx.guild.unban(user)
            # Benutzer aus der Datenbank entfernen
            cursor.execute('''DELETE FROM banned_users WHERE user_id = ?''', (user_id,))
            conn.commit()

            await ctx.send(f'Benutzer mit der ID {user_id} wurde entbannt.')
            embed = discord.Embed(title=f"__{ctx.guild.name}__", color=discord.Color.green())
            embed.add_field(name=f" :white_check_mark: Du wurdest wieder entbannt!", value=f"⚠️Also benimm dich!",
                            inline=False)
            await user.send(embed=embed)
        except discord.NotFound:
            await ctx.send('Benutzer nicht gefunden.')
        conn.close()
    else:
        await ctx.send(f" :x: {ctx.author} ruhe auf den billigen Plätzen! :x:")


@client.command()
async def get_banned(ctx):
    await ctx.message.delete()
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('banned_users.db')
    cursor = conn.cursor()
    # Abfrage der gebannten Benutzer aus der Datenbank
    cursor.execute('''SELECT user_id, username, discriminator, reason FROM banned_users''')
    banned_users = cursor.fetchall()

    if banned_users:
        for user in banned_users:
            user_id, username, discriminator, reason = user
            embed = discord.Embed(title=f"🗃__Gebannte User__🗃", color=discord.Color.dark_red())
            embed.add_field(name=f"🏷{user_id}\n 🔰{username}#{discriminator}", value=f"__Grund__:》 {reason}")
            await ctx.send(embed=embed)
    else:
        await ctx.send("Keine gebannten Benutzer gefunden.")

    conn.close()

#----------prefix change----------

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('prefixes.db')
cursor = conn.cursor()

# Tabelle für die Präfixe erstellen (falls nicht vorhanden)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS prefixes (
        guild_id INTEGER PRIMARY KEY,
        prefix TEXT
    )
''')
conn.commit()

@client.command()
async def setprefix(ctx, prefix):
    await ctx.message.delete()
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('prefixes.db')
    cursor = conn.cursor()
    if ctx.author.guild_permissions.administrator:
         guild_id = ctx.guild.id
         cursor.execute('INSERT OR REPLACE INTO prefixes (guild_id, prefix) VALUES (?, ?)', (guild_id, prefix))
         conn.commit()
         await ctx.send(f'Präfix auf: `{prefix}` festgelegt.')
         client.command_prefix = get_custom_prefix
    else:
        await ctx.send('Schnauze!')
    conn.commit()

@client.command()
async def removeprefix(ctx):
    await ctx.message.delete()
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('prefixes.db')
    cursor = conn.cursor()
    if ctx.author.guild_permissions.administrator:
         guild_id = ctx.guild.id
         cursor.execute('DELETE FROM prefixes WHERE guild_id = ?', (guild_id,))
         conn.commit()
         await ctx.send('Benutzerdefiniertes Präfix entfernt. Verwende das Standardpräfix: `?`')
         client.command_prefix = '?'  # Setze wieder auf den Standardpräfix zurück
    else:
        await ctx.send('Mensch halt jetzt die Fresse!')
    conn.commit()

@client.command()
async def prefix(ctx):
    await ctx.message.delete()
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('prefixes.db')
    cursor = conn.cursor()
    guild_id = ctx.guild.id
    cursor.execute('SELECT prefix FROM prefixes WHERE guild_id = ?', (guild_id,))
    result = cursor.fetchone()
    guild_prefix = result[0] if result else '?'
    embed = discord.Embed(title=f"🗂Prefix für diesen Server🗂", color=discord.Color.dark_red())
    embed.add_field(name=f"Hallo! Mein Prefix für diesen Server ist: `{guild_prefix}`", value='', inline=False)
    embed.add_field(name=f"Befehle um mein Prefix zu ändern:", value=f"**{guild_prefix}setprefix [prefix]**\n**{guild_prefix}removeprefix**", inline=False)
    embed.add_field(name=f"⚠️***Denk dran, dass wenn du mein Prefix geändert hast, nur noch das CustomPrefix funktioniert!***⚠️", value='', inline=False)
    await ctx.send(embed=embed)
    conn.commit()

def get_custom_prefix(client, message):
    guild_id = message.guild.id
    cursor.execute('SELECT prefix FROM prefixes WHERE guild_id = ?', (guild_id,))
    result = cursor.fetchone()
    return result[0] if result else '?'

#-----------Zeit ansage----------
@tasks.loop(seconds=60)  # Hier wird das Intervall in Sekunden festgelegt
async def display_time():
    current_time = datetime.datetime.now(pytz.utc)
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    channel = client.get_channel(1134617650534809701)  # Ersetze YOUR_CHANNEL_ID durch die Kanal-ID
    await channel.send(f"Aktuelle Zeit: {formatted_time}", delete_after=60)

@client.command()
async def start_time_display(ctx):
    await ctx.message.delete()
    display_time.start()
    await ctx.send("Zeitanzeige gestartet.")

@client.command()
async def stop_time_display(ctx):
    await ctx.message.delete()
    display_time.stop()
    await ctx.send("Zeitanzeige gestoppt.")

#----------spielerei----------

@client.command()
async def update_message(ctx, message_id: int, new_content: str):
    try:
        message = await ctx.channel.fetch_message(message_id)
        await message.edit(content=new_content)
        await ctx.send('Nachricht erfolgreich aktualisiert.')
    except discord.NotFound:
        await ctx.send('Nachricht nicht gefunden.')

@client.command()
async def update_embed(ctx, message_id: int, new_title: str, new_description: str):
    try:
        message = await ctx.channel.fetch_message(message_id)
        if message.embeds:
            embed = message.embeds[0]
            embed.title = new_title
            embed.description = new_description
            await message.edit(embed=embed)
            await ctx.send('Embed in der Nachricht erfolgreich aktualisiert.')
        else:
            await ctx.send('Die Nachricht enthält kein Embed.')
    except discord.NotFound:
        await ctx.send('Nachricht nicht gefunden.')

#----------avatar----------

@client.command()
async def avatar(ctx):
      await ctx.message.delete()
      async with ctx.channel.typing():
          await asyncio.sleep(5)
          await ctx.send('<a:laden:1134179627481432245>Warte ich krame in den Discord-Datein rum...<a:laden:1134179627481432245>', delete_after=15)
          async with ctx.channel.typing():
             await asyncio.sleep(15)
      avatar_url = ctx.author.avatar.url if ctx.author.avatar else ctx.author.default_avatar.url
      await ctx.send(avatar_url,)
      async with ctx.channel.typing():
          await asyncio.sleep(2)
          await ctx.send(':white_check_mark:Hier dein Profilbild! :smile:\n<:emoji_11:1128476494977568828>War in der hinterletzten Ecke...')

#----------Buttons----------
class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Admin-Commands",description="Alles rund um Moderation!"),
            discord.SelectOption(label="Minispiel-Commands",description="Alles rund um Minigames!"),
            discord.SelectOption(label="Botspielerei",description="Alles rund um kleine Spielerein!"),
            discord.SelectOption(label="Prefix",description="Alle Infos über Prefix-Change!")
            ]
        super().__init__(placeholder="Wähle eine Kategorie aus!",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        # Verbindung zur SQLite-Datenbank herstellen
        conn = sqlite3.connect('prefixes.db')
        cursor = conn.cursor()
        guild_id = interaction.guild.id
        cursor.execute('SELECT prefix FROM prefixes WHERE guild_id = ?', (guild_id,))
        result = cursor.fetchone()
        guild_prefix = result[0] if result else '?'
        if self.values[0] == "Admin-Commands":
            embed = discord.Embed(title=f'__:warning:Admincommands:warning:__',
                                  color=discord.Color.dark_red())
            embed.add_field(name=f"__User warnen__", value=f"* {guild_prefix}warn [User ID] [Grund]", inline=False)
            embed.add_field(name=f"__Alle Warns für einen User löschen__", value=f"* {guild_prefix}clear_warnings [User ID]", inline=False)
            embed.add_field(name=f"__Alles Warns für einen User aufrufen__", value=f"* {guild_prefix}warnings [User ID]", inline=False)
            embed.add_field(name=f"__User im Voice muten__", value=f"* {guild_prefix}mute [User]", inline=False)
            embed.add_field(name=f"__User im Voice entmuten__", value=f"* {guild_prefix}unmute [User]", inline=False)
            embed.add_field(name=f"__User im Chat timeouten__", value=f"* {guild_prefix}timeout [User] [Duration in Minuten]\n* :warning:", inline=False)
            embed.add_field(name=f"__Rollen geben__", value=f"* {guild_prefix}addrole [Rolle] [User]", inline=False)
            embed.add_field(name=f"__Rollen entfernen__", value=f"* {guild_prefix}removerole [Rolle] [User]", inline=False)
            embed.add_field(name=f"__User vom Server kicken__", value=f"* {guild_prefix}kick [User]", inline=False)
            embed.add_field(name=f"__Nachrichten löschen__", value=f"* {guild_prefix}clean[Nachrichtenanzahl]", inline=False)
            embed.add_field(name=f"__Ankündigung erstellen__", value=f"* {guild_prefix}ads\n* :exclamation:Halte Hexcodes bereit für die Embedfarbe.", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1135239501900431380/1142790213962321950/Testbildmenu.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1135239501900431380/1142840907759099935/GLOBAL_CHAT_1.png")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        elif self.values[0] == "Minispiel-Commands":
            embed = discord.Embed(title=f'__:game_die:Minispiel-Commands:game_die:__',
                                  color=discord.Color.green())
            embed.add_field(name="__Würfeln__", value=f"* {guild_prefix}würfeln [Seitenanzahl des Würfels (optional)]", inline=False)
            embed.add_field(name=f"__Blackjack__", value=f"* {guild_prefix}blackjack", inline=False)
            embed.add_field(name=f"__Tachenrechner__", value=f"* {guild_prefix}calculate [Rechenaufgabe]")
            embed.add_field(name=f"__TicTacToe__", value=f"* {guild_prefix}ttt\n* {guild_prefix}f [Nummer des Feldes 1-9]\n* :warning:BEACHTE: Du brauchst min. 2 Spieler für dieses Minigame!", inline=False)
            embed.add_field(name=f"__Hangman__", value=f"* {guild_prefix}hangman", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1135239501900431380/1142789970877235310/Testbildmenu.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1135239501900431380/1142841564712927374/GLOBAL_CHAT_1.png")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        elif self.values[0] == "Botspielerei":
            embed = discord.Embed(title=f'__:robot:Bot-Spielerei:robot:__',
                                  color=discord.Color.dark_teal())
            embed.add_field(name=f"__Latenz__", value=f"* {guild_prefix}ping", inline=False)
            embed.add_field(name=f"__Profilbild aufrufen__", value=f"* {guild_prefix}avatar", inline=False)
            embed.add_field(name=f"__Userinfo__", value=f"* {guild_prefix}userinfo [User-ID]", inline=False)
            embed.add_field(name=f"__Serverinfo__", value=f"* {guild_prefix}serverinfo", inline=False)
            embed.add_field(name=f"__Botinfo__", value=f"* {guild_prefix}botinfo", inline=False)
            embed.add_field(name=f"__Global-Chat__", value=f"* {guild_prefix}erstelle_global\n* :warning:Denk daran die entsprechenden User/Rollen zum Kanal hinzuzufügen!", inline=False)
            embed.add_field(name=f"__Hexcode finden__", value=f"* {guild_prefix}find_hex [Farbenname auf Englisch]", inline=False)
            embed.add_field(name=f"__Clash of Stats__", value=f"* {guild_prefix}cos [Spielerkürzel ohne #]", inline=False)
            embed.add_field(name=f"__Command-Anzahl__", value=f"* {guild_prefix}command", inline=False)
            embed.add_field(name=f"__Codezeilen-Anzahl__", value=f"* {guild_prefix}codelines", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1135239501900431380/1142790415796420628/Testbildmenu.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1135239501900431380/1142842365426536458/GLOBAL_CHAT_1.png")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        elif self.values[0] == "Prefix":
            embed = discord.Embed(title="__<:astronaut:1137145211013840927>Prefix-Info<:astronaut:1137145211013840927>__", color=discord.Color.dark_magenta())
            embed.add_field(name=f"__Mein aktuelles Prefix für diesen Server__", value=f"`{guild_prefix}`", inline=False)
            embed.add_field(name=f"__Prefix ändern__", value=f"* {guild_prefix}setprefix", inline=False)
            embed.add_field(name=f"__Prefix zurücksetzen__", value=f"* {guild_prefix}removeprefix", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1135239501900431380/1143891956875935764/Testbildmenu.png")
            embed.set_image(url="https://cdn.discordapp.com/attachments/1135239501900431380/1143891967739183114/GLOBAL_CHAT_1.png")
            await interaction.response.send_message(embed=embed, ephemeral=True)
        conn.commit()


class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())

@client.command()
async def menü(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"__:information_source:Hilfs-Menü:information_source:__", color=discord.Color.teal())
    embed.add_field(name=f"Hier findest du sämtliche Commands, welche ich unterstütze.", value=f"Wähle einfach eine Kategorie aus!", inline=False)
    embed.add_field(name=f":alarm_clock:Uhrzeit:", value=datetime.datetime.now().strftime("%H:%M"), inline=True)
    embed.add_field(name=f":date:Datum:", value= datetime.date.today().strftime("%d.%m.%Y"), inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1135239501900431380/1142789044535840778/Testbildmenu.png")
    embed.set_image(url="https://media.discordapp.net/attachments/1135239501900431380/1142839607281594458/GLOBAL_CHAT_1.png?width=1024&height=52")
    embed.set_footer(text=f"Angefragt von {ctx.author.name}\nDieses Embed löscht sich automatisch nach 60 Sekunden!", icon_url=ctx.author.avatar.url)
    await ctx.send(embed=embed,view=SelectView(), delete_after=60)


#-----------to Do liste----------

@client.command()
async def todo(ctx):
     await ctx.message.delete()
     embed = discord.Embed(title=f"📝TO DO LISTE📝", color=discord.Color.red())
     embed.add_field(name=":white_check_mark:warn in liste aufnehmen\n :white_check_mark: ban schick machen und Berechtigung bearbeiten ", value="", inline=False)
     embed.add_field(name=f" :white_check_mark:warn und ban dm schick machen\n :white_check_mark: Welcome message embed bearbeiten ", value="", inline=False)
     embed.add_field(name=f"<a:loading:1134644133676449923>Minigame fertigstellen\n :white_check_mark: Kick dm erstellen\n<a:loading:1134644133676449923>Den bot verprügeln weil er mich nur ärgert", value="", inline=False)
     embed.add_field(name=f"<a:loading:1134644133676449923>On Message dm user bearbeiten", value=f"Antwort problem beheben", inline=False)
     embed.add_field(name=f"<a:loading:1134644133676449923>Verwendung für Zeitangabe ausdenken\n :white_check_mark: Avatar aus on message raus in befehl", value="", inline=False)
     embed.add_field(name=f":white_check_mark:Ping befehl in embed + eleganter machen", value="", inline=False)
     embed.add_field(name=f":white_check_mark:Button menü erstellen", value="<a:loading:1134644133676449923>Menü schick machen", inline=False)
     embed.add_field(name=f":white_check_mark:Bilder für Menüs erstellen", value=f"<a:loading:1134644133676449923>Neues pb für Bot", inline=False)
     embed.add_field(name=f"<a:loading:1134644133676449923>Emoji erstellen für die Menü-Punkte", value=f"", inline=False)
     embed.add_field(name=f"<a:loading:1134644133676449923>Endlich mal gescheites to machen", value="Und die ganzen Berechtigungen updaten", inline=False)
     embed.add_field(name=f".white_check_mark:Prefixchange wieder aktivieren", value="", inline=False)
     await ctx.send(embed=embed)


client.run(bot_token)