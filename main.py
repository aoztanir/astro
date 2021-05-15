###########PACKAGING INSTRUCTIONS:
#######pip install -r pyproject.toml


###########INFO/NOTES
#ONLY INSTALL DNSPYTHON==2.1.0


import discord
import datetime 
import syllables
import pymongo
from pymongo import MongoClient
# from replit import db
import random as rando
import wavelink
from discord_slash.utils.manage_commands import *
# from covid19_data import JHU
# from bottle import route, template, run
# from recommender.api import Recommender
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import praw
from discord_slash import SlashCommand, SlashContext, cog_ext

import asyncpraw
from discord.voice_client import VoiceClient
import youtube_dl
import random
import wikipedia
import textcaptcha
from discord.ext import commands
# Timedelta function demonstration  
  

import asyncio
import async_timeout
import copy
# import datetime
import discord
import math
import random
import re
import typing
import wavelink
from discord.ext import commands, menus
# from datetime import *



import os
# import lyricsgenius as lg
import asyncio
from googlesearch import search
# from flask import Flask
# import re
from youtubesearchpython import VideosSearch
# import urllib.request as ur
# from PyLyrics import *
# import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from datetime import timedelta
import pytz 
import time
# from pyowm import OWM
import requests, json
from discord.ext import commands
import pafy
# import keep_alive
from threading import Thread
import pyjokes
from lyrics_extractor import SongLyrics
import psutil
# intents = discord.Intents.all()
# client = discord.Client(intents=intents)
# import json 
# from emoji_translate.emoji_translate import Translator #######Deprecated for RPI
from PIL import Image
import requests
from io import StringIO
import urllib.request
from google_images_search import GoogleImagesSearch
from pyiku import haiku
ctxSave=None

# mutedUsers=[][]
import threading
QueList = []
TaskList = []
website="https://teamastro.ml/"
# filtered_words = ["word1","word2"]
# astroSite="https://teamastro.ml/"
# threader = threading.Thread(target=os.system("java -jar Lavalink.jar"))
# threader.start()
# os.system("java -jar Lavalink.jar")
# thread.start_new_thread(os.system, ('java -jar Lavalink.jar',))
intents = discord.Intents.default()
intents.members = True
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='b0d1cdbcce274e96905178376add6d61', client_secret="11a204d370c24b79891667ceb6fa5c31"))
def formatTitle(title: str):
  title=title.replace("(","")
  title=title.replace(")","")
  title=title.replace("[","")
  title=title.replace("]","")
  return title




mongoCli = MongoClient('mongodb+srv://aoztanir:astro@cluster0.740dq.mongodb.net/astro?retryWrites=true&w=majority')

# astroDB = pymongo.MongoClient("mongodb+srv://aoztanir:ladoo256@cluster0.740dq.mongodb.net/astro?retryWrites=true&w=majority")
datab = mongoCli.astro




def get_prefix(client, message):
  # try:
    return '.'
    prefixes = mongoCli['prefixes']
    # if client.user.id==841760295432880168:
    #   return '!'
    # prefixes=datab['prefixes']
    
    prefixObj = prefixes[str(message.guild.id)]
    if prefixObj == None:
      prefixObj.insert_one({'server': str(message.guild.id), 'prefix':'.'})
    prefixJson = prefixes.posts.find_one({'server': str(message.guild.id)})

    return prefixJson['prefix']

    # return '.'
    # prefixes = db["prefixes"]
    # with open('prefixes.json', 'r') as f: ##we open and read the prefixes.json, assuming it's in the same file
    #   prefixes = json.load(f) #load the json as prefixes
    try:
      return commands.when_mentioned_or(prefixes[str(message.guild.id)])(client, message) #recieve the prefix for the guild id given
    except:
      # with open('prefixes.json', 'r') as f: #read the prefix.json file
      #   prefixes = json.load(f) #load the json file
      prefixes=db["prefixes"]
      prefixes[str(message.guild.id)] = '.'#default prefix
      db["prefixes"]=prefixes

      # with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
      #   json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater
      return commands.when_mentioned_or(prefixes[str(message.guild.id)])(client, message)

      
  # except Exception as e:
  #   print(e)
# client = commands.Bot(
#     command_prefix= (get_prefix),
#     )


client = commands.AutoShardedBot(shard_count=4, command_prefix=(get_prefix), intents = discord.Intents.all(), case_insensitive=True)
# client = commands.AutoShardedBot(shard_count=2, command_prefix='.', intents = discord.Intents.all())

slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.

# @slash.slash(name="play")
# async def playSlash(ctx, song:): # Defines a new "context" (ctx) command called "ping."
#   await play(ctx,)


@client.event
async def on_ready():
    process = subprocess.Popen("java -jar Lavalink.jar", shell=True)
    
    await asyncio.sleep(20)
    client.add_cog(Music(client))
    # keep_alive.keep_alive()
    # dbd.openDash(client)
    # for server in client.guilds: 
    #   # Spin through every server
    #   for channel in server.channels: 
    #     # Channels on the server
    #     if channel.permissions_for(server.me).send_messages:
    #       try:
    #         await channel.send(f"> Astro Now Has A Dashboard! 🎉 Check this Servers Dashboard Out At https://teamastro.ml/guild/{server.id}")
    #         # So that we don't send to every channel:
    #       except:
    #         pass
    #       else:
    #         break
    with open("previous.json","r") as f:
      users = json.load(f)
    users={}
    with open("previous.json","w") as f:
      json.dump(users,f)
    # if skip == True:
    #     skip = False
    users = await get_bank_data()
    for user in users:
      users[str(user)]["job"]=False
      users[str(user)]["attacking"]=False
      users[str(user)]["attacking"]=False
      users[str(user)]["healing"]=False
    with open("mainbank.json","w") as f:
      json.dump(users,f)
    gameover1=True
    # await client.change_presence(activity=discord.Game(name = '🚀https://teamastro.ml/'))
    
    # await bot.change_presence(activity=discord.Game(name="a game"))

    # Setting `Streaming ` status
    # await client.change_presence(activity=discord.Streaming(name="🚀Team Astro", url="https://teamastro.ml/")) 
    # await client.change_presence(discord.Activity(name="Test"))
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Hooked On A Feeling"))
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name = '@Astro | teamastro.ml'))
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

    # await client.change_presence()
    # # Setting `Listening ` status
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

    # # Setting `Watching ` status
    # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
    print('ASTRO IS READY')
    print(str(client.shards))
    print(str(client.latencies))
    # await update_db()



# async def search_submissions():
#     while(true):
#         # do your stuff
#         await asyncio.sleep(1)

# @client.event
# async def on_raw_reaction_add(payload):
#   # Channel = client.get_channel(db["reaction_roles"])
#   # print("hiHIIII")
#   guild = discord.utils.find(lambda g : g.id == payload.guild_id, client.guilds)
#   for element in db["reaction_roles"][str(payload.guild_id)]:
#     # print(element)
#     if payload.message_id == element["id"]:
#       # print(payload.emoji.name)
#       for element2 in element["roleAdds"]:
#         if payload.emoji.name== element2["emoji"]:
#           Role = discord.utils.get(guild.roles, name=element2["role"])
#           await payload.member.add_roles( Role)



# @client.event
# async def on_raw_reaction_remove(payload):
#   # Channel = client.get_channel(db["reaction_roles"])
#   # print("hiHIIII")
#   guild = discord.utils.find(lambda g : g.id == payload.guild_id, client.guilds)
#   for element in db["reaction_roles"][str(payload.guild_id)]:
#     # print(element)
#     if payload.message_id == element["id"]:
#       # print(payload.emoji.name)
#       for element2 in element["roleAdds"]:
#         if payload.emoji.name== element2["emoji"]:
#           Role = discord.utils.get(guild.roles, name=element2["role"])
#           member = discord.utils.get(guild.members, id=payload.user_id)
#           await member.remove_roles( Role)




async def checkAmounts():
    users = await get_bank_data()
    for user in users:
      if users[str(user)]["health"]>=500:
        users[str(user)]["health"]=500
      if users[str(user)]["armor"]>=500:
        users[str(user)]["armor"]=500
      if users[str(user)]["armor"]<0:
        users[str(user)]["armor"]=0
      if users[str(user)]["health"]<=0:

        users[str(user)]["health"]=500
        users[str(user)]["armor"]=0
        users[str(user)]["wallet"]=400
        users[str(user)]["bank"]=0
        print(str(user)+" has lost everything")
        users[str(user)]["job"]=False
        users[str(user)]["attacking"]=False
        users[str(user)]["healing"]=False
        users[str(user)]["killer"]=None
      with open("mainbank.json","w") as f:
        json.dump(users,f)

# async def level( member):
#   lvl=-1
#   exp=-1
#   with open("userJson.json","r") as f:
#     users = json.load(f)
#   if str(member) in users:
#     exp = users[str(member)]["exp"]
#     lvl = users[str(member)]["lvl"]
#   else:
#     userLevelInfo = {"id" : str(member), "exp" : 0, "level": 1}
#     users[str(member)]= {}
#     users[str(member)]["exp"]=0
#     users[str(member)]["lvl"]=1
#     exp = users[str(member)]["exp"]
#     lvl = users[str(member)]["lvl"]
#   return exp, lvl




# URL matching REGEX...
URL_REG = re.compile(r'https?://(?:www\.)?.+')


class NoChannelProvided(commands.CommandError):
    """Error raised when no suitable voice channel was supplied."""
    pass


class IncorrectChannelError(commands.CommandError):
    """Error raised when commands are issued outside of the players session channel."""
    pass


class Track(wavelink.Track):
    """Wavelink Track object with a requester attribute."""

    __slots__ = ('requester', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args)

        self.requester = kwargs.get('requester')

class spotTrack(wavelink.Track):
    """Wavelink Track object for spotify"""

    __slots__ = ('requester', 'title', 'uri' )
    

    def __init__(self,**kwargs):
        # super().__init__(*args)
        self.title=kwargs.get('name')
        self.uri="https://open.spotify.com/"
        # self.query=kwargs.get('query')
        self.requester = kwargs.get('requester')


class Player(wavelink.Player):
    """Custom wavelink Player class."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.context: commands.Context = kwargs.get('context', None)
        if self.context:
            self.dj: discord.Member = self.context.author
        self.loopSong=False
        self.queue = asyncio.Queue()
        self.controller = None

        self.waiting = False
        self.updating = False
        self.loopTrack=None
        self.pause_votes = set()
        self.resume_votes = set()
        self.skip_votes = set()
        self.shuffle_votes = set()
        self.stop_votes = set()

    async def play(self, track):
      try:
        if  isinstance(track, spotTrack):
          try:
            spotifyTrack=await self.bot.wavelink.get_tracks(f'ytsearch:'+track.title, retry_on_failure=True)
            trackToQueue = Track(spotifyTrack[0].id, spotifyTrack[0].info, requester=track.requester)
            # if self.loopSong==True:
            #   await self.queue.put(trackToQueue)
            # self.loopTrack=trackToQueue
            return await super().play(trackToQueue)
          except:
            await self.stop()
            return await self.do_next()
    
          

        # if self.loopSong==True:
        #   await self.queue.put(track)
        # self.loopTrack=track
        await super().play( track)
      except:
        await self.stop()
        return await self.do_next()

    async def do_next(self) -> None:
      try:
        if self.is_playing or self.waiting:
            return
        # print(self.current.title)
        # Clear the votes for a new song...
        self.pause_votes.clear()
        self.resume_votes.clear()
        self.skip_votes.clear()
        self.shuffle_votes.clear()
        self.stop_votes.clear()

        try:
            self.waiting = True
            with async_timeout.timeout(300):
                track = await self.queue.get()
        except asyncio.TimeoutError:
            # No music has been played for 5 minutes, cleanup and disconnect...
            return await self.teardown()
        # if self.loopSong and self.loopTrack!=None:
        #   await self.queue.put(self.loopTrack)
        if self.channel_id==None:
          return await self.teardown()
        channel =  client.get_channel(self.channel_id)
        member_count=0
        for element in channel.members:
          if not element.bot:
            member_count+=1
        if member_count<1:
          print("DISCONNECTING")
          return await self.teardown()

        await self.play(track)
        self.waiting = False

        # Invoke our players controller...
        await self.invoke_controller()
      except:
        await self.stop()
        return await self.do_next()



    async def searchPlaylist(self, ctx, playlist):
      player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
      tracks=playlist["tracks"]
      for i in range(len(tracks["items"])):
        # player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
        # print(player)
        if i!=0:
          # try:
            # trackSpot = await self.bot.wavelink.get_tracks(str(f'ytsearch:'+tracks["items"][i]["track"]["name"]+" - "+tracks["items"][i]["track"]["artists"][0]["name"]), retry_on_failure=True)
          trackToQueue = spotTrack(name=tracks["items"][i]["track"]["name"]+" - "+tracks["items"][i]["track"]["artists"][0]["name"], requester=ctx.author)
          await player.queue.put(trackToQueue)
        
          # except:
          #   pass

      while tracks['next']:
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
        if player==None:
          return
        tracks = spotify.next(tracks)
        for item in tracks["items"]:
          try:
            # trackSpot = await self.bot.wavelink.get_tracks(str(f'ytsearch:'+item["track"]["name"]+" - "+item["track"]["artists"][0]["name"]), retry_on_failure=True)
            # trackToQueue = Track(trackSpot[0].id, trackSpot[0].info, requester=ctx.author)
            trackToQueue = spotTrack(name=item["track"]["name"]+" - "+item["track"]["artists"][0]["name"], requester=ctx.author)
            await player.queue.put(trackToQueue)
            # await player.queue.put(trackToQueue)
        
          except:
            pass





    async def invoke_controller(self) -> None:
      try:
        """Method which updates or sends a new player controller."""
        if self.updating:
            return
        if self.current==None:
          return

        self.updating = True

        if not self.controller:
            self.controller = InteractiveController(embed=self.build_embed(), player=self)
            await self.controller.start(self.context)

        elif not await self.is_position_fresh():
            try:
                await self.controller.message.delete()
            except discord.HTTPException:
                pass

            self.controller.stop()

            self.controller = InteractiveController(embed=self.build_embed(), player=self)
            await self.controller.start(self.context)

        else:
            channel = self.bot.get_channel(int(self.channel_id))
            embed = self.build_embed()
            embed2 = discord.Embed(title=f'ASTRO MUSIC | {channel.name}', colour=discord.Color.green())
            # if embed.description==None:
            #   await self.controller.message.edit(content=f"** > 🔊 {channel}**")
            await self.controller.message.edit(content=None, embed=embed)
            

        self.updating = False
      except:
        pass
    def build_embed(self) -> typing.Optional[discord.Embed]:
      try:
        """Method which builds our players controller embed."""
        track = self.current
        if not track:
            return discord.Embed(title=f'ASTRO MUSIC | ▶️', colour=discord.Color.green())
        # player: Player = self.bot.wavelink.get_player(guild_id=, cls=Player, context=ctx)
        try:
          length2 = track.length
        except:
          length2=1
        try:
          length=str(datetime.timedelta(milliseconds=int(track.length)))
  
        except:
          length="LIVE"
        status='🔘'
        if self.is_paused:
          status="⏸"
        positionPercent =  float(self.position/length2)
        position="|"
        for i in range(30):
          position+="▬"
        position+="|"
        posNum=int(30*positionPercent)+1
        position = position[:posNum] + status + position[posNum+1:]
        if track.is_stream:
          position = "🔴 LIVE"
        channel = self.bot.get_channel(int(self.channel_id))
        qsize = self.queue.qsize()

        embed = discord.Embed(colour=discord.Color.green())
        embed.description = f'**Now Playing:**\n**[{formatTitle(track.title[:30])}...]({track.uri})**\n\n`{position}`\n\n'
        try:
          embed.set_thumbnail(url=track.thumb)
          if track.thumb==None:
            embed.set_thumbnail(url=f"{client.user.avatar_url}")
        except:
          embed.set_thumbnail(url=f"{client.user.avatar_url}")

        embed.add_field(name='Duration', value=f"**` {length} `**")
        embed.add_field(name='Queue Length', value=f'` {str(qsize)} `')
        embed.add_field(name='Volume', value=f'**` {self.volume}% `**')
        embed.add_field(name='Requested By', value=track.requester.mention)
        embed.add_field(name='DJ', value=self.dj.mention)
        embed.add_field(name='Looping', value=f'**{self.loopSong}**')
        # embed.add_field(name="Show's This Command", value=f'` np `')

        return embed
      except:
        return discord.Embed(title=f'ASTRO MUSIC | ▶️', colour=discord.Color.green())
    async def is_position_fresh(self) -> bool:
        """Method which checks whether the player controller should be remade or updated."""
        try:
            async for message in self.context.channel.history(limit=5):
                if message.id == self.controller.message.id:
                    return True
        except (discord.HTTPException, AttributeError):
            return False

        return False

    async def teardown(self):
        """Clear internal states, remove player controller and disconnect."""
        try:
            await self.controller.message.delete()
        except:
            pass
        try:
          self.controller.stop()
        except:
          pass

        try:
            # del self.searchPlaylist
            await self.destroy()
            
        except KeyError:
            pass


class InteractiveController(menus.Menu):
    """The Players interactive controller menu class."""

    def __init__(self, *, embed: discord.Embed, player: Player):
        super().__init__(timeout=None)

        self.embed = embed
        self.player = player

    def update_context(self, payload: discord.RawReactionActionEvent):
        """Update our context with the user who reacted."""
        ctx = copy.copy(self.ctx)
        ctx.author = payload.member

        return ctx

    def reaction_check(self, payload: discord.RawReactionActionEvent):
        # if payload.event_type == 'REACTION_REMOVE':
        #     return False

        if not payload.member:
            return False
        if payload.member.bot:
            return False
        if payload.message_id != self.message.id:
            return False
        if payload.member not in self.bot.get_channel(int(self.player.channel_id)).members:
            return False

        return payload.emoji in self.buttons

    async def send_initial_message(self, ctx: commands.Context, channel: discord.TextChannel) -> discord.Message:
   
        # voicechannel = self.bot.get_channel(int(self.player.channel_id))
        return await channel.send(content=None , embed=self.embed)

    # @menus.button(emoji='\u25B6')
    # async def resume_command(self, payload: discord.RawReactionActionEvent):
    #     """Resume button."""
    #     ctx = self.update_context(payload)

    #     command = self.bot.get_command('resume')
    #     ctx.command = command

    #     await self.bot.invoke(ctx)
    #     command = self.bot.get_command('np')
    #     ctx.command = command

    #     await self.bot.invoke(ctx)
    
    @menus.button(emoji='⏪')
    async def ff_command(self, payload: discord.RawReactionActionEvent):
        """Volume up button"""
        ctx = self.update_context(payload)

        command = self.bot.get_command('f_down')
        ctx.command = command

        await self.bot.invoke(ctx)
        command = self.bot.get_command('np')
        ctx.command = command

        await self.bot.invoke(ctx)
    @menus.button(emoji='⏯')
    async def pause_command(self, payload: discord.RawReactionActionEvent):
        """Pause button"""
        ctx = self.update_context(payload)
        player: Player = self.bot.wavelink.get_player(ctx.guild.id, cls=Player, context=ctx)
        if player.is_playing and not player.is_paused:

          command = self.bot.get_command('pause')
          ctx.command = command

          await self.bot.invoke(ctx)
          command = self.bot.get_command('np')
          ctx.command = command

          return await self.bot.invoke(ctx)
        if player.is_paused:
          ctx = self.update_context(payload)

          command = self.bot.get_command('resume')
          ctx.command = command

          await self.bot.invoke(ctx)
          command = self.bot.get_command('np')
          ctx.command = command

          return await self.bot.invoke(ctx)
    @menus.button(emoji='⏩')
    async def fb_command(self, payload: discord.RawReactionActionEvent):
        """Volume down button."""
        ctx = self.update_context(payload)

        command = self.bot.get_command('f_up')
        ctx.command = command

        await self.bot.invoke(ctx)
        command = self.bot.get_command('np')
        ctx.command = command

        await self.bot.invoke(ctx)
    @menus.button(emoji='\u23ED')
    async def skip_command(self, payload: discord.RawReactionActionEvent):
        """Skip button."""
        ctx = self.update_context(payload)

        command = self.bot.get_command('skip')
        ctx.command = command

        await self.bot.invoke(ctx)
    @menus.button(emoji='🔂')
    async def loop_command(self, payload: discord.RawReactionActionEvent):
        """Skip button."""
        ctx = self.update_context(payload)

        command = self.bot.get_command('loop')
        ctx.command = command

        await self.bot.invoke(ctx)
        command = self.bot.get_command('np')
        ctx.command = command

        await self.bot.invoke(ctx)
    @menus.button(emoji='⏺')
    async def rewind_command(self, payload: discord.RawReactionActionEvent):
        """Skip button."""
        ctx = self.update_context(payload)

        command = self.bot.get_command('rewind')
        ctx.command = command

        await self.bot.invoke(ctx)
   
    @menus.button(emoji='\U0001F500')
    async def shuffle_command(self, payload: discord.RawReactionActionEvent):
        """Shuffle button."""
        ctx = self.update_context(payload)

        command = self.bot.get_command('shuffle')
        ctx.command = command

        await self.bot.invoke(ctx)

    @menus.button(emoji='🔊')
    async def volup_command(self, payload: discord.RawReactionActionEvent):
        """Volume up button"""
        ctx = self.update_context(payload)

        command = self.bot.get_command('vol_up')
        ctx.command = command

        await self.bot.invoke(ctx)
        command = self.bot.get_command('np')
        ctx.command = command

        await self.bot.invoke(ctx)
    @menus.button(emoji='🔉')
    async def voldown_command(self, payload: discord.RawReactionActionEvent):
        """Volume down button."""
        ctx = self.update_context(payload)

        command = self.bot.get_command('vol_down')
        ctx.command = command

        await self.bot.invoke(ctx)
        command = self.bot.get_command('np')
        ctx.command = command
    
    
    @menus.button(emoji='🎸')
    async def queue_command(self, payload: discord.RawReactionActionEvent):
        """Player queue button."""
        ctx = self.update_context(payload)

        command = self.bot.get_command('queue')
        ctx.command = command

        await self.bot.invoke(ctx)

    
    @menus.button(emoji='🔃')
    async def reload_command(self, payload: discord.RawReactionActionEvent):
        """Player Reload button."""
        ctx = self.update_context(payload)

        command = self.bot.get_command('np')
        ctx.command = command

        await self.bot.invoke(ctx)
    @menus.button(emoji='⁉')
    async def help_command(self, payload: discord.RawReactionActionEvent):
        """Player Reload button."""
        ctx = self.update_context(payload)

        command = self.bot.get_command('question_controller')
        ctx.command = command

        await self.bot.invoke(ctx)
    @menus.button(emoji='🛑')
    async def stop_command(self, payload: discord.RawReactionActionEvent):
        """Stop button."""
        ctx = self.update_context(payload)

        command = self.bot.get_command('stop')
        ctx.command = command

        await self.bot.invoke(ctx)
class PaginatorSource(menus.ListPageSource):
    """Player queue paginator class."""

    def __init__(self, entries, *, per_page=8):
        super().__init__(entries, per_page=per_page)

    async def format_page(self, menu: menus.Menu, page):
        embed = discord.Embed(title='Coming Up...', colour=discord.Color.orange())
        # print(page)
        embed.description = '\n'.join(f'{title}' for index, title in enumerate(page, 1))

        return embed

    def is_paginating(self):
        # We always want to embed even on 1 page of results...
        return True


class Music(commands.Cog, wavelink.WavelinkMixin):
    """Music Cog."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

        if not hasattr(bot, 'wavelink'):
            bot.wavelink = wavelink.Client(bot=bot)

        bot.loop.create_task(self.start_nodes())
    # async def start_nodes(self):
    #     await self.bot.wait_until_ready()

    #     # Initiate our nodes. For this example we will use one server.
    #     # Region should be a discord.py guild.region e.g sydney or us_central (Though this is not technically required)
    #     await self.bot.wavelink.initiate_node(host='0.0.0.0',
    #                                           port=2333,
    #                                           rest_uri='http://0.0.0.0:2333',
    #                                           password='youshallnotpass',
    #                                           identifier='TEST',
    #                                           region='us_central')
    async def start_nodes(self) -> None:
        """Connect and intiate nodes."""
        await self.bot.wait_until_ready()

        if self.bot.wavelink.nodes:
            previous = self.bot.wavelink.nodes.copy()

            for node in previous.values():
                await node.destroy()

        nodes = {'MAIN': {'host':'0.0.0.0',
                          'port':2333,
                          'rest_uri':'http://0.0.0.0:2333',
                          'password':'youshallnotpass',
                          'identifier':'MAIN',
                          'region':'us_central'
                          }}
        # nodes = {'MAIN': {'host': 'x',
        #                   'port': 2333,
        #                   'rest_uri': 'http://x:2333',
        #                   'password': 'youshallnotpass',
        #                   'identifier': 'MAIN',
        #                   'region': 'us_central'
        #                   }}
                        

        for n in nodes.values():
            await self.bot.wavelink.initiate_node(**n)

    @wavelink.WavelinkMixin.listener()
    async def on_node_ready(self, node: wavelink.Node):
        print(f'Node {node.identifier} is ready!')

    @wavelink.WavelinkMixin.listener('on_track_stuck')
    @wavelink.WavelinkMixin.listener('on_track_end')
    @wavelink.WavelinkMixin.listener('on_track_exception')
    async def on_player_stop(self, node: wavelink.Node, payload):
        await payload.player.do_next()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if member.bot:
            return

        player: Player = self.bot.wavelink.get_player(member.guild.id, cls=Player)

        if not player.channel_id or not player.context:
            player.node.players.pop(member.guild.id)
            return

        channel = self.bot.get_channel(int(player.channel_id))

        if member == player.dj and after.channel is None:
            for m in channel.members:
                if m.bot:
                    continue
                else:
                    player.dj = m
                    return

        elif after.channel == channel and player.dj not in channel.members:
            player.dj = member

    # async def cog_command_error(self, ctx: commands.Context, error: Exception):
    #     """Cog wide error handler."""
    #     if isinstance(error, IncorrectChannelError):
    #         return

    #     if isinstance(error, NoChannelProvided):
    #         embed=discord.Embed(description="**You must be in a voice channel or provide one to connect to**".title(), color = discord.Color.red())
    #         return await ctx.send(embed=embed, delete_after=10)
    #         # return await ctx.send('')

    async def cog_check(self, ctx: commands.Context):
        """Cog wide check, which disallows commands in DMs."""
        if not ctx.guild:
            await ctx.send('Music commands are not available in Private Messages.')
            return False

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        """Coroutine called before command invocation.
        We mainly just want to check whether the user is in the players controller channel.
        """
        player: Player = self.bot.wavelink.get_player(ctx.guild.id, cls=Player, context=ctx)

        if player.context:
            if player.context.channel != ctx.channel:
                embed=discord.Embed(description=f"**{ctx.author.mention} You Must Be In {player.context.channel.mention} To Control Astro's Music**", color = discord.Color.red())
                await ctx.send(embed=embed, delete_after=10)
                # await ctx.send(f'{ctx.author.mention}, you must be in {player.context.channel.mention} for this session.')
                raise IncorrectChannelError

        if ctx.command.name == 'connect' and not player.context:
            return
        elif self.is_privileged(ctx):
            return

        if not player.channel_id:
            return

        channel = self.bot.get_channel(int(player.channel_id))
        if not channel:
            return

        if player.is_connected:
            if ctx.author not in channel.members:
                embed=discord.Embed(description=f"**{ctx.author.mention}, You Must Be In `{channel.name}` To Control Astro's Music**", color = discord.Color.red())
                await ctx.send(embed=embed, delete_after=10)
          
                raise IncorrectChannelError
    
    def required(self, ctx: commands.Context):
        """Method which returns required votes based on amount of members in a channel."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
        channel = self.bot.get_channel(int(player.channel_id))
        required = math.ceil((len(channel.members) - 1) / 2.5)

        if ctx.command.name == 'stop':
            if len(channel.members) == 3:
                required = 2

        return required

    def is_privileged(self, ctx: commands.Context):
        """Check whether the user is an Admin or DJ."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        return player.dj == ctx.author or ctx.author.guild_permissions.kick_members

    @commands.command()
    async def connect(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        """Connect to a voice channel."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if player.is_connected:
            return

        channel = getattr(ctx.author.voice, 'channel', channel)
        if channel is None:
            raise NoChannelProvided

        await player.connect(channel.id)


    # @commands.command(aliases=['seek','moveto'])
    # async def move(self, ctx: commands.Context, timestamp: str=None):
    #   player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
    #   await player.seek(int(timestamp)*1000)
    
    


    @cog_ext.cog_slash(name="play",
             description="Plays Music Through Any Voice Channel",
             options=[
               create_option(
                 name="song",
                 description="Song Name / Playlist URL",
                 option_type=3,
                 required=False
               )
             ])
    async def playSlash(self, ctx: SlashContext, song: str):
        # ctx=commands.context(ctx)
        return await self.play(ctx,query=song)

    @commands.command(aliases = [ 'sing'])
    @commands.cooldown(1,3,commands.BucketType.user)
    async def lyrics(self, ctx,*, song : str=None):
      player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
      if song==None:
        if player.current==None:
          embed=discord.Embed(description=f'**Currently Nothing Is Playing**', color = discord.Color.red())
          return await ctx.send(embed=embed, delete_after=10)
        
        song=player.current.title
        print(song)
      try:

        extract_lyrics = SongLyrics("AIzaSyBRcquo71lWc8_jaTOF-bhaEeT-fgfjI6M", "72f842b0aaf3270be")
        loop = asyncio.get_event_loop()
        test_dict = await loop.run_in_executor(None, lambda:extract_lyrics.get_lyrics(song))
        # test_dict = extract_lyrics.get_lyrics(song)
        res = {key: test_dict[key] for key in test_dict.keys() 
                                    & {'lyrics'}}
        for key, value in test_dict.items(): 
          if key == "lyrics":
            valSave = str(value)
        embed=discord.Embed(title="Lyrics For "+song.title(), color = discord.Color.green())
        # await ctx.send("Here are the lyrics! \n")
        valArr = valSave.split("\n\n")
        for element in valArr:
          embed.add_field(name="`~"+"`", value="`"+element+"`", inline=False)
        await ctx.send(embed=embed)
      except:
        embed=discord.Embed(description="**Couldn't Find That Song**", color = discord.Color.red())
        await ctx.send(embed=embed)
        return
    
    @commands.command(aliases=['p'])
    @commands.cooldown(1,2,commands.BucketType.user)
    async def play(self, ctx: commands.Context, *, query: str=None):
        """Play or queue a song with the given query."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_connected:
            await ctx.invoke(self.connect)
        if query==None:
          if player.is_paused:
            return await self.resume(ctx)
          else:
            embed=discord.Embed(description=f'**Specify A Song To Play**', color = discord.Color.red())
            await ctx.send(embed=embed)

          return

        if ctx.author.id==608778878835621900:
          if query=="my jam":
            query="https://open.spotify.com/playlist/6A83PFHKOMYMQTV6YwSeNk"

        query = query.strip('<>')
        if not URL_REG.match(query):
            query = f'ytsearch:{query}'
      # if "open.spotify.com" not in query:
        tracks = await self.bot.wavelink.get_tracks(query, retry_on_failure=True)
        # else:
        #   track=None
       
        if not tracks:
            # print(query)
            if "open.spotify.com/track"in query:
              try:
                song=spotify.track("query")
              except Exception as e:
                print(e)
                embed=discord.Embed(description=f'**Invalid Song URL**', color = discord.Color.red())
                return await ctx.send(embed=embed, delete_after=10)
              # print(song.keys())
              trackSpot = await self.bot.wavelink.get_tracks(str(f'ytsearch:'+song["name"]+" - "+song["artists"][0]["name"]), retry_on_failure=True)
              trackToQueue = Track(trackSpot[0].id, trackSpot[0].info, requester=ctx.author)
              await player.queue.put(trackToQueue)
              try:
                length = str(datetime.timedelta(milliseconds=int(trackToQueue.length)))
              except:
                length="LIVE"
              embed=discord.Embed(description=f'**Queued [{formatTitle(trackToQueue.title[:30])}...]({trackToQueue.uri}) ` {length} ` | Requestor: {trackToQueue.requester.mention}**', color = discord.Color.green())
              try:
                embed.set_thumbnail(url=trackToQueue.thumb)
                if trackToQueue.thumb==None:
                  embed.set_thumbnail(url=f"{client.user.avatar_url}")
              except:
                embed.set_thumbnail(url=f"{client.user.avatar_url}")
              await ctx.send(embed=embed, delete_after=20)
              if not player.is_playing:
                return await player.do_next()
              return

            # if "open.spotify.com/album" in query:
            #   try:
            #     album=spotify.album(query)
            #   except:
            #     embed=discord.Embed(description=f'**Invalid Album URL**', color = discord.Color.red())
            #     return await ctx.send(embed=embed, delete_after=10)
            #   await self.searchPlaylist(ctx, album)
            #   return

            if "open.spotify.com/playlist"  in query:
              try:
                print(query)
                playlist=spotify.playlist(query)
                print(playlist["tracks"].keys())
                trackSpot = await self.bot.wavelink.get_tracks(str(f'ytsearch:'+playlist['tracks']["items"][0]["track"]["name"]+" - "+playlist['tracks']["items"][0]["track"]["artists"][0]["name"]), retry_on_failure=True)
                trackToQueue = Track(trackSpot[0].id, trackSpot[0].info, requester=ctx.author)
                await player.queue.put(trackToQueue)
                embed=discord.Embed(description=f'**Queued `{playlist["tracks"]["total"]}` Tracks From `{playlist["name"]}`**', color = discord.Color.green())
                await ctx.send(embed=embed, delete_after=20)
              except Exception as e:
                print(e)
                embed=discord.Embed(description=f'**Invalid Playlist URL**', color = discord.Color.red())
                return await ctx.send(embed=embed, delete_after=10)
              # playlist=spotify.playlist(query)
              # print(playlist)
              
              
             
              await player.searchPlaylist(ctx, playlist)
              if not player.is_playing:
                await player.do_next()
              # trackLength=0

              # for item in playlist['tracks']["items"]:

              #   try:
              #     trackSpot = await self.bot.wavelink.get_tracks(str(f'ytsearch:'+item["track"]["name"]), retry_on_failure=True)
              #     trackToQueue = Track(trackSpot[0].id, trackSpot[0].info, requester=ctx.author)
              #     await player.queue.put(trackToQueue)
              #     trackLength+=1
              #   except:
              #     pass
       
              if not player.is_playing:
                return await player.do_next()
              return
              
            embed=discord.Embed(description=f'**✋ Nothing Found**'.title(), color = discord.Color.orange())
            return await ctx.send(embed=embed, delete_after=10)
            # return await ctx.send('No songs were found with that query. Please try again.', delete_after=15)

        if isinstance(tracks, wavelink.TrackPlaylist):
            for track in tracks.tracks:
                track = Track(track.id, track.info, requester=ctx.author)
                await player.queue.put(track)

            # await ctx.send(f'```ini\nAdded the playlist {tracks.data["playlistInfo"]["name"]}'
            #                f' with {len(tracks.tracks)} songs to the queue.\n```', delete_after=15)
            embed=discord.Embed(description=f'**Queued {len(tracks.tracks)} Tracks**', color = discord.Color.green())
            await ctx.send(embed=embed, delete_after=10)
        else:
     
            track = Track(tracks[0].id, tracks[0].info, requester=ctx.author)
            
            try:
              length = str(datetime.timedelta(milliseconds=int(track.length)))
            except:
              length="LIVE"
            embed=discord.Embed(description=f'**Queued [{formatTitle(track.title[:30])})...]({track.uri}) ` {length} ` | Requestor: {track.requester.mention}**', color = discord.Color.green())
            try:
              embed.set_thumbnail(url=track.thumb)
              if track.thumb==None:
                embed.set_thumbnail(url=f"{client.user.avatar_url}")
            except:
              embed.set_thumbnail(url=f"{client.user.avatar_url}")
            await ctx.send(embed=embed, delete_after=20)
            # await ctx.send(f'```ini\nAdded {track.title} to the Queue\n```', delete_after=15)
            try:
              await player.queue.put(track)
            except:
              pass

        if not player.is_playing:
            await player.do_next()

    @commands.command()
    async def pause(self, ctx: commands.Context):
        """Pause the currently playing song."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if player.is_paused or not player.is_connected:
            return

        if self.is_privileged(ctx):
            embed=discord.Embed(description="**⏸ Paused**", color = discord.Color.blue())
            await ctx.send(embed=embed, delete_after=10)
            # await ctx.send('.', )
            player.pause_votes.clear()

            return await player.set_pause(True)

        required = self.required(ctx)
        player.pause_votes.add(ctx.author)

        if len(player.pause_votes) >= required:
            embed=discord.Embed(description="**⏸️ Vote Passed | Pausing**", color = discord.Color.blue())
            await ctx.send(embed=embed, delete_after=10)
            player.pause_votes.clear()
            await player.set_pause(True)
        else:
            embed=discord.Embed(description=f"**{ctx.author.mention} Has Voted To Pause**", color = discord.Color.blue())
            await ctx.send(embed=embed, delete_after=10)

    @commands.command()
    async def resume(self, ctx: commands.Context):
        """Resume a currently paused player."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_paused or not player.is_connected:
            return

        if self.is_privileged(ctx):
            embed=discord.Embed(description=f"**▶️ Resumed**", color = discord.Color.blue())
            await ctx.send(embed=embed, delete_after=10)
            player.resume_votes.clear()

            return await player.set_pause(False)

        required = self.required(ctx)
        player.resume_votes.add(ctx.author)

        if len(player.resume_votes) >= required:
            embed=discord.Embed(description="**▶️ Vote Passed | Resuming**", color = discord.Color.blue())
            await ctx.send(embed=embed, delete_after=10)
            player.resume_votes.clear()
            await player.set_pause(False)
        else:
            embed=discord.Embed(description=f"**{ctx.author.mention} Has Voted To Resume**", color = discord.Color.blue())
            await ctx.send(embed=embed, delete_after=10)

    @commands.command()
    # @commands.cooldown(1,3,commands.BucketType.guild)
    async def skip(self, ctx: commands.Context):
        """Skip the currently playing song."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_connected:
            return

        if self.is_privileged(ctx):
            embed=discord.Embed(description="**⏭ Skipped**", color = discord.Color.blue())
            await ctx.send(embed=embed, delete_after=10)
            player.skip_votes.clear()

            return await player.stop()

        if ctx.author == player.current.requester:
            embed=discord.Embed(description="**⏭ Skipped By Requestor**", color = discord.Color.blue())
            await ctx.send(embed=embed, delete_after=10)
            player.skip_votes.clear()

            return await player.stop()

        required = self.required(ctx)
        player.skip_votes.add(ctx.author)

        if len(player.skip_votes) >= required:
            embed=discord.Embed(description="**⏭ Vote Passed | Skipping**", color = discord.Color.blue())
            await ctx.send(embed=embed, delete_after=10)
            player.skip_votes.clear()
            await player.stop()
        else:
            embed=discord.Embed(description=f"**{ctx.author.mention} Has Voted To Skip**", color = discord.Color.blue())
            await ctx.send(embed=embed, delete_after=10)

    @commands.command()
    async def stop(self, ctx: commands.Context):
        """Stop the player and clear all internal states."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_connected:
            return

        if self.is_privileged(ctx):
            embed=discord.Embed(description="**🛑 Stopped**", color = discord.Color.orange())
            await ctx.send(embed=embed, delete_after=10)
            return await player.teardown()

        required = self.required(ctx)
        player.stop_votes.add(ctx.author)

        if len(player.stop_votes) >= required:
            embed=discord.Embed(description="**🛑 Vote Passed | Stopped**", color = discord.Color.orange())
            await ctx.send(embed=embed, delete_after=10)
            await player.teardown()
        else:
            embed=discord.Embed(description=f'**{ctx.author.mention} Has Voted To Stop**', color = discord.Color.orange())
            await ctx.send(embed=embed, delete_after=10)
            # await ctx.send(f'{ctx.author.mention} has voted to stop the player.', delete_after=15)

    @commands.command(aliases=['v', 'vol'])
    async def volume(self, ctx: commands.Context, *, vol: int):
        """Change the players volume, between 1 and 100."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_connected:
            return

        if not self.is_privileged(ctx):
            embed=discord.Embed(description="**Only DJ's Or Admins Can Control Volume**", color = discord.Color.teal())
            return await ctx.send(embed=embed, delete_after=10)

        if not 0 < vol < 101:
            embed=discord.Embed(description="**Please Enter A Number Between 1-100**", color = discord.Color.teal())
            return await ctx.send(embed=embed, delete_after=10)

        await player.set_volume(vol)
        embed=discord.Embed(description=f"**Volume Set To {vol}%**", color = discord.Color.teal())
        await ctx.send(embed=embed, delete_after=10)

    @commands.command(aliases=['mix'])
    async def shuffle(self, ctx: commands.Context):
        """Shuffle the players queue."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_connected:
            return

        if player.queue.qsize() < 3:
            embed=discord.Embed(description="**Add More Songs Before Shuffling**", color = discord.Color.teal())
            return await ctx.send(embed=embed, delete_after=10)

        if self.is_privileged(ctx):
            embed=discord.Embed(description="**🔀 Shuffled**", color = discord.Color.teal())
            await ctx.send(embed=embed, delete_after=10)
            player.shuffle_votes.clear()
            return random.shuffle(player.queue._queue)

        required = self.required(ctx)
        player.shuffle_votes.add(ctx.author)

        if len(player.shuffle_votes) >= required:
            embed=discord.Embed(description="**🔀 Vote Passed | Shuffled**", color = discord.Color.teal())
            await ctx.send(embed=embed, delete_after=10)
            player.shuffle_votes.clear()
            random.shuffle(player.queue._queue)
        else:
            embed=discord.Embed(description=f"**{ctx.author.mention} Has Voted To Shuffle**", color = discord.Color.teal())
            await ctx.send(embed=embed, delete_after=10)

    @commands.command(hidden=True)
    async def vol_up(self, ctx: commands.Context):
        """Command used for volume up button."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_connected or not self.is_privileged(ctx):
            return

        vol = int(math.ceil((player.volume + 10) / 10)) * 10

        if vol > 100:
            vol = 100
            embed=discord.Embed(description=f"**🔊 Maximum Volume Reached**", color = discord.Color.red())
            await ctx.send(embed=embed, delete_after=10)

        await player.set_volume(vol)

    @commands.command(hidden=True)
    async def vol_down(self, ctx: commands.Context):
        """Command used for volume down button."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_connected or not self.is_privileged(ctx):
            return

        vol = int(math.ceil((player.volume - 10) / 10)) * 10

        if vol <= 0:
            vol = 0
            embed=discord.Embed(description=f"**🔇 Player Is Muted**", color = discord.Color.red())
            await ctx.send(embed=embed, delete_after=10)

        await player.set_volume(vol)
    @commands.command(hidden=True)
    async def f_down(self, ctx: commands.Context):
        """Command used for volume down button."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_connected or not self.is_privileged(ctx):
            return

        position = player.position
        await player.seek(player.position-15000)
    @commands.command(aliases=["ff",'fastforward'])
    async def forward(self, ctx: commands.Context, amount:int=15):
      player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
      
      if not player.is_connected:
          return
      if not self.is_privileged(ctx):
          embed=discord.Embed(description=f"**Only A DJ Or Admin Can Use This Command**", color = discord.Color.red())
          return await ctx.send(embed=embed, delete_after=10)
      # if amount==None:
      #   await player.seek(0)
      #   embed=discord.Embed(title=f"⏺ Rewinding".title(), color = discord.Color.teal())
      #   return await ctx.send(embed=embed, delete_after=10)
        
      if not isinstance(int(amount), int):
        # await ctx.send("> Please Type A Number Representing The Seconds.")
        embed=discord.Embed(title="Please Type A Number".title(), color = discord.Color.red())
        return await ctx.send(embed=embed, delete_after=10)
      # try:
      #   if int(timestamp)>int(player.current.length/100):
      #     embed=discord.Embed(title="You Cannot Seek To A Time Stamp Greater Than The Songs Length".title(), color = discord.Color.red())
      #     return await ctx.send(embed=embed, delete_after=10)
      # except:
      #   return
      
      await player.seek(player.position+amount*1000)
      embed=discord.Embed(description=f"**⏩ {amount} Seconds**".title(), color = discord.Color.green())
      return await ctx.send(embed=embed, delete_after=10)



    @commands.command(hidden=True)
    async def f_up(self, ctx: commands.Context):
        """Command used for volume down button."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_connected or not self.is_privileged(ctx):
            return

        position = player.position
        await player.seek(player.position+15000)
        # if position+15000 > track.le:
        #     vol = 0
        #     embed=discord.Embed(description=f"**🔇 Player Is Muted**", color = discord.Color.red())
        #     await ctx.send(embed=embed, delete_after=10)

        # await player.set_volume(vol)

    @commands.command(aliases=['eq'])
    async def equalizer(self, ctx: commands.Context, *, equalizer: str):
        """Change the players equalizer."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_connected:
            return

        if not self.is_privileged(ctx):
            embed=discord.Embed(description=f"**Only A DJ Or Admin Can Can Change EQ**", color = discord.Color.red())
            return await ctx.send(embed=embed, delete_after=10)

        eqs = {'flat': wavelink.Equalizer.flat(),
               'boost': wavelink.Equalizer.boost(),
               'metal': wavelink.Equalizer.metal(),
               'piano': wavelink.Equalizer.piano()}

        eq = eqs.get(equalizer.lower(), None)

        if not eq:
            joined = "\n".join(eqs.keys())
            embed=discord.Embed(description=f"**Valid EQ's:\n\n{joined}**", color = discord.Color.teal())
            return await ctx.send(embed=embed, delete_after=10)
            # return await ctx.send(f'Invalid EQ provided. Valid EQs:\n\n{joined}')

        embed=discord.Embed(description=f"**EQ Set To {equalizer}**", color = discord.Color.teal())
        await ctx.send(embed=embed, delete_after=10)
        await player.set_eq(eq)

    @commands.command(aliases=['q', 'que'])
    @commands.cooldown(1,3,commands.BucketType.user)
    async def queue(self, ctx: commands.Context,*, song=None):
        """Display the players queued songs."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
        if song!=None:
          return await self.play(ctx, query=song)
        if not player.is_connected:
            return

        if player.queue.qsize() == 0:
            embed=discord.Embed(description=f"**✋ Add More Songs Before Using The Queue Command**", color = discord.Color.orange())
            return await ctx.send(embed=embed, delete_after=10)
        entries=[]
        for i in range(len(player.queue._queue)):
          entries.append(f" `{i+1}.`**   [{player.queue._queue[i].title}]({player.queue._queue[i].uri})**")
        # entries = [track.title for track in player.queue._queue]
        pages = PaginatorSource(entries=entries)
        paginator = menus.MenuPages(source=pages, timeout=None, delete_message_after=True)

        await paginator.start(ctx)
    @commands.command()
    @commands.cooldown(1,8,commands.BucketType.user)
    async def question_controller(self, ctx: commands.Context):
      embed=discord.Embed(description=f"**⏯ -> ` Pause/Play `\n\n⏪ -> ` Back 15 Seconds `\n\n⏩ -> ` Forward 15 Seconds `\n\n⏭ -> ` Skip To Next Song `\n\n⏺ -> ` Rewind Song `\n\n🔀 -> ` Shuffle Queue `\n\n🔊 -> ` Sound Up `\n\n🔉 -> ` Sound Down `\n\n🎸 -> ` Shows Queue `\n\n🛑 -> ` Stops Player `\n\n🔃 -> ` Updates Controller `\n\n🔂 -> ` Loops The Current Song `\n\n⁉ -> ` Shows This Message `**", color = discord.Color.orange())
      return await ctx.send(embed=embed, delete_after=10)
    @commands.command(aliases=['np', 'now_playing', 'current', 'playing'])
    async def nowplaying(self, ctx: commands.Context):
        """Update the player controller."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
        if not player.is_playing:
            return
        if not player.is_connected:
            return

        await player.invoke_controller()
    @commands.command()
    async def clearqueue(self, ctx: commands.Context):
      player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
      
      if not player.is_connected:
          return
      if not self.is_privileged(ctx):
          embed=discord.Embed(description=f"**Only A DJ Or Admin Can Use This Command**", color = discord.Color.red())
          return await ctx.send(embed=embed, delete_after=10)
      player.queue._queue.clear()
      embed=discord.Embed(description=f"**💣 Cleared**", color = discord.Color.teal())
      return await ctx.send(embed=embed, delete_after=10)



    @commands.command(aliases=['skipto'])
    async def st(self, ctx: commands.Context, index=None):
      player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
      
      if not player.is_connected:
          return
      if not self.is_privileged(ctx):
          embed=discord.Embed(description=f"**Only A DJ Or Admin Can Use This Command**", color = discord.Color.red())
          return await ctx.send(embed=embed, delete_after=10)
      if index==None:
 
        embed=discord.Embed(description=f"**Type A Track Number To Skip To**".title(), color = discord.Color.teal())
        return await ctx.send(embed=embed, delete_after=10)
        
      if not isinstance(int(index), int):

        embed=discord.Embed(description="**Please Type A Number**".title(), color = discord.Color.red())
        return await ctx.send(embed=embed, delete_after=10)
      try:
        if int(index)-1>len(player.queue._queue) or int(index)-1<0:
          embed=discord.Embed(description="**That Track Number Is Not In The Queue**".title(), color = discord.Color.red())
          return await ctx.send(embed=embed, delete_after=10)
      except:
        return
      queueSave=[]
      for i in range(int(index)):
        await player.stop()
        await player.do_next()
      # player.queue._queue=queueSave

      # for i in range(len(player.queue._queue)):
      #   if i == index:
      #     break
      #   else:
      #     player.queue._queue.remove(i)
      embed=discord.Embed(description=f"**⏭ Skipped To {index}**".title(), color = discord.Color.teal())
      # await player.stop()
      return await ctx.send(embed=embed, delete_after=10)



    @commands.command(aliases=['loopsong','ls'])
    async def loop(self, ctx: commands.Context):
      player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
      
      if not player.is_connected:
          return
      if not self.is_privileged(ctx):
          embed=discord.Embed(description=f"**Only A DJ Or Admin Can Use This Command**", color = discord.Color.red())
          return await ctx.send(embed=embed, delete_after=10)

      
      player.loopSong = not player.loopSong
      if player.loopSong==True:
        await player.queue.put(player.current)
      embed=discord.Embed(description=f"**🔂 Looping Set To **"+str(player.loopSong).title(), color = discord.Color.teal())
      return await ctx.send(embed=embed, delete_after=10)




    @commands.command(aliases=['seek','moveto', 'rewind'])
    async def move(self, ctx: commands.Context, timestamp=None):
      player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)
      
      if not player.is_connected:
          return
      if not self.is_privileged(ctx):
          embed=discord.Embed(description=f"**Only A DJ Or Admin Can Use This Command**", color = discord.Color.red())
          return await ctx.send(embed=embed, delete_after=10)
      if timestamp==None:
        await player.seek(0)
        embed=discord.Embed(description=f"**⏺ Rewinding**".title(), color = discord.Color.teal())
        return await ctx.send(embed=embed, delete_after=10)
        
      if not isinstance(int(timestamp), int):
        # await ctx.send("> Please Type A Number Representing The Seconds.")
        embed=discord.Embed(description="**Please Type A Number**".title(), color = discord.Color.red())
        return await ctx.send(embed=embed, delete_after=10)
      try:
        if int(timestamp)>int(player.current.length/100):
          embed=discord.Embed(description="**You Cannot Seek To A Time Stamp Greater Than The Songs Length**".title(), color = discord.Color.red())
          return await ctx.send(embed=embed, delete_after=10)
      except:
        return
      
      await player.seek(int(timestamp)*1000)
      embed=discord.Embed(description=f"**⏩ Moved To {timestamp}**".title(), color = discord.Color.teal())
      return await ctx.send(embed=embed, delete_after=10)


    @commands.command(aliases=['swap'])
    async def swap_dj(self, ctx: commands.Context, *, member: discord.Member = None):
        """Swap the current DJ to another member in the voice channel."""
        player: Player = self.bot.wavelink.get_player(guild_id=ctx.guild.id, cls=Player, context=ctx)

        if not player.is_connected:
            return

        if not self.is_privileged(ctx):
            embed=discord.Embed(description=f"**Only A DJ Or Admin Can Use This Command**", color = discord.Color.red())
            return await ctx.send(embed=embed, delete_after=10)

        members = self.bot.get_channel(int(player.channel_id)).members

        if member and member not in members:
            embed=discord.Embed(description=f"**{member.mention} Is Not In This Voice Channel**", color = discord.Color.red())
            return await ctx.send(embed=embed, delete_after=10)

        if member and member == player.dj:
            embed=discord.Embed(description=f"**{member.mention} Is already A DJ or Admin**", color = discord.Color.red())
            return await ctx.send(embed=embed, delete_after=10)

        if len(members) <= 2:
            embed=discord.Embed(description=f"**No More Members To Swap To**", color = discord.Color.red())
            return await ctx.send(embed=embed, delete_after=10)

        if member:
            player.dj = member
            embed=discord.Embed(description=f"**🎸 {member.mention} Is Now The DJ**", color = discord.Color.red())
            return await ctx.send(embed=embed, delete_after=10)

        for m in members:
            if m == player.dj or m.bot:
                continue
            else:
                player.dj = m
                embed=discord.Embed(description=f"**🎸 {member.mention} Is Now The DJ**", color = discord.Color.red())
                return await ctx.send(embed=embed, delete_after=10)







# class Music(commands.Cog):

#     def __init__(self, client):
#         self.client = client

#         if not hasattr(client, 'wavelink'):
#             self.client.wavelink = wavelink.Client(bot=self.client)

#         self.client.loop.create_task(self.start_nodes())

#     async def start_nodes(self):
#         await self.client.wait_until_ready()

#         # Initiate our nodes. For this example we will use one server.
#         # Region should be a discord.py guild.region e.g sydney or us_central (Though this is not technically required)
#         await self.client.wavelink.initiate_node(host='0.0.0.0',
#                                               port=2333,
#                                               rest_uri='http://0.0.0.0:2333',
#                                               password='youshallnotpass',
#                                               identifier='TEST',
#                                               region='us_central')

#     @commands.command(name='connectLava')
#     async def connect_(self, ctx, *, channel: discord.VoiceChannel=None):
#         if not channel:
#             try:
#                 channel = ctx.author.voice.channel
#             except AttributeError:
#                 raise discord.DiscordException('No channel to join. Please either specify a valid channel or join one.')

#         player = self.client.wavelink.get_player(ctx.guild.id)
#         await ctx.send(f'Connecting to **`{channel.name}`**')
#         await player.connect(channel.id)

#     @commands.command()
#     async def playLava(self, ctx, *, query: str):
#         tracks = await self.client.wavelink.get_tracks(f'ytsearch:{query}', retry_on_failure=True)

#         if not tracks:
#             return await ctx.send('Could not find any songs with that query.')

#         player = self.client.wavelink.get_player(ctx.guild.id)
#         if not player.is_connected:
#             await ctx.invoke(self.connect_)

#         await ctx.send(f'Added {str(tracks[0])} to the queue.')
#         print(tracks[0])
#         server=ctx.guild.id

#         await player.play(tracks[0])







async def level(server, member):
  lvl=-1
  exp=-1
  userLevelInfo = {"id" : str(member), "exp" : 5, "lvl": 1}
  with open("userJson.json","r") as f:
    users = json.load(f)
  if str(server) in users:
    state=False
    for element in users[str(server)]:
      if element["id"]==str(member):
        index = users[str(server)].index(element)
        state=True
    if state:
      # users[str(server)][index]["exp"]+=5
      #Check If Pass Level
      exp= users[str(server)][index]["exp"]
      lvl= users[str(server)][index]["lvl"]
      # lvl_end = int(users[str(server)][index]["exp"] ** (1/4))
      # if lvl_start<lvl_end:
      #   users[str(server)][index]["lvl"]=lvl_end
      #   lvl = lvl_end
      # print(lvl_start)
      # print(lvl_start)
      # print(lvl)
    else:
      users[str(server)].append(userLevelInfo)
      exp= userLevelInfo["exp"]
      lvl= userLevelInfo["lvl"]
  else:
    users[str(server)]= {}
    users[str(server)]=[]
    users[str(server)].append(userLevelInfo)
    exp= userLevelInfo["exp"]
    lvl= userLevelInfo["lvl"]
  with open("userJson.json","w") as f:
    json.dump(users,f)
  return exp, lvl


# async def addExp( member):
#   lvl=-1
#   with open("userJson.json","r") as f:
#     users = json.load(f)
#   if str(member) in users:
#     users[str(member)]["exp"]+=5
#     lvl_start= users[str(member)]["lvl"]
#     lvl_end = int(users[str(member)]["exp"] ** (1/4))
#     if lvl_start<lvl_end:
#       users[str(member)]["lvl"]=lvl_end
#       lvl = lvl_end
#   else:
#     userLevelInfo = {"id" : str(member), "exp" : 0, "level": 1}
#     users[str(member)]= {}
#     users[str(member)]["exp"]=5
#     users[str(member)]["lvl"]=1
#   with open("userJson.json","w") as f:
#     json.dump(users,f)
#   return lvl

async def addExp(server, member):
  lvl=-1
  userLevelInfo = {"id" : str(member), "exp" : 5, "lvl": 1}
  with open("userJson.json","r") as f:
    users = json.load(f)
  if str(server) in users:
    state=False
    for element in users[str(server)]:
      if element["id"]==str(member):
        index = users[str(server)].index(element)
        state=True
    if state:
      users[str(server)][index]["exp"]+=5
      #Check If Pass Level
      lvl_start= users[str(server)][index]["lvl"]
      lvl_end = int(users[str(server)][index]["exp"] ** (1/4))
      if lvl_start<lvl_end:
        users[str(server)][index]["lvl"]=lvl_end
        lvl = lvl_end
      # print(lvl_start)
      # print(lvl_start)
      # print(lvl)
    else:
      users[str(server)].append(userLevelInfo)
  else:
    users[str(server)]= {}
    users[str(server)]=[]
    users[str(server)].append(userLevelInfo)
  with open("userJson.json","w") as f:
    json.dump(users,f)
  return lvl

async def check(ctx):
  # define the voice channel
  vc=None
  try:
    vc = ctx.guild.voice_client 
    member_count=0
    for element in vc.channel.members:
      if not element.bot:
        member_count+=1


    # member_count = len(vc.channel.members)
    print("VC LENGTH MEMBERS"+str(len(vc.channel.members)))
    if member_count == 0:
      # if len(vc.channel.members)<1:
      #   # await asyncio.sleep(1)
      #   if len(vc.channel.members)<1:
      #     # try:
      #     #   voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
      #     # except:
      #     #   return
      await vc.disconnect()
      embed=discord.Embed(title="✋ Astro Has Disconnected From The Voice Channel. Astro Automatically Disconnects After Inactivity!".title(), color = discord.Color.orange())
      await ctx.channel.send(embed=embed)
      await clear(ctx)
    # leave the channel
  except Exception as e :
    if vc==None:
      await clear(ctx)

async def clear(ctx):
  server=ctx.guild.id
  with open("queue.json","r") as f:
    users = json.load(f)
  if str(server) in users:
    users[str(server)]["queue"].clear()
    users[str(server)]["name"].clear()
    users[str(server)]["duration"].clear()
    users[str(server)]["thumbnail"].clear()
    users[str(server)]["link"].clear()
    users[str(server)]["requestor"].clear()
  else:
    users[str(server)]= {}
    users[str(server)]["queue"]=[]
    users[str(server)]["name"]=[]
    users[str(server)]["duration"]=[]
    users[str(server)]["thumbnail"]=[]
    users[str(server)]["link"]=[]
    users[str(server)]["requestor"]=[]
  with open("queue.json","w") as f:
    json.dump(users,f)



  with open("playing.json","r") as f:
    users = json.load(f)
  if str(server) in users:
    users[str(server)]["song"]=None
    users[str(server)]["link"]=None
    users[str(server)]["duration"]=None
    users[str(server)]["thumbnail"]=None
    users[str(server)]["weburl"]=None
    users[str(server)]["requestor"]=None
  else:
    users[str(server)]= {}
    users[str(server)]["song"]=None
    users[str(server)]["link"]=None
    users[str(server)]["duration"]=None
    users[str(server)]["thumbnail"]=None
    users[str(server)]["weburl"]=None
    users[str(server)]["requestor"]=None
  with open("playing.json","w") as f:
    json.dump(users,f)
  
  with open("previous.json","r") as f:
    users = json.load(f)
  if str(server) in users:

    users[str(server)]["previous"].clear()
    users[str(server)]["names"].clear()
    users[str(server)]["durations"].clear()
    users[str(server)]["thumbnails"].clear()
    users[str(server)]["links"].clear()
    users[str(server)]["requestors"].clear()
      
  else:
    users[str(server)]= {}
    users[str(server)]["previous"]=[]
    users[str(server)]["names"]=[]
    users[str(server)]["durations"]=[]
    users[str(server)]["thumbnails"]=[]
    users[str(server)]["links"]=[]
    users[str(server)]["requestors"]=[]
    



# client.loop.create_task(check(ctx))


import json
@client.event
async def on_message(msg):
  # msg.content=msg.content.lower()
  # await update_db(msg.guild.id)
  # print(msg.content)
  if msg.content == "<@!809609861456723988>":
    # with open('prefixes.json', 'r') as f: #read the prefix.json file
    #   prefixes = json.load(f) #load the json file
    prefixes=db["prefixes"]

    prefix= prefixes[str(msg.guild.id)]
    embed=discord.Embed(title="My Current Prefix Here Is  ` "+prefix+" ` ".title(), color = discord.Color.orange())
    await msg.channel.send(embed=embed)

    # prefixes[str(guild.id)] = ['.']#default prefix

    # with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
    #   json.dump(prefixes, f, indent=4) #the indent is to
  if msg.author.bot:

    await check(msg)
    return
  await check(msg)
  
  try:
  #   try:
  #     server = msg.guild
  #     vc = server.voice_client     # vc = client.user.voice.channel
  #     # voice_client = ctx.message.guild.voice_client
  #     # vc = discord.utils.get(client.voice_clients, guild=msg.guild)
  #     # print("VC LENGTH MEMBERS"+str(len(vc.channel.members)))
  #     if len(vc.channel.members)<2:
  #       await asyncio.sleep(120)
  #       if len(vc.channel.members)<2:
  #         try:
  #           voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  #         except:
  #           return
  #         await vc.disconnect()
  #         embed=discord.Embed(title="✋ Astro Has Disconnected From The Voice Channel. Astro Automatically Disconnects After Two Minutes Of Inactivity!".title(), color = discord.Color.orange())
  #         await msg.channel.send(embed=embed)
  #   except Exception as e:
  #     print(e)
      
    # await bot_dashboard.process_request(msg)
    # if msg.author.id != client.user.id:
    #   await checkAmounts()
    #   lvl = await addExp(msg.guild.id, msg.author.id)
    #   # print(lvl)
    #   if lvl>0:
    #     print(lvl)
    #     await msg.channel.send("> Congrats "+msg.author.mention+" You Just Leveled Up To Level " +str(lvl)+"!")

    # with open("mutedUsers.json","r") as f:
    #   users = json.load(f)

  
    # try:
    #   for server in users[str(msg.author.id)]["mute"]:
    #     if server==msg.guild.id:
    #       embed = discord.Embed(title="My Apologies "+msg.author.name+" You Have Been Muted.", colour=discord.Color.gold(), timestamp=datetime.utcnow())
    #       embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    #       embed.set_thumbnail(url=f"{client.user.avatar_url}")

    #       embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
    #       embed.add_field(name="You Have Been Muted By A Mod, Thus You Cannot Speak.", value="Talk To A Mod For More Info", inline=False)
    #       try:
    #         await msg.author.send(embed=embed)
    #       except:
    #         pass
    #       await msg.delete()
    #       return
    # except:
    #   pass
    # with open("mutedUsers.json","w") as f:
    #   json.dump(users,f)
    
    # if msg.author.id==503649934625472544:
    #   return
    #   try:
    #     pass
    #     # await msg.channel.send("😐")
    #   except:
    #     pass
    #     # await msg.delete
    #     return

    # if "lol" in msg.content.lower() or "lmao" in msg.content.lower() or "lmfao" in msg.content.lower():

    words=[]
    # db["mod_words"]={
    
    # }
    users = db["mod_words"]

    if str(msg.guild.id) not in users:
      users[str(msg.guild.id)]={}
      users[str(msg.guild.id)]["words"]=[]
    # with open("swearWords.json","r") as f:
    #   users = json.load(f)
    try:
      for word in users[str(msg.guild.id)]["words"]:
        if word.lower() in msg.content.lower():
          words.append(word)
    except:
      pass
    
    if len(words)>0:
      embed = discord.Embed(title=f"👋 Hi, The Message You Just Sent In {msg.guild.name} Contained A Moderated Word", description=" ` Please Do Not Do this Again, As Your Message Will Once Again Be Deleted `", colour=discord.Color.orange(), timestamp=datetime.utcnow())
      # embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

      # embed.set_thumbnail(url=f"{client.user.avatar_url}")

      # embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")

      # for element in words:
      #   embed.add_field(name=f"Your Message In {msg.guild.name} contained:", value="` "+element.title()+" `", inline=False)
      # embed.add_field(name="Astro is hoping to make chats and channels a safer and better place for all!", value=f"Learn more at ({website})", inline=False)
      # wordslist=""
      # i=0
      # try:
      #   for element in users[str(msg.guild.id)]["words"]:
      #     i=i+1
      #     if i==len(users[str(msg.guild.id)]["words"]):
      #       wordslist = wordslist +element.title()
      #     else:
      #       wordslist = wordslist +element.title()+", "
      # except:
      #   pass
      # embed.add_field(name="Refraining from using the words below, as messages containing any of these words will be automatically deleted.", value=wordslist, inline=False)

      # await ctx.send(embed=embed)
      # profaneAmount=0
      # import profanity
      # for element in words:
      #   if profanity.contains_profanity(element):
      #     profaneAmount+=1;
      
      # if profaneAmount>0:
      #   if profanity.contains_profanity(msg.content):
      #     try:
      #       await msg.author.send(embed=embed)
      #     except:
      #       pass
      #     await msg.delete()
      # else:
      #   try:
      #     await msg.author.send(embed=embed)
      #   except:
      #     pass
      #   await msg.delete()


      
      try:
        await msg.author.send(embed=embed)
      except:
        pass
      # await msg.author.send("Hello, In an effort to create a less toxic environment, Astro is moderating words that are deemed explicit or innapropriate by the server. Please know that this is meant to detoxify an environment!")
      await msg.delete()
      return
    # syls = syllables.estimate(msg.content)
    try:

      verse = Pyverse(msg.content)
      # print(str(verse.count))
      syls= verse.count
      # await msg.channel.send(my_haiku)
      # print(msg.content)
      # print(syls)
      if "astro" in msg.content.lower() and "ty" in msg.content.lower():
        await msg.add_reaction("🚀")
        await msg.add_reaction("🤍")
      if "astro" in msg.content.lower() and "thank" in msg.content.lower():
        await msg.add_reaction("🚀")
        await msg.add_reaction("🤍")
      # if "aryah" in msg.content.lower() or "dhruv" in msg.content.lower() or "aoztanir" in msg.content.lower() or "driftrs" in msg.content.lower():
      #   # await msg.add_reaction("🚀")
      #   await msg.add_reaction("🚀")
      if syls == 17:
        pass
        # await msg.channel.send("> Nice Haiku "+msg.author.mention+"!")
    except:
      pass
  except Exception as e:
    print(e)
  await client.process_commands(msg)




import discord
from discord.ext import commands
import random


player1 = ""
player2 = ""
turn = ""
gameover1 = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command(aliases=['dash'])
async def dashboard(ctx, *, prefixNew:str=None):
  embed=discord.Embed(description=f"**🚀 Check Out This Server's [Dashboard]( {website}/guild/{ctx.guild.id} )**", color = discord.Color.orange())
  await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, *, prefixNew:str=None):
  # with open('prefixes.json', 'r') as f: #read the prefix.json file
  #   prefixes = json.load(f) #load the json file
  prefixes=db["prefixes"]
  if prefixNew==None:
    prefix=prefixes[str(ctx.guild.id)]
    embed=discord.Embed(title="My Current Prefix Here Is  ` "+prefix+" ` ".title(), color = discord.Color.orange())
    await ctx.send(embed=embed)
    return
  prefixes[str(ctx.guild.id)] = prefixNew
  db["prefixes"]=prefixes
  # with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
  #   json.dump(prefixes, f, indent=4) #the indent is to
  prefix= prefixes[str(ctx.guild.id)]
  embed=discord.Embed(title="My Prefix Is Now  ` "+prefix+" ` ".title(), color = discord.Color.orange())
  await ctx.send(embed=embed)


@client.command(aliases=['muted'])
async def listmute(ctx):
  role = discord.utils.get(ctx.guild.roles, name="astroMuted")
  # if role is None:
  #   await ctx.send('There is no "mod" role on this server!')
  #   return
  mutedMembs = []

  for member in ctx.guild.members:
    if role in member.roles:
      # await bot.say("{0.name}: {0.id}".format(member))
      mutedMembs.append(member)
      empty = False

  # with open("mutedUsers.json","r") as f:
  #   users = json.load(f)
  embed = discord.Embed(title="Muted Users In "+ctx.guild.name+":", colour=discord.Color.orange())
  # embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  # embed.set_thumbnail(url=f"{ctx.guild.icon_url}")

  # embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")

  for member in mutedMembs:
    embed.add_field(name=member.name, value="Status: ` Mute `", inline=False)
  # try:
  #   for userobj in users:
  #     for server in users[str(userobj)]["mute"]:
  #       if server==ctx.guild.id:
  #         user = await client.fetch_user(int(userobj))
  #         embed.add_field(name=user.name, value="Status: Mute", inline=False)
  # except:
  #   pass
  await ctx.send(embed=embed)


# cluster = MongoClient("mongodb+srv://astro:astro@cluster0.alu7p.mongodb.net/test")
# mongodb = cluster["AstroData"]

async def update_db(server=None):
  # mongoQueue=mongodb["queue"]
  # db["reaction_roles"]={}
  while True:
    for i in  range(len(db["announcement"])):
      try:
        # print(str(db["announcement"][i]))
        announcement=dict(db["announcement"][i])
        server=announcement['server']
        title=announcement['title']
        description=announcement['description']
        pic=announcement['pic']
        name=announcement['name']
        channel=announcement['channel']
        role=announcement['role']
        fields=announcement['fields']
        color=announcement['color']
        sixteenIntegerHex = int(color, 16)
        readableHex = int(hex(sixteenIntegerHex), 0)
        if str(title.strip(" "))=="":
          title="~"
        if str(description.strip(" "))=="":
          description="~"
        for serverText in client.guilds:
          if serverText.id == int(server):
            for channelText in serverText.channels:
              if channelText.name.lower()==channel.lower() and channelText.type == discord.ChannelType.text:
                print("SENDING")
                embed=discord.Embed(title=str(title),description=str(description), color=readableHex)
                embed.set_author(name=name, icon_url=pic)
                for element in fields:
                  if str(element['title'].strip(" "))=="":
                    element['title']="~"
                  if str(element['value'].strip(" "))=="":
                    element['value']="~"
                  embed.add_field(name=str(element['title']), value=str(element['value']), inline=False)
                if (role!="None"):
                  rolePing=discord.utils.get(serverText.roles,name=str(role))
                  if (role=="@everyone"):
                    await channelText.send("@everyone")
                  else:
                    await channelText.send(rolePing.mention)
                await channelText.send(embed=embed)
                db["announcement"].pop(i)
                break
      except Exception as e:
        print(e)
        db["announcement"].pop(i)







    for globServer in db["reaction_roles"]:
      for i in range(len(db["reaction_roles"][str(globServer)])):
        REACTION_OBJ = db["reaction_roles"][str(globServer)]
        if REACTION_OBJ[i]["sent"]==False:
          try:
            # print(str(db["announcement"][i]))
            announcement=dict(db["reaction_roles"][str(globServer)][i])
            server=announcement['server']
            title=announcement['title']
            description=announcement['description']
            pic=announcement['pic']
            name=announcement['name']
            channel=announcement['channel']
            role=announcement['role']
            fields=announcement['fields']
            roleAdds=announcement['roleAdds']
            color=announcement['color']
            sixteenIntegerHex = int(color, 16)
            readableHex = int(hex(sixteenIntegerHex), 0)
            if str(title.strip(" "))=="":
              title="~"
            if str(description.strip(" "))=="":
              description="~"
            for serverText in client.guilds:
              if serverText.id == int(server):
                for channelText in serverText.channels:
                  if channelText.name.lower()==channel.lower() and channelText.type == discord.ChannelType.text:
                    print("SENDING")
                    embed=discord.Embed(title=str(title),description=str(description), color=readableHex)
                    embed.set_author(name=name, icon_url=pic)
                    for element in fields:
                      if str(element['title'].strip(" "))=="":
                        element['title']="~"
                      if str(element['value'].strip(" "))=="":
                        element['value']="~"
                      embed.add_field(name=str(element['title']), value=str(element['value']), inline=False)
                    if (role!="None"):
                      rolePing=discord.utils.get(serverText.roles,name=str(role))
                      if (role=="@everyone"):
                        await channelText.send("@everyone")
                      else:
                        await channelText.send(rolePing.mention)
                    msgSent =await channelText.send(embed=embed)
                    for element in roleAdds:
                      await msgSent.add_reaction(element["emoji"])
                    db["reaction_roles"][str(globServer)][i]["sent"]=True
                    db["reaction_roles"][str(globServer)][i]["id"]=msgSent.id
                    break
          except Exception as e:
            print(e)
          # db["reaction_roles"][str(globServer)].pop(i)
        
    # for server in client.guilds: 
    #   # Spin through every server
    #   for channel in server.channels: 
    #     # Channels on the server
    #     if channel.permissions_for(server.me).send_messages:
    #       try:
    #         await channel.send("> Astro Has Just gotten Twice The Ram, Look Forward To A Boost In Processing Power!\n-Team Astro")
    #         # So that we don't send to every channel:
    #       except:
    #         pass
    #       else:
    #         break
    try:
      ###QUEUE
      with open("queue.json","r") as f:
        users = json.load(f)
      # for i in range(len(users[str(server)]["duration"])):
      #   users[str(server)]["duration"][i]=int(users[str(server)]["duration"][i])
      db["queue"]=users
      mongoQueue.replace_one(users, users)
      # print(db["queue"][str(server)]["queue"][0])


      ###CURRENTLY PLAYING
      with open("playing.json","r") as f:
        users = json.load(f)
      db["playing"]=users
      # print(db["playing"][str(server)]["song"])


      ###PREVIOUSLY PLAYING
      with open("previous.json","r") as f:
        users = json.load(f)
      db["previous"]=users

      ###VOLUMES
      with open("volumes.json","r") as f:
        users = json.load(f)
      db["volumes"]=users
      # print(db["volumes"][str(server)]["volume"])
    except Exception  as e:
      print(e)
    # print("UPDATED DB SUCCESFULLY")
    await asyncio.sleep(2)

  # print(str(a[str(server)]["queue"]))

# client.loop.create_task(update_db())


@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, memb: discord.Member,*, reason:str =None):
  if reason == None:
    reason="Unspecified"
  if memb.guild_permissions.administrator:
    await ctx.send("> Mods Cannot Mute/Unmute or Unmute Mods/Admins.")
    return
  if (ctx.guild.owner == memb):
    await ctx.send("> You Cannot Mute/Unmute A Mod/Admin Or An Owner.")
    return
  role = discord.utils.get(ctx.guild.roles, name='astroMuted')
  await memb.remove_roles(role)
  embed=discord.Embed(title=f"Reason: ` {reason} `", color=discord.Color.orange())
  embed.set_author(name=memb.name+" Has Been Unmuted!", icon_url=memb.avatar_url)
  await ctx.send(embed=embed)
  # print("hi")
  # if time != None:
  #   print("time used")
  #   seconds = 0
  #   try:
  #     if time.lower().endswith("d"):
  #         seconds += int(time[:-1]) * 60 * 60 * 24
  #         counter = f"{seconds // 60 // 60 // 24} days"
  #     if time.lower().endswith("h"):
  #         seconds += int(time[:-1]) * 60 * 60
  #         counter = f"{seconds // 60 // 60} hours"
  #     elif time.lower().endswith("m"):
  #         seconds += int(time[:-1]) * 60
  #         counter = f"{seconds // 60} minutes"
  #     elif time.lower().endswith("s"):
  #         seconds += int(time[:-1])
  #         counter = f"{seconds} seconds"
  #   except:
  #     return
  #   await ctx.send("> "+memb.mention+" Is Unmuted For "+counter.title()+" By "+ctx.author.mention)
  #   await unMute_person(memb, ctx.guild.id)
  #   print(seconds)
  #   await asyncio.sleep(seconds)
  #   print(seconds)
  #   await unMute_person(memb, ctx.guild.id)
  #   await ctx.send("> "+memb.mention+" Has Been Muted Once Again.")
  #   return
  # print("unmuted")
  # print(ctx.guild.id)
  # await unMute_person(memb, ctx.guild.id)
  # await ctx.send("> "+memb.mention+" Has Been Unmuted By "+ctx.author.mention)
  # # await ctx.send("muted")




@client.command(aliases=['silence'])
@commands.has_permissions(administrator=True)
async def mute(ctx, memb: discord.Member,*, reason :str =None):
  member=memb
  if reason==None:
    reason="Unspecified"
  if (ctx.guild.owner == memb):
    await ctx.send("> You Cannot Mute/Unmute A Mod/Admin Or An Owner.")
    return
  if memb.guild_permissions.administrator:
    await ctx.send("> "+"Mods Cannot Mute Mods/Admins.")
    return
  role = discord.utils.get(ctx.guild.roles, name='astroMuted')
  # try:
  if not role:
    role = await ctx.guild.create_role(name="astroMuted")

    for channel in ctx.guild.channels:
      await channel.set_permissions(role, speak=False, send_messages=False)
  await memb.add_roles(role)
  # except:
  #   pass
    # role = discord.utils.get(ctx.guild.roles, name='MutedAstro')
    # await memb.add_roles(role)
  
  embed=discord.Embed(title=f"Reason: ` {reason} `", color=discord.Color.orange())
  embed.set_author(name=memb.name+" Has Been Muted!", icon_url=memb.avatar_url)
  await ctx.send(embed=embed)
  # print("hi")
  # if time != None:
  #   print("time used")
  #   seconds = 0
  #   try:
  #     if time.lower().endswith("d"):
  #         seconds += int(time[:-1]) * 60 * 60 * 24
  #         counter = f"{seconds // 60 // 60 // 24} days"
  #     if time.lower().endswith("h"):
  #         seconds += int(time[:-1]) * 60 * 60
  #         counter = f"{seconds // 60 // 60} hours"
  #     elif time.lower().endswith("m"):
  #         seconds += int(time[:-1]) * 60
  #         counter = f"{seconds // 60} minutes"
  #     elif time.lower().endswith("s"):
  #         seconds += int(time[:-1])
  #         counter = f"{seconds} seconds"
  #   except:
  #     return
  #   await ctx.send("> "+memb.mention+" Has Been Muted By "+ctx.author.mention+" For "+counter.title())
  #   await mute_person(memb, ctx.guild.id)
  #   print(seconds)
  #   await asyncio.sleep(seconds)
  #   print(seconds)
  #   await unMute_person(memb, ctx.guild.id)
  #   await ctx.send("> "+memb.mention+" Has Been Unmuted And Can Speak Now Because The Mute Countdown Has Elapsed.")
  #   return
  # print("muted")
  # print(ctx.guild.id)
  # await mute_person(memb, ctx.guild.id)
  # await ctx.send("> "+memb.mention+" Has Been Muted By "+ctx.author.mention)
  # await ctx.send("muted")


  


@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameover1

    if gameover1:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameover1 = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("> A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameover1

    if not gameover1:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)

                if gameover1 == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameover1 = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameover1
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameover1 = True

@client.command(aliases=['cleartictactoe','stoptictatoe','stoptictactoegame'])
async def endtictactoegame(ctx):
  global gameover1
  gameover1 = True
  await ctx.send("Game ended!")

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


client.remove_command("help")
# from pretty_help import DefaultMenu, PrettyHelp
# ending_note = f"hi"
# menu = DefaultMenu(page_left="👍", page_right="👎",remove="❌", active_time=5)
# client.help_command = PrettyHelp(menu=menu, ending_note=ending_note)

# @slash.slash(name="test")
# async def _test(ctx: SlashContext):
#     embed = discord.Embed(title="embed test")
#     await ctx.send(content="test", embeds=[embed])

@client.command()
async def help(ctx, *, commandType :str =None):
  # with open('prefixes.json', 'r') as f: #read the prefix.json file
  #   prefixes = json.load(f) #load the json file
  prefixes=db["prefixes"]
  prefix = prefixes[str(ctx.guild.id)]
  if commandType==None:
    embed = discord.Embed( colour=discord.Color.orange())
    embed.set_author(name="Astro's Command Categories", url="https://teamastro.ml/commands", icon_url=f"{client.user.avatar_url}")
    embed.add_field(name="**Music**", value=f"` {prefix}help music `", inline=True)
    embed.add_field(name="**Moderator**", value=f"` {prefix}help moderator `", inline=True)
    embed.add_field(name="**Dungeon**", value=f"` {prefix}help dungeon `", inline=True)
    embed.add_field(name="**Utility**", value=f"` {prefix}help utility `", inline=True)
    embed.add_field(name="**Data**", value=f"` {prefix}help data `", inline=True)
    embed.add_field(name="**Fun**", value=f"` {prefix}help fun `", inline=True)
    embed.add_field(name="**Other**", value=f" [Dashboard]( {website}/guild/{ctx.guild.id} )", inline=True)
    # embed.add_field(name="**CPU**", value=f"` {psutil.cpu_percent(0)}% `", inline=True)
    # embed.add_field(name="**RAM**", value=f"` {psutil.virtual_memory()[2]}% `", inline=True)
    
    embed.set_thumbnail(url=client.user.avatar_url)
    await ctx.send(embed=embed, delete_after=10)
    return
  commandType = commandType.lower()
  if commandType =="music" or commandType =="moderator" or commandType =="dungeon" or commandType =="utility" or commandType =="data" or commandType =="fun":
    if commandType == "music":
      embed = discord.Embed(title="Music", colour=discord.Color.orange())
      # embed.set_author(name="Music", url="https://teamastro.ml/commands", icon_url=f"{client.user.avatar_url}")
      embed.add_field(name="**Play**", value=f"` {prefix}play <song> | Plays A Song `", inline=False)
      embed.add_field(name="**Queue**", value=f"` {prefix}queue <song> | Queues A Song `", inline=False)
      embed.add_field(name="**Queue**", value=f"` {prefix}queue | Lists The Queue `", inline=False)
      embed.add_field(name="**Remove**", value=f"` {prefix}remove <song/number> | Removes A Song From The Queue `", inline=False)
      embed.add_field(name="**Seek**", value=f"` {prefix}seek <position> | Moves The Currently Playing Song To A New Position `", inline=False)
      embed.add_field(name="**Search**", value=f"` {prefix}search <song> | Searches For A Song `", inline=False)
      embed.add_field(name="**Pause**", value=f"` {prefix}pause | Pauses The Playing Song `", inline=False)
      embed.add_field(name="**Resume**", value=f"` {prefix}resume | Resumes The Playing Song `", inline=False)
      embed.add_field(name="**Stop**", value=f"` {prefix}stop | Stops The Playing Song `", inline=False)
      embed.add_field(name="**Shuffle**", value=f"` {prefix}shuffle | Shuffles The Queue `", inline=False)
      embed.add_field(name="**Clear Queue**", value=f"` {prefix}clear queue | Clears The Queue `", inline=True)
      embed.add_field(name="**Lyrics**", value=f"` {prefix}lyrics <song> | Lyrics For The Currently Playing Song, Or Any Song If Specified `", inline=False)
      embed.add_field(name="**Playing**", value=f"` {prefix}playing | Displays What Is Playing `", inline=False)
      embed.add_field(name="**Volume**", value=f"` {prefix}volume <amount> | Changes Astro's Volume `", inline=False)
      embed.add_field(name="**Previous**", value=f"` {prefix}previous | Goes Back A Song `", inline=False)
      await ctx.send(embed=embed)
    if commandType == "moderator":
      embed = discord.Embed(title="Moderator", colour=discord.Color.orange())
      # embed.set_author(name="Music", url="https://teamastro.ml/commands", icon_url=f"{client.user.avatar_url}")
      embed.add_field(name="**Kick**", value=f"` {prefix}kick <user> | Kicks A User From This Server `", inline=False)
      embed.add_field(name="**Ban**", value=f"` {prefix}ban <user> | Bans A User From This Server `", inline=False)
      embed.add_field(name="**Mute**", value=f"` {prefix}mute <user> | Mutes A User `", inline=False)
      embed.add_field(name="**Unmute**", value=f"` {prefix}unmute <user> | Unmutes A User `", inline=False)
      embed.add_field(name="**Muted**", value=f"` {prefix}muted | Lists All Users That Have Been Muted `", inline=False)
      # embed.add_field(name="**Seek**", value=f"` {prefix}seek <position> | Moves The Currently Playing Song To A New Position `", inline=False)

      # embed.set_thumbnail(url=client.user.avatar_url)
      await ctx.send(embed=embed)
    if commandType == "dungeon":
      embed = discord.Embed(title="The Dungeon Game's Commands", colour=discord.Color.orange())
      # embed.set_author(name="Music", url="https://teamastro.ml/commands", icon_url=f"{client.user.avatar_url}")
      embed.add_field(name="**Balance**", value=f"` {prefix}balance | Checks How Much Money You Have `", inline=False)
      embed.add_field(name="**Beg**", value=f"` {prefix}beg | Begs For More Money `", inline=False)
      embed.add_field(name="**Buy**", value=f"` {prefix}buy <amount> <item> | Buys An Item/Healable/Weapon `", inline=False)
      embed.add_field(name="**Shop**", value=f"` {prefix}shop | Checks What's In The Shop `", inline=False)
      embed.add_field(name="**Items**", value=f"` {prefix}items | Checks What Items You Have `", inline=False)
      embed.add_field(name="**Rob**", value=f"` {prefix}rob <user> | Robs Money From Another User `", inline=False)
      embed.add_field(name="**Deposit**", value=f"` {prefix}deposit <amount> | Deposits Money From You're Wallet To You're Bank `", inline=False)
      embed.add_field(name="**Withdraw**", value=f"` {prefix}withdraw <amount> | Withdraw's Money From You're Bank `", inline=False)
      embed.add_field(name="**Send**", value=f"` {prefix}send <amount> | Send's Money To Another User `", inline=False)
      embed.add_field(name="**Attack**", value=f"` {prefix}attack <user> <item> | Attack's A User With An Item `", inline=False)
      embed.add_field(name="**Heal**", value=f"` {prefix}heal <item> | Uses A Healable `", inline=False)
      embed.add_field(name="**Heal**", value=f"` {prefix}heal <item> | Uses A Healable `", inline=False)
      embed.add_field(name="**Sell**", value=f"` {prefix}sell <amount> <item> | Sells An Item You Have For A Lower Price `", inline=False)
      embed.add_field(name="**Slots**", value=f"` {prefix}slots <amount> | Risks Your Money For Double If You Win `", inline=False)
      embed.add_field(name="**Jobs**", value=f"` {prefix}jobs | Lists All Available Jobs `", inline=False)
      embed.add_field(name="**Earn**", value=f"` {prefix}earn <job type> | Earns You Money For A Specified Job `", inline=False)
      await ctx.send(embed=embed)
    if commandType == "utility":
      embed = discord.Embed(title="Utility", colour=discord.Color.orange())
      # embed.set_author(name="Music", url="https://teamastro.ml/commands", icon_url=f"{client.user.avatar_url}")
      embed.add_field(name="**Reminder**", value=f"` {prefix}reminder <time> <reminder text> | Reminds You About Something In A Specified Amount Of Time `", inline=False)
      embed.add_field(name="**Timer**", value=f"` {prefix}Timer <time> | Sets A Timer For A Certain Amount Of Time `", inline=False)
      embed.add_field(name="**News**", value=f"` {prefix}news <amount> | Gives You A Specified Amount Of Headlines `", inline=False)
      embed.add_field(name="**Wiki**", value=f"` {prefix}wiki <query> | Searches Wikipedia For Something `", inline=False)
      embed.add_field(name="**Google Links**", value=f"` {prefix}googlelinks <query> | Gives You Link Results From Your Query `", inline=False)
      embed.add_field(name="**Google**", value=f"` {prefix}google <query> | Gets A Google Result For Your Query `", inline=False)
      embed.add_field(name="**poll**", value=f"` {prefix}poll <time> <question> | Creates A Poll For Your Discord Server `", inline=False)
      # embed.add_field(name="**Seek**", value=f"` {prefix}seek <position> | Moves The Currently Playing Song To A New Position `", inline=False)

      # embed.set_thumbnail(url=client.user.avatar_url)
      await ctx.send(embed=embed)

    if commandType == "data":
      embed = discord.Embed(title="Live Data", colour=discord.Color.orange())
      # embed.set_author(name="Music", url="https://teamastro.ml/commands", icon_url=f"{client.user.avatar_url}")
      embed.add_field(name="**Time**", value=f"` {prefix}time in <region> | Gives You The Time In Any Region `", inline=False)
      embed.add_field(name="**Timer**", value=f"` {prefix}Timer <time> | Sets A Timer For A Certain Amount Of Time `", inline=False)
      embed.add_field(name="**News**", value=f"` {prefix}news <amount> | Gives You A Specified Amount Of Headlines `", inline=False)
      embed.add_field(name="**Wiki**", value=f"` {prefix}wiki <query> | Searches Wikipedia For Something `", inline=False)
      embed.add_field(name="**Google Links**", value=f"` {prefix}googlelinks <query> | Gives You Link Results From Your Query `", inline=False)
      embed.add_field(name="**Google**", value=f"` {prefix}google <query> | Gets A Google Result For Your Query `", inline=False)
      embed.add_field(name="**Userinfo**", value=f"` {prefix}userinfo <user> | Gives You User Info For Any User In The Server `", inline=False)
      embed.add_field(name="**Serverinfo**", value=f"` {prefix}serverinfo | Gives You Server Info For This Server `", inline=False)
      await ctx.send(embed=embed)
    if commandType == "fun":
      embed = discord.Embed(title="Fun", colour=discord.Color.orange())
      # embed.set_author(name="Music", url="https://teamastro.ml/commands", icon_url=f"{client.user.avatar_url}")
      embed.add_field(name="**8ball**", value=f"` {prefix}8ball <question> | Answers Your Life Questions `", inline=False)
      embed.add_field(name="**Meme**", value=f"` {prefix}meme <Sub Reddit> | Gives You A Meme From Any Subreddit `", inline=False)
      embed.add_field(name="**Reddit**", value=f"` {prefix}reddit <Sub Reddit> | Gives You Posts From Any Subreddit `", inline=False)
      embed.add_field(name="**Joke**", value=f"` {prefix}joke | Gives You Some Funny Jokes `", inline=False)

      # embed.add_field(name="**Seek**", value=f"` {prefix}seek <position> | Moves The Currently Playing Song To A New Position `", inline=False)

      # embed.set_thumbnail(url=client.user.avatar_url)
      await ctx.send(embed=embed)

  else:
    embed = discord.Embed( title="❌ Nothing Found",colour=discord.Color.orange())
    await ctx.send(embed=embed)
  # embed = discord.Embed(title="Commands", colour=discord.Color.orange(), timestamp=datetime.utcnow())

  # embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")


  # embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")

  # embed.add_field(name="Music 🎵", value="Play,\nPause,\nPlayurl,\nResume,\nSkip,\nLyrics,\nQueue,\nListqueue,\nRemove,\nClearqueue", inline=True)
  # embed.add_field(name="Moderation 📶", value="Kick,\nBan,\nInvite,\nAuto Moderation Features,\nMute,\nUnmute,\nMuted", inline=True)
  # embed.add_field(name="Games 🎯", value="8ball,\nTictactoe,\nRock Paper Scissors(playrps),\nDungeon Crawler", inline=True)
  # embed.add_field(name="Productivity/Work ⚒", value="Reminder,\nTimer,\nPolltimes,\nPoll,\nSearchyt,\nYoutube,\nGoogle,\nGooglelinks,\nWiki,\nAgenda,\nMeeting,\nTasks,\nListtasks,\nCleartasks,\nTeamtask,\nListteamtasks,\nDeletetask\nListteamtasks", inline=True)
  # embed.add_field(name="Live Data 📈", value="Time,\nWeather,\nCovid,\nUserinfo", inline=True)
  # embed.add_field(name="Fun 🎉", value="Meme,\nTictactoe,\nReddit,\nJoke,\n**| THE DUNGEON GAME |**", inline=True)

  # await ctx.send(embed=embed)
  



@client.command(aliases=['quickstart','beginSetup'])
async def setup(ctx):
  await on_guild_join(ctx.guild)

@client.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    print("Removed From "+guild.name)
    # with open('prefixes.json', 'r') as f: #read the file
    #   prefixes = json.load(f)

    # prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    # with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
    #   json.dump(prefixes, f, indent=4)



@client.event
async def on_guild_join(guild):
  # with open('prefixes.json', 'r') as f: #read the prefix.json file
  #   prefixes = json.load(f) #load the json file
  prefixes=db["prefixes"]
  prefixes[str(guild.id)]='.'
  db["prefixes"]=prefixes

  #   prefixes[str(guild.id)] = '.'#default prefix

  #   with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
  #     json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater
    
    # for channel in guild.text_channels:
    #     if channel.permissions_for(guild.me).send_messages:
    #         await channel.send('> Hi, I am Astro! Thanks For Inviting Me To '+guild.name+'!'+" To Start Using Me, I Have To Walk You Through My Set Up Process! I have sent a DM to the owner of the server, to begin the setup process! For A Full List Of My Commands use the help command!".title())
    #         try:
    #           await guild.owner.send('> Hi, I am Astro! Thanks For Inviting Me To '+guild.name+'!'+" To Start Using Me, I Have To Walk You Through My Set Up Process! Type The Server Name To Proceed!")
    #         except:
    #           await channel.send('> '+guild.owner.mention+" Doesnt Seem to Be Accepting Messages...")
    #         msg = await client.wait_for('message')
    #         while(msg.content.lower()!=guild.name.lower() ):
    #           msg = await client.wait_for('message')
    #         await guild.owner.send("> Excellent!")
    #         await asyncio.sleep(1)

    #         await guild.owner.send("> 1. Start by letting me know what words you would like to moderate in your server. These words will be automatically deleted if sent. Words should be seperated by a ', '. In addition to that, include your server name at the beginning of your msg(eg: <server name> word1, word2, word3) Do not worry, you can always change this later by using the setup command to walk through this process again!".title())
            
    #         swearWordsMsg= await client.wait_for('message')
    #         while(guild.name.lower() not in swearWordsMsg.content.lower()):
    #           msg = await client.wait_for('message')
    #         swearWordsMsgContent=swearWordsMsg.content.replace(guild.name.lower()+" ",'')

    #         swearWordsArr = swearWordsMsgContent.split(", ")
    #         await add_server_swear(guild.id , swearWordsArr)
    #         await guild.owner.send("Cool! Your Moderated Words Are Now: "+str(swearWordsArr))
    #         await guild.owner.send("> 2. Give Astro Admin. In Order to do this, create a new role and check the admin box at the bottom under the permissions section. Then add that role to Astro. If you already have the role created, skip the first step. In Order for proto to moderate it needs admin!".title())
    #         await asyncio.sleep(60)
    #         await guild.owner.send("Thats all for now! Remember, Use The .Setup Command To Walk through this again, and change your setup.".title())
    #         return

            # await guild.owner.send("> 2. Let me know what prefixes you would like to use. Seperate all of the prefixes with ', '.")

            # swearWordsMsg= await client.wait_for('message')
            # swearWordsArr = swearWordsMsg.split(", ")
            # await add_prefixes(guild.id , swearWordsArr)

            # await guild.owner.send()
            
        # break


# async def add_prefixes(server, prefixArr):

#   with open("prefixes.json","r") as f:
#     users = json.load(f)
#   if str(server) in users:
#     for element in prefixArr:
#       users[str(server)]["prefixes"].append(element)
#   else:
#     users[str(server)]= {}
#     users[str(server)]["prefixes"]=prefixArr
#   with open("prefixes.json","w") as f:
#     json.dump(users,f)

#   # return True




# async def add_server_swear(server, swearWordsArr):

#   with open("swearWords.json","r") as f:
#     users = json.load(f)
#   if str(server) in users:
#     for element in swearWordsArr:
#       users[str(server)]["words"]=swearWordsArr
#   else:
#     users[str(server)]= {}
#     users[str(server)]["words"]=swearWordsArr
#   with open("swearWords.json","w") as f:
#     json.dump(users,f)

  # return True








async def mute_person(user, server):
  if user.id==809609861456723988:
    return
  with open("mutedUsers.json","r") as f:
    users = json.load(f)
  if str(user.id) in users:
    if server not in users[str(user.id)]["mute"]:
      users[str(user.id)]["mute"].append(server)
  else:
    users[str(user.id)]= {}
    users[str(user.id)]["mute"]=[]
    users[str(user.id)]["mute"].append(server)
  with open("mutedUsers.json","w") as f:
    json.dump(users,f)
  print("hi")
  # return True

async def unMute_person(user, server):
  with open("mutedUsers.json","r") as f:
    users = json.load(f)
  print(users[str(user.id)]["mute"])
  print("given server "+str(server))
  users[str(user.id)]["mute"].remove(server)

  with open("mutedUsers.json","w") as f:
    json.dump(users,f)
  # return True




mainshop = [
            #useless items
            {"name":"Mi 11 Ultra","price":10000000000000,"description":"Useless","damage":0},
            {"name":"Laptop","price":1000,"description":"Useless","damage":0},
            {"name":"PC","price":10000,"description":"Useless","damage":0},


            

            #weapons
            {"name":"Knife","price":20000,"description":"Weapon","damage":5},
            {"name":"Wooden Sword","price":1000,"description":"Weapon","damage":10},
            {"name":"Stone Sword","price":4000,"description":"Weapon","damage":20},
            {"name":"Iron Sword","price":10000,"description":"Weapon","damage":40},
            {"name":"Steel Sword","price":15000,"description":"Weapon","damage":60},
            {"name":"Daggers","price":20000,"description":"Weapon","damage":75},
            {"name":"Diamond Sword","price":30000,"description":"Weapon","damage":90},
            {"name":"Pistol","price":50000,"description":"Weapon","damage":110},
            {"name":"Deagle","price":100000,"description":"Weapon","damage":155},
            {"name":"Rifle","price":200000,"description":"Weapon","damage":175},
            {"name":"Gandalf Staff","price":1000000000000,"description":"Weapon","damage":300},
            {"name":"Sauron Ring","price":1000000000000000,"description":"Weapon","damage":499},

            #armor

            {"name":"Mini","price":500,"description":"Armor","damage":0,"armor":25},
            {"name":"50 pot","price":4000,"description":"Armor","damage":0,"armor":50},
            {"name":"100 shield","price":15000,"description":"Armor","damage":0,"armor":100},
            



            #healables
            {"name":"Bandage","price":250,"description":"Healable","damage":-10,"armor":0},
            {"name":"Mini Med Kit","price":1000,"description":"Healable","damage":-25,"armor":0},
            {"name":"Med Kit","price":2500,"description":"Healable","damage":-100,"armor":0},    
            {"name":"Holy Grail","price":1000000000000000000,"description":"Healable","damage":-499,"armor":0},
            ]

















import json
import os

@client.command()
async def sell(ctx,amount = 1,*, item):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Item Does Not Exist")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item.title()} for {amount*res[2]}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.7* item["price"]
                resaleprice=price
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked",resaleprice]







# @client.command(aliases=['Sellto'])
# async def sellto(ctx, member: discord.Member , amount, *, item):

#   await open_account(ctx.author)
#   await open_account(member)
#   users = await get_bank_data()

  

#   item_name=item.lower()
#   item_name = item_name.lower()
#   name_ = None
#   for item in mainshop:
#       name = item["name"].lower()
#       desc =item["description"].lower()
#       if name == item_name and desc =="weapon":
#           name_ = name
#           break
#   if name_ == None:
#     await ctx.send("This Item Does Not Exist.")
#     return
#   user=ctx.author

#   users = await get_bank_data()

#   bal = await update_bank(user)

#   index = False

#   #deletes from inventory
#   t = None
#   try:
#     for thing in users[str(user.id)]["bag"]:
#       n = thing["item"]
#       print(f"Item Name: {item_name}, Current Item: {n}")
#       if n.lower() == item_name.lower():
#         old_amt = thing["amount"]
#         try:
#           if old_amt==0 or old_amt<0:
#             await ctx.send("You Do Not Have This Item.")
#             return
#         except:
#           pass
        
#         index=True
#         break
#   except:
#     await ctx.send("You Do Not Have This Item.")
#     return

#   if index==False:
#     await ctx.send("You Do Not Have This Item.")
#     return

  
#   msg = await ctx.send(f"> {ctx.author.name} Wants To Sell {item_name.title()} to {member.name} for {amount} 💰s. Proto Has Sent {member.name} A DM With Your Request.")

#   # await msg.add_reaction("✅")
#   # await msg.add_reaction("❌")
#   # await msg.on_reaction_add("✅", member)
#   msgsent = await member.send(f"{ctx.author.name} Wants To Sell {item_name.title()} to {member.name} for {amount} 💰s. Respond with a y if you accept this deal or with a n if you do not.")

#   def check(message):
#     return msgsent.channel.type == discord.ChannelType.private

#   response = await msg.wait_for_message(timeout = 3600, author = member, check=check, content="SSM")
#   print(response.content)
#   # msga = await client.wait_for('message')

#   print("hi!")
#   # reaction, user = await client.wait_for("reaction_add")
#   # def check(reaction, user):
#   #   return user != client.user and str(reaction.emoji) in ["✅"]
#   # while True:
#   #   try:
      
#   #     reaction, user = await client.wait_for("reaction_add")
#   #     if str(reaction.emoji) == "✅":
#   #       print('hi!')
#   #   except asyncio.TimeoutError:
#   #     return















async def use_item(user, item_name):
    item_name = item_name.lower()
    name_ = None
    armor= None
    dmg = None
    users = await get_bank_data()
    for item in mainshop:
        name = item["name"].lower()
        desc =item["description"].lower()
        if name == item_name and desc =="healable":
          print(users[str(user.id)]["health"])
          if users[str(user.id)]["health"]>=500:
            print("hi")
            return [False, 3]
          name_ = name
          dmg = item["damage"]
          armor = item["armor"]
          break
        elif name == item_name and desc == "armor":
          if users[str(user.id)]["armor"]>=500:
            print("hi")
            return [False, 3]
          name_=name
          dmg= 0
          armor = item["armor"]
    
    if name_ == None:
        return [False,1]
    print(name_)

    users = await get_bank_data()

    bal = await update_bank(user)

    index = False

    #deletes from inventory
    t = None
    try:
      for thing in users[str(user.id)]["bag"]:
          n = thing["item"]
          print(f"Item Name: {item_name}, Current Item: {n}")
          if n.lower() == item_name.lower():
              old_amt = thing["amount"]
              try:
                if old_amt==0 or old_amt<0:
                  return [False,2]
              except:
                pass
              new_amt = old_amt - 1

              users[str(user.id)]["bag"][index]["amount"] = new_amt
              
              index=True
              break
    except:
      return [False,2]

    if index==False:
      return [False,2]


    
    return [True,"Worked",dmg, armor]


@client.command(aliases=['heal', 'Utilize'])
async def use(ctx, *, item):
  users = await get_bank_data()
  await open_account(ctx.author)

  # if users[str(ctx.author.id)]["health"]>=500 or users[str(ctx.author.id)]["armor"]>=500:
  #   await ctx.send("You Cannot Use Potions/Healables when You Have More Than 500 Health Or Armor.")
  #   return
  if users[str(ctx.author.id)]["healing"]==True:
    await ctx.send(f"{ctx.author.name} cannot use a {item.title()} until {ctx.author.name}'s healing countdown expires.")
    return


  res = await use_item(ctx.author,item)
  if not res[0]:
      if res[1]==1:
          await ctx.send("That Item Does Not Exist.")
          return
      if res[1]==2:
          await ctx.send(f"You don't have a {item.title()}.")
          return
      if res[1]==3:
          await ctx.send(f"You cannot use a {item.title()} when you are at 500 health/shield.")
          return

  

  await ctx.send(f"> {ctx.author.mention} just used a {item.title()} for {-1*res[2]} health and {res[3]} armor. Wait two more minutes before using an item again.")
  armor=res[3]
  dmg=res[2]
  user=ctx.author
  users[str(user.id)]["health"] = users[str(user.id)]["health"]-dmg
  print(armor)
  print(users[str(user.id)]["armor"])
  users[str(user.id)]["armor"] = users[str(user.id)]["armor"]+armor
  print(users[str(user.id)]["armor"])
  users[str(user.id)]["healing"]=True
  users[str(ctx.author.id)]["healing"]=True
  
  
  with open("mainbank.json","w") as f:
      json.dump(users,f)

  
  await asyncio.sleep(120)
  users[str(ctx.author.id)]["healing"]=False

  with open("mainbank.json","w") as f:
    json.dump(users,f)
    f.close()


  






async def attack_person(user,victim,item_name):
    item_name = item_name.lower()
    name_ = None
    dmg = None
    for item in mainshop:
        name = item["name"].lower()
        desc =item["description"].lower()
        if name == item_name and desc =="weapon":
            name_ = name
            dmg = item["damage"]
            
            break
    
    if name_ == None:
        return [False,1]
    print(name_)

    users = await get_bank_data()

    bal = await update_bank(user)

    index = False

    #deletes from inventory
    t = None
    try:
      for thing in users[str(user.id)]["bag"]:
          n = thing["item"]
          print(f"Item Name: {item_name}, Current Item: {n}")
          if n.lower() == item_name.lower():
              old_amt = thing["amount"]
              try:
                if old_amt==0 or old_amt<0:
                  return [False,2]
              except:
                pass
              new_amt = old_amt - 1

              users[str(user.id)]["bag"][index]["amount"] = new_amt
              
              index=True
              break
    except:
      return [False,2]

    if index==False:
      return [False,2]

    
    
    return [True,"Worked",dmg]


@client.command(aliases=['Fight'])
async def attack(ctx, member: discord.Member=None, *, item):

  await open_account(ctx.author)
  await open_account(member)
  user=ctx.author
  
  res = await attack_person(ctx.author,member, item)
  if not res[0]:
      if res[1]==1:
          await ctx.send("That Item Does Not Exist.")
          return
      if res[1]==2:
          await ctx.send(f"{ctx.author.mention} Doesn't have a {item.title()}.".title())
          return
  users = await get_bank_data()
  if users[str(ctx.author.id)]["attacking"]==True:
    await ctx.send(f"{ctx.author.mention} cannot attack since they has already attacked/robbed recently. Wait for the cooldown to expire.".title())
    return
  
  dmg = res[2]
  totalHealth = users[str(member.id)]["health"]+users[str(member.id)]["armor"]
  if users[str(member.id)]["armor"]>0:
    print("Damage subbed from Armor")
    users[str(member.id)]["armor"]=users[str(member.id)]["armor"]-dmg
    if users[str(member.id)]["armor"] <0:
      print("Damage subbed from health too!")
      users[str(member.id)]["health"]=users[str(member.id)]["health"]+users[str(member.id)]["armor"]
  else:
    users[str(member.id)]["health"]=users[str(member.id)]["health"]-dmg
    print("Damage subbed from health")

  if users[str(member.id)]["health"]<=0:
    await ctx.send(member.mention+" Has Died To "+ctx.author.name +". "+ctx.author.name+" also now inherits all "+member.name+"'s money")
    # users[str(member.id)]["killer"]=str(ctx.author.id)
    users[str(user.id)]["wallet"]=users[str(user.id)]["wallet"]+users[str(member.id)]["wallet"]+users[str(member.id)]["bank"]
  users[str(user.id)]["attacking"]=True
  
  with open("mainbank.json","w") as f:
      json.dump(users,f)


  await ctx.send(f"{ctx.author.name} just attacked {member.name} with {item} for {res[2]} damage. {ctx.author.name} cannot attack for another {(res[2]*75)/60} minutes.")
  
  await asyncio.sleep(res[2]*75)
  users[str(ctx.author.id)]["attacking"]=False

  with open("mainbank.json","w") as f:
    json.dump(users,f)













































@client.command(aliases=['stats','gameinfo','bal'])
async def balance(ctx, member: discord.Member=None):
  if member != None:
    pass
  else:
    member = ctx.author

  await open_account(member)
  user=member
  users = await get_bank_data()

  wallet_amt = users[str(user.id)]["wallet"]
  bank_amt = users[str(user.id)]["bank"]
  job = users[str(user.id)]["job"]
  health = users[str(user.id)]["health"]
  armor = users[str(user.id)]["armor"]
  attacking = users[str(user.id)]["attacking"]
  healing = users[str(user.id)]["healing"]

  embed = discord.Embed(title=f"{member.name}'s Stats", colour = discord.Color.gold(),timestamp=datetime.utcnow())
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")
  embed.set_footer(text="Team Astro | https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")
  embed.set_thumbnail(url=user.avatar_url)
  embed.add_field(name = "Health:", value=str(health))
  embed.add_field(name = "Armor:", value=str(armor))
  embed.add_field(name = "Wallet Balance:", value=str(wallet_amt)+" 💰s")
  embed.add_field(name = "Bank Balance:", value=str(bank_amt)+" 💰s")
  embed.add_field(name = "Working A Job?", value=str(job))
  embed.add_field(name = "Attack Cooldown On?", value=str(attacking))
  embed.add_field(name = "Healing Cooldown On?", value=str(healing))
  await ctx.send(embed=embed)
  return


@client.command()
async def beg(ctx):
  user=ctx.author
  await open_account(ctx.author)

  users = await get_bank_data()

  earnings = random.randrange(101)

  await ctx.send(f"> Someone gave {user.mention} {earnings} 💰s!")
  users[str(user.id)]["wallet"]+=earnings
  print(users[str(user.id)]["wallet"])
  print(earnings)
  with open("mainbank.json","w") as f:
    json.dump(users,f)

async def update_bank(user,change=0,mode="wallet"):
  users = await get_bank_data()
  print("Before: "+str(users[str(user.id)][mode]))
  users[str(user.id)][mode]+=change
  print("After: "+str(users[str(user.id)][mode]))

  with open("mainbank.json","w") as f:
    json.dump(users,f)

  bal=[users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
  return bal

@client.command()
async def deposit(ctx, amount: str):
  try:
    if int(amount)<0:
      await ctx.send("You Cannot Deposit A Negative Amount.")
      return
  except:
    pass
  user=ctx.author
  users = await get_bank_data()
  if amount.lower() == "total":
    amount = int(users[str(user.id)]["wallet"])
  else:
    amount = int(amount)

  await open_account(ctx.author)


  if amount >3000:
    await ctx.send("Sorry, you cannot deposit this much money at once, you can only deposit amounts between 1 and 3000 💰s")
    return
  if amount > users[str(user.id)]["wallet"]:
    await ctx.send(f"> {user.mention} Cannot Deposit More Than What You Have In Your Wallet.")
    return

  await ctx.send(f"> {user.mention} deposited {amount} 💰s!")
  users[str(user.id)]["bank"]+=amount
  users[str(user.id)]["wallet"]-=amount


  with open("mainbank.json","w") as f:
    json.dump(users,f)

jobsarr = ["Fastfood Worker","Construction Worker", "Project Manager", "Manager","Developer","Engineer","COO", "CEO"]
jobsmon = [1000,1000,50000,150000,200000,200000,100000000, 1000000000000 ]
jobsincome = [15,20,40,50,80,100,500,1000]




@client.command(aliases=['alljobs','listjobs','work'])
async def jobs(ctx):
  em = discord.Embed(title = f"All Jobs" , description = "Use The Earn Command And One of These Jobs, And If You Meet The Requirements, You Will Work A Day In That Job",color = discord.Color.gold(),timestamp=datetime.utcnow()) 
  em.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")
  em.set_footer(text="Team Astro | https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  for i in range(len(jobsarr)):
    em.add_field(name = f"{jobsarr[i]}" , value = f"Hourly Income: {jobsincome[i]} 💰s | Required Money: {jobsmon[i]}💰s",  inline = False)
    
  await ctx.send(embed = em)



@client.command()
async def earn(ctx, *, job: str=None):
  await open_account(ctx.author)
  users = await get_bank_data()

  user=ctx.author
  if job==None:
    await ctx.send("You Must Name A Job, For The List of Jobs, Use The Job Command.")
    return
  jobElement=0
  i=0
  iSave=0
  for element in jobsarr:
    i=i+1
    if element.lower() == job.lower():
      jobElement = element
      iSave=i-1

  print(jobsarr[iSave])
  print(jobsmon[iSave])
  print(jobsincome[iSave])
  bal = await update_bank(ctx.author)
  
  if users[str(user.id)]["job"]==True:
    await ctx.send("You Cannot Work Two Jobs At Once. Wait For Your Current Gig To Finish, Then Start A New One.")
    return

  if bal[0]+bal[1]<jobsmon[iSave]:
    await ctx.send("You Must Have The Required Amount Of Money To Do This Job. Check The Job Command For More Info.")
    return
  await ctx.send("After every hour you will earn "+str(jobsincome[iSave])+" for 1 day as a "+str(jobsarr[iSave]))
  
  users[str(user.id)]["job"]=True
  with open("mainbank.json","w") as f:
    json.dump(users,f)

  for a in range(24):
    await asyncio.sleep(3600)
    await update_bank(ctx.author,jobsincome[iSave])

  users[str(user.id)]["job"]=False
  with open("mainbank.json","w") as f:
    json.dump(users,f)
  


  

@client.command()
async def gamble(ctx, amount: str):
  try:
    if int(amount)<0:

      await ctx.send("You Cannot Use A Negative Amount.")
      return
  except:
    pass
  user=ctx.author
  bal = await update_bank(ctx.author)
  users = await get_bank_data()
  if amount.lower() == "total":
    amount = int(users[str(user.id)]["wallet"])
  else:
    amount = int(amount)

  await open_account(ctx.author)
  if amount > bal[0]:
    await ctx.send("You Cannot Gamble More Than What You Have In Your Wallet.")
    return
  choices = [1,2,3]

  if random.choice(choices)==3:
    await update_bank(ctx.author,2*amount)
    await ctx.send("🎉You Won! You Won Double The Amount You Bet!🎉")
  else:
    await ctx.send("You Lost Your Money, Tough Luck.")
    await update_bank(ctx.author,-1*amount)


@client.command()
async def slots(ctx, amount: str):
  try:
    if int(amount)<0:
      await ctx.send("You Cannot Play Slots With A Negative Amount.")
      return
  except:
    pass
  user=ctx.author
  bal = await update_bank(ctx.author)
  users = await get_bank_data()
  if amount.lower() == "total":
    amount = int(users[str(user.id)]["wallet"])
  else:
    amount = int(amount)

  await open_account(ctx.author)
  if amount > bal[0]:
    await ctx.send("You Cannot Play Slots With More Than What You Have In Your Wallet.")
    return
  final =[]
  for i in range(3):
    a = random.choice(["💸","💰","💡","⏰","🚀","🔨"])
    final.append(a)
  arraystring=""
  for element in final:
    arraystring=arraystring+" "+element
  await ctx.send(str(arraystring))

  if final[0]==final[1] or final[0]==final[2] or final[1] == final[2]:
    await update_bank(ctx.author,2*amount)
    await ctx.send("🎉You Won! You Won Double The Amount You Bet!🎉")
  else:
    await ctx.send("You Lost Your Money, Tough Luck.")
    await update_bank(ctx.author,-1*amount)
  
@client.command()
async def rob(ctx, member:discord.Member):
  await open_account(ctx.author)
  await open_account(member)
  user=ctx.author
  users = await get_bank_data()
  await open_account(ctx.author)

  bal = await update_bank(member)
  amount = random.randint(0,int((bal[0])/10))
  if amount>100000:
    amount=100000
  if users[str(ctx.author.id)]["attacking"]:
    await ctx.send(f"> {user.mention} Cannot Rob Right Now Because They Have Attacked Or Robbed Recently.")
    return
  if (users[str(ctx.author.id)]["wallet"]+users[str(ctx.author.id)]["bank"])<1000:
    await ctx.send(f"> {user.mention} Cannot Rob Anyone Until They Have More Than 1000 💰s.")
    return
  if (users[str(member.id)]["wallet"]+users[str(member.id)]["bank"])<600:
    await ctx.send(f"> {user.mention} Its Not Worth It. {member.mention} Has Less Than 600 💰s.")
    return

  await ctx.send(f"> {user.mention} Robbed {amount} 💰s From {member.mention}! {user.mention} Cannot Rob For The Next 30 Minutes")
  

  users[str(ctx.author.id)]["wallet"]+=amount
  users[str(member.id)]["wallet"]-=amount
  with open("mainbank.json","w") as f:
    json.dump(users,f)

  with open("mainbank.json","w") as f:
    json.dump(users,f)
  users[str(ctx.author.id)]["attacking"]=True
  with open("mainbank.json","w") as f:
    json.dump(users,f)
  await asyncio.sleep(1800)
  users[str(ctx.author.id)]["attacking"]=False
  with open("mainbank.json","w") as f:
    json.dump(users,f)
  

@client.command()
async def send(ctx,member:discord.Member, amount: str):
  await open_account(ctx.author)
  await open_account(member)

  try:
    if int(amount)<0:
      await ctx.send("You Cannot Send A Negative Amount.")
      return
  except:
    pass
  user=ctx.author
  users = await get_bank_data()
  if amount.lower() == "total":
    await ctx.send("> You Cannot Use the Total Keyword Here, You Must Name an Amount For Safety Purposes.")
    return
  else:
    amount = int(amount)
  await open_account(ctx.author)

  bal = await update_bank(ctx.author)
  if amount > bal[1]:
    await ctx.send("> You Cannot Send More Than What You Have In Your Bank.")
    return

  await ctx.send(f"> {user.mention} Sent {amount} 💰s to {member.mention}!")
  with open("mainbank.json","w") as f:
    json.dump(users,f)
  await update_bank(ctx.author, -1*amount, "bank")
  await update_bank(member,amount,"bank")


@client.command()
async def withdraw(ctx, amount: str):
  user=ctx.author

  try:
    if int(amount)<0:
      await ctx.send("You Cannot Withdraw A Negative Amount.")
      return
  except:
    pass
  users = await get_bank_data()
  if amount.lower() == "total":
    amount = int(users[str(user.id)]["bank"])
  else:
    amount = int(amount)


  if amount > users[str(user.id)]["bank"]:
    await ctx.send("You Cannot Withdraw More Than What You Have In Your Bank Account.")
    return

  await open_account(ctx.author)


  await ctx.send("> "+f"{user.mention} Withdrew {amount} 💰s!")
  users[str(user.id)]["wallet"]+=amount
  users[str(user.id)]["bank"]-=amount


  with open("mainbank.json","w") as f:
    json.dump(users,f)

@client.command(aliases = ["lb", "ranks","levels"])
async def leaderboard(ctx,x = 10):
  server = ctx.guild.id
  with open("userJson.json","r") as f:
    users = json.load(f)
  
  em = discord.Embed(title = f"Top Members In "+ctx.guild.name , description = "Based On Exp/Level For Each Server",color = discord.Color.gold(),timestamp=datetime.utcnow())
  
  em.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  em.set_footer(text="Team Astro | https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")
  
  # for element in users[str(server)]:
  #   element["exp"]
  arr = sorted(users[str(server)], key=lambda x: x['exp'], reverse=True)
  # print(arr)
  index = 1

  for element in arr:
    try:

      member = client.get_user(int(element["id"]))
      name = member.name
      lvl = element["lvl"]
      exp=element["exp"]
      # print(name)
      em.add_field(name = f"{index}. {name}" , value = f"Level: {lvl} | Experience: {exp}",  inline = False)
    except:
      pass
    if index>15:
      break
    index+=1
  await ctx.send(embed = em)







@client.command(aliases = ["gamelb"])
async def gameleaderboard(ctx,x = 10):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:

        name = int(user)
        # print(name)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    # print(total)
    total = sorted(total,reverse=True)
    # print(total)  

    em = discord.Embed(title = f"Top {x} Richest Members" , description = "What's In Your Wallet?",color = discord.Color.gold(),timestamp=datetime.utcnow())
    
    em.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    em.set_footer(text="Team Astro | https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    index = 1
    # print(total)
    # print(leader_board)
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        if (member in ctx.guild.members):
          name = member.name
        # print(name)
          em.add_field(name = f"{index}. {name}" , value = f"{amt} 💰s",  inline = False)
          if index == x:
            break
          else:
            index += 1
    await ctx.send(embed = em)
















@client.command()
async def buy(ctx,amount = 1,*,item):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("> "+"That Item Does Not Exist.")
            return
        if res[1]==2:
            await ctx.send("> "+f"You don't have enough money in your wallet to buy {amount} {item}")
            return
    await ctx.send("> "+f"You just bought {amount} {item}!")


@client.command(aliases = ['items','objects'])
async def bag(ctx, member: discord.Member = None):
    if member != None:
      user = member
    else:
      user = ctx.author
    await open_account(user)
    
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = user.name+"'s Items",color = discord.Color.gold(),timestamp=datetime.utcnow())
    
    em.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    em.set_footer(text="Team Astro | https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)  









async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]




@client.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop",color=discord.Color.gold(),timestamp=datetime.utcnow())
    
    em.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    em.set_footer(text="Team Astro | https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        damage = item["damage"]

        if damage<0:
          damage = damage*-1
          damage ="+"+ str(damage)
        else:
          damage ="-"+ str(damage)
        if item["description"]=="Armor":
          damage = str("+"+str(item["armor"]))
        em.add_field(name = name, value = f"{price} 💰s | {desc} | {damage}")

    await ctx.send(embed = em)


async def open_account(user):
  with open("mainbank.json","r") as f:
    users = json.load(f)
  if str(user.id) in users:
    return False
  else:
    users[str(user.id)]= {}
    users[str(user.id)]["health"]=500
    users[str(user.id)]["wallet"]=400
    users[str(user.id)]["bank"]=0
    users[str(user.id)]["job"]=False
    users[str(user.id)]["attacking"]=False
    users[str(user.id)]["healing"]=False
    users[str(user.id)]["armor"]=0
  with open("mainbank.json","w") as f:
    json.dump(users,f)
  return True

async def get_bank_data():
  with open("mainbank.json","r") as f:
    users = json.load(f)
  return users

# @client.command()
# async def resetstatus(ctx):
#   await ctx.send("> Reset!")
#   await client.change_presence(activity=discord.Game(name = '🚀'))




@client.command()
async def _emojiconvert(ctx,*, words : str):
  emo = Translator(exact_match_only=False, randomize=True)
  await ctx.send(emo.emojify(words))

def split(word): 
    return [char for char in word] 



@client.command(aliases = ['pfp','profilepic'])
async def _pfp(ctx, memb : discord.Member=None):
  if memb==None:
    pfp=ctx.author.avatar_url
  else:
    pfp = memb.avatar_url
  await ctx.send(pfp)

def downloadImages(query):
  from urllib.request import urlopen
  import simplejson
  # import cStringIO
  from urllib.request import Request, urlopen

  searchTerm = query
  startIndex = 0
  searchUrl = "google.com"
  print(searchUrl)
  page = urlopen(searchUrl)
  xml_page=page.read()
  page.close()
  soup_page=soup(xml_page,"lxml")
  news_list=soup_page.find_all("a", class_="rg_i Q4LuWd")

@client.command(aliases = ['nicknamemember','Nickname','Nick'])
@commands.has_permissions(administrator=True)
async def nickmember(ctx, target: discord.Member=None, *, nickname: str):
    # target = ctx.message.author
    if target == None:
      target=ctx.author
    if nickname == "reset":
      await target.edit(nick = target.name)
      nickSave = target.name+"'s Nickname Has Been Reset!"
    else:
      await target.edit(nick=nickname)
      nickSave = target.name+"'s Nickname Has Been Changed To " + nickname.title()
    if ctx.author.guild_permissions.administrator:
        x = ctx.guild.members
        if target in x:
             roles = [role for role in target.roles]
             embed = discord.Embed(title=nickSave, colour=discord.Color.gold(), timestamp=datetime.utcnow())

             embed.set_author(name=target.name, icon_url=target.avatar_url)

             embed.set_thumbnail(url=target.avatar_url)

             embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")

             fields = [("Name", str(target), False),
                   ("ID", target.id, False),
                   ("Status", str(target.status).title(), False),
                   (f"Roles ({len(roles)})", " ".join([role.mention for role in roles]), False),
                   ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
                   ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]

             for name, value, inline in fields:
                    embed.add_field(name=name, value=value, inline=inline)

             await ctx.send(embed=embed)
        else:
            await ctx.send(f'You have to ping soneone from this server')
    else:
        await ctx.send(f'Not enough permissions')

# @client.command(aliases = ['Spam','spamping', 'pingMember'])
# async def spam(ctx, amount=5, memb: discord.Member=None):
#   amount=int(amount)
#   if amount>30:
#     await ctx.send("Ping amounts cannot be greater than 30.")
#     return
#   if memb == None:
#     await ctx.send("Specify Someone to Spam.")
#     return
#   else:
#     for i in range(amount):
#       await ctx.send(str(memb.mention))
#       # await asyncio.sleep(1)

# @client.command(aliases = ['pingDm','spamDm', 'spamdm'])
# async def spamDM(ctx,amount, memb: discord.Member=None, *, msg:str=""):
#   amount=int(amount)
#   if amount>50:
#     await ctx.send("Ping amounts cannot be greater than 50.")
#     return
#   if memb == None:
#     await ctx.send("Specify Someone to Spam.")
#     return
#   else:
#     await ctx.send("Starting The Ping For "+memb.mention)
#     for i in range(amount):
#       await memb.send(memb.mention+" "+msg)
#       # await asyncio.sleep(1)



# @client.command(aliases = ['Nickname','Nick', 'nick'])
# async def nickname(ctx, *, nickname: str):
#     target=ctx.author
#     if nickname == "reset":
#       await target.edit(nick = target.name)
#       nickSave = target.name+"'s Nickname Has Been Reset!"
#     else:
#       await target.edit(nick=nickname)
#       nickSave = target.name+"'s Nickname Has Been Changed To " + nickname.title()
#     if True:
#         x = ctx.guild.members
#         if target in x:
#              roles = [role for role in target.roles]
#              embed = discord.Embed(title=nickSave, colour=discord.Color.gold(), timestamp=datetime.utcnow())

#              embed.set_author(name=target.name, icon_url=target.avatar_url)

#              embed.set_thumbnail(url=target.avatar_url)

#              embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")

#              fields = [("Name", str(target), False),
#                    ("ID", target.id, False),
#                    ("Status", str(target.status).title(), False),
#                    (f"Roles ({len(roles)})", " ".join([role.mention for role in roles]), False),
#                    ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
#                    ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]

#              for name, value, inline in fields:
#                     embed.add_field(name=name, value=value, inline=inline)

#              await ctx.send(embed=embed)
#         else:
#             await ctx.send(f'You have to ping soneone from this server')
#     else:
#         await ctx.send(f'Not enough permissions')


@client.command(aliases=['level','rank','exp', 'position'])
async def userinfo(ctx, target: discord.Member=None):
    if target==None:
      target=ctx.author
    exp,lvl = await level(ctx.guild.id,target.id)
    if True:
        x = ctx.guild.members
        if target in x:
            roles = [role for role in target.roles]
            embed = discord.Embed( colour=discord.Color.orange())

            embed.set_author(name=target.name, icon_url=target.avatar_url)

            embed.set_thumbnail(url=target.avatar_url)

            # embed.set_footer(text="Team Astro | https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")
            # embed.add_field(name="Experience Points:", value=str(exp), inline=False)
            # embed.add_field(name="Level:", value=str(lvl), inline=False)
            
            fields = [("Name",target.mention, True),
                  ("ID:", "` "+ str(target.id)+" `", True),
                  # ("Status:", str(target.status).title(), True),
                  (f"Roles: ({len(roles)})", " ".join([role.mention for role in roles]), True),
                  ("Created At:","` "+str(target.created_at.strftime("%m/%d/%Y %H:%M:%S"))+" `", True),
                  ("Joined At:","` "+ str(target.joined_at.strftime("%m/%d/%Y %H:%M:%S"))+" `", True)]
                  
            for name, value, inline in fields:
              embed.add_field(name=name, value=value, inline=inline)
            await ctx.send(embed=embed)
            
        # else:
        #     await ctx.send(f'You have to ping soneone from this server')
    else:
        await ctx.send(f'Not enough permissions')
 




@client.command(aliases = ['reactletters'])
async def react(ctx,*, words : str):
  finalWord = ""
  letterArr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  wordArr = split(words.lower())
  msg = await ctx.send("Reaction Below!")
  for j in range(len(wordArr)):
    for i in range(len(letterArr)):
      if letterArr[i] == wordArr[j]:
          if wordArr[j] == ' ':
            wordArr.pop(j)
          reaction =":regional_indicator_"+letterArr[i]+':'
          await msg.add_reaction(reaction)

  


@client.command(aliases = [ 'Emojify'])
async def _emojify(ctx,*, words : str):
  finalWord = ""
  letterArr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  wordArr = split(words.lower())
  for j in range(len(wordArr)):
    for i in range(len(letterArr)):
      if letterArr[i] == wordArr[j]:
        try:
          if wordArr[j+1] == ' ':
            finalWord = finalWord+":regional_indicator_"+letterArr[i]+':'+'     '
          else:
            finalWord = finalWord+":regional_indicator_"+letterArr[i]+':'+' '
        except IndexError:
          finalWord = finalWord+":regional_indicator_"+letterArr[i]+':'+''
  await ctx.send(finalWord)


# @client.command(aliases = ['lyrics', 'Lyrics','sing', 'Sing'])
# async def _lyrics(ctx,*, song : str=None):
#   if song==None:
#     try:
#         voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#         if voice.is_playing():
#           if song==None:
#             info = await accessPlaying(ctx.guild.id)
#             song=info[0]
#     except:
#       embed=discord.Embed(title="Currently Nothing is Playing!".title(), color = discord.Color.red())
#       await ctx.send(embed=embed)
#       return
#   try:

#     extract_lyrics = SongLyrics("AIzaSyBRcquo71lWc8_jaTOF-bhaEeT-fgfjI6M", "72f842b0aaf3270be")
#     loop = asyncio.get_event_loop()
#     test_dict = await loop.run_in_executor(None, lambda:extract_lyrics.get_lyrics(song))
#     # test_dict = extract_lyrics.get_lyrics(song)
#     res = {key: test_dict[key] for key in test_dict.keys() 
#                                 & {'lyrics'}}
#     for key, value in test_dict.items(): 
#       if key == "lyrics":
#         valSave = str(value)
#     embed=discord.Embed(title="Lyrics For "+song.title(), color = discord.Color.orange())
#     # await ctx.send("Here are the lyrics! \n")
#     valArr = valSave.split("\n\n")
#     for element in valArr:
#       embed.add_field(name="`~"+"`", value="`"+element+"`", inline=False)
#     await ctx.send(embed=embed)
#   except:
#     embed=discord.Embed(title="Couldn't Find That Song!", color = discord.Color.red())
#     await ctx.send(embed=embed)
#     return
  
  
  # valArr = valSave.split("\n\n")

  # await ctx.send("Here are the lyrics! \n")
  # for element in valArr:
  #   await ctx.send("> "+element+"\n\n")

  

@client.command(aliases = [ 'status'])
async def setstatus(ctx,*, status: str):
    # if skip == True:
    #     skip = False
    if ctx.author.id == 608778878835621900:
      await ctx.send("> Thanks Team Astro Admins It Has Been Set!")
      await client.change_presence(status=discord.Status.idle, activity=discord.Game(name = status))
    else:
      await ctx.send("Sorry, You Cannot Change The Status If You Are Not Part Of Team Astro's Adminstrative Team.")

@client.command()
async def playrps(ctx, userrps):
  arr = ["Rock", "Paper", "Scissors"]
  choice = rando.choice(arr)
  await ctx.send("> "+choice)
  print(choice)

  if userrps.lower() == choice.lower():
    await ctx.send("> Draw! Try at your own risk, surely I will beat you next time 😉!")
  if userrps.lower() == "rock" and choice.lower() == "scissors":
    await ctx.send("> AWWW shucks, you won 😒")
    return
  elif userrps.lower() == "scissors" and choice.lower() == "rock":
    await ctx.send("> HA I WON! 🐒")
    return

  if userrps.lower() == "paper" and choice.lower() == "rock":
    await ctx.send("AWWW shucks, you won 😒")
    return
  elif userrps.lower() == "rock" and choice.lower() == "paper":
    await ctx.send("> HA I WON! 🐒")
    return

  if userrps.lower() == "scissors" and choice.lower() == "paper":
    await ctx.send("> AWWW shucks, you won 😒")
    return
  elif userrps.lower() == "paper" and choice.lower() == "scissors":
    await ctx.send("> HA I WON! 🐒")
    return


import asyncio

@client.command(case_insensitive = True, aliases = ["setagenda", "angendaset", "meetingagenda", 'agendameeting'])
# @commands.bot_has_permissions(attach_files = True, embed_links = True)
async def agenda(ctx,*, question):
  author = ctx.message.author
  author_name = author.name
  print(question)
  if " " not in question and ", " not in question and "," not in question:
    await ctx.send("> You have not included the topics/items from the meeting. Remember seperate your topics like so: topic1, topic2, topic3, etc... Make sure to use commas. ")
    return
  questiona = question
  if "," in question and ", " not in question:
    questiona = question.replace(',', ', ')
  # if " " in question and ", " not in question:
  #   questiona = question.replace(' ', ', ')
  questionArr = questiona.split(", ")
  
  questiona = ""
  for i in range(len(questionArr)):
    if i != len(questionArr)-1:
      questiona = questiona + questionArr[i]+", "
    else:
      questiona = questiona + questionArr[i]
  # await ctx.send(author.mention+" Please give the summary for this meeting.")
  # msg = await client.wait_for('message')
  # summary = msg.content
  await ctx.send("@everyone")
  embed=discord.Embed(title="Agenda From " +author_name.title(), description= "Items", color=0xFF5733, timestamp=datetime.utcnow())

  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")


  embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/meeting-1543488-1305981.png")
  i=0
  for element in questionArr:
    i=i+1
    embed.add_field(name="Topic "+str(i)+":", value= str(element).title() , inline=False)


  await ctx.send(embed = embed)

@client.command(case_insensitive = True, aliases = ["meeting", "summary", "meetingSummary", 'summarizeMeeting'])
# @commands.bot_has_permissions(attach_files = True, embed_links = True)
async def _meetingSummary(ctx,*, question):
  author = ctx.message.author
  author_name = author.name
  print(question)
  if " " not in question and ", " not in question and "," not in question:
    await ctx.send("> You have not included the topics/items from the meeting. Remember seperate your topics like so: topic1, topic2, topic3, etc... Make sure to use commas. ")
    return
  questiona = question
  if "," in question and ", " not in question:
    questiona = question.replace(',', ', ')

  questionArr = questiona.split(", ")
  
  questiona = ""
  for i in range(len(questionArr)):
    if i != len(questionArr)-1:
      questiona = questiona + questionArr[i]+", "
    else:
      questiona = questiona + questionArr[i]
  await ctx.send(author.mention+" Please give the summary for this meeting.")
  msg = await client.wait_for('message')
  summary = msg.content
  await ctx.send("@everyone")
  embed=discord.Embed(title="Meeting Summary From " +author_name.title(), description= "Topics/Summary", color=0xFF5733, timestamp=datetime.utcnow())

  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    # Add rs/608778878835621900/76e69643d799ee584dd46afa91127105.webp")

  embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/meeting-1543488-1305981.png")
  i=0
  for element in questionArr:
    i=i+1
    embed.add_field(name="Topic "+str(i)+":", value= str(element).title() , inline=False)

  embed.add_field(name="Summary:", value= summary , inline=False)
  # embed.add_field(name="URL:", value = final_url , inline=False) 

  await ctx.send(embed = embed)




@client.command(case_insensitive = True, aliases = ["timer", "timeit"])
# @commands.bot_has_permissions(attach_files = True, embed_links = True)
async def _timer(ctx, time):
    reminder = ""
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
    embed.set_footer(text="Team Astro | https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")
    embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(name='Warning', value='Please specify what do you want me to remind you about.') # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(name='No Duration',
                        value='Please specify a proper duration, send `help` for more information.')
    elif seconds < 1:
        embed.add_field(name='Too Short Duration',
                        value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
    elif seconds > 7776000:
        embed.add_field(name='Too Long Duration', value='You have specified a too long duration!\nMaximum duration is 90 days.')
    else:
        rem = str(f"Timer for {counter} set!")
        embed.add_field(name='Timer Set', value=rem)
        await ctx.send(embed=embed)
        await asyncio.sleep(seconds)
        desc = str(f"Your timer for {counter} has finished.")
        embeded=discord.Embed(title="Timer ",colour=discord.Color.gold(), url="https://timer.com", description=desc, timestamp=datetime.utcnow())

        # Add author, thumbnail, fields, and footer to the embed
        embeded.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

        embeded.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/small-n-flat/24/calendar-512.png")

        embeded.add_field(name="Timer:" , value=counter, inline=False) 
        await ctx.send(embed=embeded)
        return
    await ctx.send(embed=embed)



@client.command(case_insensitive = True, aliases = ["remind", "remindme", "remind_me"])
# @commands.bot_has_permissions(attach_files = True, embed_links = True)
async def reminder(ctx, time, *, reminder):
    print(time)
    print(reminder)
    user = ctx.message.author
    embed = discord.Embed(color=0x55a7f7, timestamp=datetime.utcnow())
    embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
    embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
    seconds = 0
    if reminder is None:
        embed.add_field(name='Warning', value='Please specify what do you want me to remind you about.') # Error message
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
        embed.add_field(name='No Duration',
                        value='Please specify a proper duration, send `help` for more information.')
    elif seconds < 1:
        embed.add_field(name='Too Short Duration',
                        value='You have specified a too short duration!\nMinimum duration is 5 minutes.')
    elif seconds > 7776000:
        embed.add_field(name='Too Long Duration', value='You have specified a too long duration!\nMaximum duration is 90 days.')
    else:
        rem = str(f"Astro will remind you about '{reminder}'' in {counter}.")
        embed.add_field(name='Reminder Set', value=rem)
        await ctx.send(embed=embed)
        await asyncio.sleep(seconds)
        desc = str(f"You asked me to remind you about '{reminder}' {counter} ago.")
        embeded=discord.Embed(title="Reminder ",colour=discord.Color.gold(), url="https://timer.com", description=desc, timestamp=datetime.utcnow())

        # Add author, thumbnail, fields, and footer to the embed
        embeded.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

        embeded.set_thumbnail(url="https://cdn4.iconfinder.com/data/icons/small-n-flat/24/calendar-512.png")

        embeded.add_field(name="Reminder:" , value=reminder.title(), inline=False) 
        await ctx.send(embed=embeded)
        return
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason="Unspecified" ):
  # try:
  #   await member.send("You have been kicked because: " + reason + ". Join here again: https://discord.gg/5vRAW6wRX8")
  # except:
  #   pass
  memb=member
  await member.kick(reason=reason)
  embed=discord.Embed(title=f"Reason: ` {reason} `", color=discord.Color.orange())
  embed.set_author(name=memb.name+" Has Been Kicked!", icon_url=memb.avatar_url)
  await ctx.send(embed=embed)
  # await ctx.send(f'> {member.mention} Has Been Kicked By '+ctx.author.mention)

@client.command(aliases = ['ban'])
@commands.has_permissions(ban_members = True)
# @commands.has_permissions(ban_members = True)
async def _ban(ctx, member : discord.Member, *, reason="Unspecified" ):
  # try:
  #   # await member.send(member.mention+" You Have Been Banned From "+ctx.guild.name+". Reason: " + str(reason) + ". Contact an Admin or Mod or whoever banned you to join again".title())
  # except:
  #   pass
  await ctx.guild.ban(member, reason=reason)
  memb=member
  embed=discord.Embed(title=f"Reason: ` {reason} `", color=discord.Color.orange())
  embed.set_author(name=memb.name+" Has Been Banned!", icon_url=memb.avatar_url)
  await ctx.send(embed=embed)
  # await ctx.send(f'> {member.mention} Has Been Banned By '+ctx.author.mention)


@client.command()
async def joke(ctx):
  await ctx.send(pyjokes.get_joke() + " 😂😂😂")


def downloadSong(url, ctx):
  ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  for file in os.listdir("./"):
    if file.endswith(".mp3"):
      os.rename(file, "song.mp3")
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command(aliases= ['hi','sup','whatsup'])
async def _hi(ctx):
  await ctx.send('> ** Hi! 🚀 WHEEE!!! **')


@client.command(aliases = ['meme','reddit','imgur'])
async def _meme( ctx, *, sub="dankmemes"):
  try:
    meme=""
    reddit = asyncpraw.Reddit(client_id = 'b6zkTf4V07VdCA',
                      client_secret = 'RrI3uvddWXLNj-CneA4Pot65hl36Pw', 
                      user_agent = 'aoztanirBot')
    # print(sub) 
    # subreddit = self.reddit.subreddit(sub.replace(' ', ''))
    # print(sub) 
    # posts = subreddit.hot(limit=10)
    
    try:

      # loop = asyncio.get_event_loop()

      # meme= await loop.run_in_executor(None, lambda:reddit.subreddit(sub.replace(" ", '')).random()) 
      # subreddit = await reddit.subreddit("redditdev", fetch=True)
      subreddit = await reddit.subreddit(sub.replace(" ", ' '))
      # await reddit.close()
      # subreddit = await reddit.subreddit("learnpython")
      # meme = await subreddit.hot(limit=1000)
      # async for element in meme:
      #   meme=element
      arr=[]
      async for submission in subreddit.hot(limit=30):
        arr.append(submission)
      meme= random.choice(arr)
      await reddit.close()
      # for element in meme:
      #   meme=element
      #   break

      # meme=None
      # for element in reddit.subreddit(sub.replace(" ", '')).random_rising(limit=1):
      #   meme = element
      #   # break
    except Exception as e:
      print(e)
      await ctx.send("> Subreddit/images on subreddit not found...")

    if meme.over_18:
      # channel_nsfw = await self.is_nsfw(ctx.message.channel)
      if ctx.channel.is_nsfw():
        pass
      else:
        await ctx.send("> You are not in an NSFW channel.")
        return
    # print(meme.url)
    embed=discord.Embed(title=str(meme.title).title()+" From r/"+sub+" By: "+str(meme.author).title(),colour=discord.Color.gold(), url="https://reddit.com", description="Here is your image:", timestamp=datetime.utcnow())

    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    embed.set_thumbnail(url="https://external-preview.redd.it/iDdntscPf-nfWKqzHRGFmhVxZm4hZgaKe5oyFws-yzA.png?auto=webp&s=38648ef0dc2c3fce76d5e1d8639234d8da0152b2")
    embed.set_image(url=meme.url)

    embed.add_field(name="Image Link:" , value=str(meme.url), inline=False) 

    embed.add_field(name="Image Stats:", value="🚀 "+ str(meme.upvote_ratio*100)+"% | 👍 "+str(meme.score)+" | 💭 "+str(meme.num_comments), inline=False)
    await ctx.send(embed=embed)
  except:
    pass
  

@client.command(aliases= ['unban'])
@commands.has_permissions(ban_members = True)
@commands.has_permissions(ban_members = True)
async def _unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} Has Been Unbanned By '+ctx.author.mention)

# @client.event
# async def on_member_join(ctx, member):
#     # print(f'{member} has joined the ship :D !')
#     await ctx.send(f'{member} Has Joined The Server.')

# @client.event
# async def on_member_remove(ctx, member):
#     # print(f'{member} went out the airlock :D !')
#     await ctx.send(f'> {member} Has Left The Server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'> Pong! {round(client.latency*100)}ms!')


async def didyouknow(ctx):
  n = random.randint(1,10)
  if n==1:
    embed=discord.Embed(title="**ℹ️ Did you know**",description="Astro has a beta bot, invite him [here](https://discord.com/api/oauth2/authorize?client_id=841760295432880168&permissions=8&scope=bot%20applications.commands)", color = discord.Color.red())
    return await ctx.send(embed=embed, delete_after=10)


@client.event
async def on_command_error(ctx, error):
    if "not connected to voice" in str(error).lower():
      await ctx.send(f"> Sorry {ctx.author.mention} Astro Doesnt Have Permissions To Connect To The Voice Channel You Are In.")
      return
    if "cannot unpack" in str(error).lower():
      # # print("lmao")
      # await ctx.send("> Please Do Not Ask Astro To Play Playlists/Livestreams.")
      return
    if "failed for parameter" in str(error).lower():
      # print("lmao")
      await ctx.send("> Please Use The Correct Type For A Value.")
      return
    if "drm protected" in str(error).lower():
      # print("lmao")
      await playtheurl(ctx)
      return
    if "Unable To Download" in str(error).lower():
      # print("lmao")
      await playtheurl(ctx)
      return
    if "runtimeerror" in str(error).lower():
      await playtheurl(ctx)
      return
    if "already playing audio" in str(error).lower():
      await playtheurl(ctx)
      return
      await playtheurl(ctx)
    if "could not parse youtube response" in str(error).lower():
      await playtheurl(ctx)
      return
      print("lmao")
      await play(ctx)
      
    if "Unable To Download" in str(error):
      await play(ctx)
    if isinstance(error, commands.CommandOnCooldown):
      embed=discord.Embed(description="**⏰ Woah! This Command Is On Cooldown! Try Again In {:.2f}s!**".format(error.retry_after), color = discord.Color.red())
      return await ctx.send(embed=embed, delete_after=5)
    if isinstance(error, IncorrectChannelError):
      return
    if "ZeroConnectedNodes" in str(error) or "UnboundLocalError" in str(error):
      # pass
      client.add_cog(Music(client))
    # if "Cannot send an empty message" in str(error):
    #   embed=discord.Embed(description="**Currently Nothing Is Playing**".title(), color = discord.Color.red())
      # return await ctx.send(embed=embed, delete_after=10)
    if isinstance(error, NoChannelProvided):
      embed=discord.Embed(description="**You must be in a voice channel**".title(), color = discord.Color.red())
      return await ctx.send(embed=embed, delete_after=10)
      # return await ctx.send('')
    if isinstance(error, discord.ext.commands.MissingRequiredArgument):
      await ctx.send("> **Please include all required parts of a command!**")
    elif isinstance(error, discord.ext.commands.MissingPermissions):
      await ctx.send("> **Sorry "+ctx.author.mention+" It Looks Like You Dont Have The Permissions To Run This Command!**")
    elif isinstance(error, discord.ext.commands.BotMissingPermissions):
      await ctx.send("> **Sorry "+ctx.author.mention+" Astro Does Not Have The Permissions To Complete This Action!**")
    # elif "too many requests" in str(error).lower():
    #   await ctx.send("> **Hi "+ctx.author.mention+", youtube is having some momentary troubles, please rerun the command!**".title())
    # elif "clientexception" in str(error).lower():
    #   await ctx.send("> **Sorry "+ctx.author.mention+" This Process Is Already Running!"+"\n\nThe Error Incurred Is Below: \n\n`"+str(error)+"`**")
    elif isinstance(error, discord.ext.commands.CommandNotFound):
      pass
      # await ctx.send("> Sorry "+ctx.author.mention+" That Command Does Not Exist.")
    else:
      if 'missing permissions' in str(error).lower():
        await ctx.send("> **Sorry "+ctx.author.mention+" Astro Does Not Have The Permissions To Complete This Action!**")
        return
      # await ctx.send("> Sorry "+ctx.author.mention+" It Looks Like This Command Is Not Working As Of Now. Go To "+astroSite+" For More Info Or To Report This Problem.\n\nThe Error Incurred Is Below: \n\n`"+str(error)+"`")
      print(str(error))
      embed=discord.Embed(title="An Error Occured.".title(), color = discord.Color.red())
      await ctx.send(embed=embed, delete_after=5)
      # await ctx.send("> An Error Occured")
  
@client.command()
async def bye(ctx):
  await ctx.send("Bye!")


@client.command(aliases = ["news", "headlines", 'headline'])
async def _news(ctx, amount):
    # await ctx.send("How many headlines?")
    # msg = await client.wait_for('message')
    hNum = int(amount)
    if hNum > 16:
        await ctx.send("Headline amounts cannot be over 15")
        return
    news_url="https://news.google.com/news/rss"
    Client=urlopen(news_url)
    xml_page=Client.read()
    Client.close()
    soup_page=soup(xml_page,"lxml")
    news_list=soup_page.findAll("item")
    hNum=int(hNum)
    try:
        hNum += 1
    except TypeError:
        hNum=6

    embed=discord.Embed(title="Your "+str(hNum)+ " Headlines Are Ready!",colour=discord.Color.gold(), url="https://news.google.com", description="Here are your headlines:", timestamp=datetime.utcnow())

    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/0/0b/Google_News_icon.png")

    headlineNum = 0
    for news in news_list[:int(hNum-1)]:
      headlineNum = headlineNum+1
      embed.add_field(name="Headline "+ str(headlineNum) , value=str(news.title.text), inline=False) 

    await ctx.send(embed=embed)
    
    # for news in news_list[:int(hNum-1)]:
    #     await ctx.send(news.title.text)




@client.command(aliases = ["googlelinks", "Searchlinks"])
async def _googleLinks(ctx, *, searchstr: str):
  query = searchstr
  embed=discord.Embed(title="Your 10 Results Are Ready!",colour=discord.Color.gold(), url="https://google.com", description="Here are your results:", timestamp=datetime.utcnow())

    # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url="http://assets.stickpng.com/images/5847f9cbcef1014c0b5e48c8.png")

  headlineNum = 0
  for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    headlineNum = headlineNum+1
    embed.add_field(name="Result "+ str(headlineNum) + ":", value=str(j), inline=False) 

  await ctx.send(embed=embed)
  # for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
  #     await ctx.send(j) 

@client.command(aliases = ["google", "Search"])
async def _google(ctx, *, searchstr: str):
  query = searchstr
  results = []
  for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
      results.append(j)
    
  embed=discord.Embed(title="Your Result Is Ready!",colour=discord.Color.gold(), url="https://google.com", description="Below is a link that could help you out", timestamp=datetime.utcnow())

    # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url="http://assets.stickpng.com/images/5847f9cbcef1014c0b5e48c8.png")
  embed.add_field(name="The 1st URL Found on Google:" , value=results[0], inline=False)
  embed.add_field(name="To Get 10 Links:" , value="Use the googlelinks command with your query!", inline=False)

  await ctx.send(embed=embed)
  # await ctx.send("Here is a link that could help you out: " +results[0]+ "\nUse the googlelinks with the same query command for 10 similar links!")

# @client.command()
# # @commands.has_permissions(administrator=True, manage_messages=True)
# async def clear(ctx):
#   await ctx.send("Please use ..clear or a keyword in front of clear instead of just clear, this is to prevent the clearing of messages unintentionally.")

# @client.command(aliases = ['keyword', 'Keywords','keywords','Keyword', 'prefixes', 'Prefixes'])
# async def _keyword(ctx):
#   await ctx.send("> KEYWORDS/COMMAND PREFIXES:   '.',  'pls', 'astro', '', ' '. ")


@client.command(aliases = ["purge", "Clear"])
# @commands.has_permissions( manage_messages=True)
async def _clear(ctx, amount):
  try:
    if str(amount).lower()=="queue":
      command = client.get_command('clearqueue')
      ctx.command = command
      return await client.invoke(ctx)
  except:
    pass 
  if ctx.message.author.server_permissions.administrator:
    await ctx.channel.purge(limit = int(amount)+1)
  else:
    raise discord.ext.commands.MissingPermissions
  


@client.command(aliases = ['time', 'Now'])
async def _time(ctx, inside, city):
  # city.replace('in', '');
  print(city)
  if "europe" in city.lower() or "athens" in city.lower():
    city = "Europe/Athens"
  if "asia" in city.lower() or "kolkata" in city.lower():
    city = "Asia/Kolkata"
  if "america" in city.lower() or "new york" in city.lower() or "new_york" in city.lower() or "newyork" in city.lower():
    city = "America/New_York"
  if "us" in city.lower() or "central" in city.lower():
    city = "US/Central"
  if "africa" in city.lower() or "maseru" in city.lower():
    city = "Africa/Maseru"

  try:
    xyz = pytz.timezone(city)
  except:
    await ctx.send("You have not named a valid time zone, please try again and name one of these Asia/Kolkata, America/New_York, Africa/Maseru, US/Central, Europe/Athens.")
  current_time = datetime.now(xyz) 
  print(current_time)  
    #### Create the initial embed object ####
  embed=discord.Embed(title="Current Time", url="https://time.is/", description="This time is the current time in "+ str(xyz), color=discord.Color.gold(), timestamp=datetime.utcnow())

  # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url="https://www.patriotsoftware.com/wp-content/uploads/2017/06/time-and-half-1.jpg")

  embed.add_field(name="Time in "+ str(xyz), value=str(current_time.hour)+":"+str(current_time.minute), inline=False) 

  await ctx.send(embed=embed)

@client.command(aliases = ['Who are you?', 'who','creator', 'purpose'])
async def _who(ctx):
    await ctx.send("Heya,\nI was created by Team Astro More About Them Here: https://teamastro.ml/")

@client.command(aliases = ['weather','temperature'])
async def _weather(ctx, *, city):
    api_key = "d4b4b3505a923d073e0e9ffd3cd1a606"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city[3:]
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url) 
    x = response.json() 
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"] 
        weather_description = z[0]["description"]
        
        embed=discord.Embed(title="Weather In "+city_name.title(), url="https://weather.com", description="Weather information for "+city_name.title(), color=discord.Color.gold(), timestamp=datetime.utcnow())

      # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

        embed.set_thumbnail(url="https://icons-for-free.com/iconfiles/png/512/fog+foggy+weather+icon-1320196634851598977.png")

        embed.add_field(name="Temperature(F):", value= str(int((current_temperature-273.15) * (9/5) +32)) + " Degrees(F)", inline=False) 
        embed.add_field(name="Atmospheric Pressure(hPa)", value= str(current_pressure) +" hPa", inline=False)
        embed.add_field(name="Humidity Percentage", value=str(current_humidiy) + "%", inline=False)
        embed.add_field(name="Weather Description:", value=str(weather_description).title(), inline=False)

        # embed.set_footer(text="This is the footer. It contains text at the  bottom of the embed")
        await ctx.send(embed=embed)

    else:
        await ctx.send(" City Not Found ")

@client.command(aliases = ['Wiki'])
async def _wiki(ctx, *, topic):
    ny = wikipedia.page(topic)
    
    
    embed=discord.Embed(title="Wikipedia Results For "+topic.title(), url="https://wikipedia.com", description="This is the result of your query.", color=discord.Color.gold(), timestamp=datetime.utcnow())

  # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    embed.set_thumbnail(url="http://pngimg.com/uploads/wikipedia/wikipedia_PNG12.png")

    embed.add_field(name="Wikipedia Result:", value=ny.content[:500]+"...", inline=False) 

    await ctx.send(embed=embed)



# @client.command()
async def listqueueOld(ctx):
    from datetime import timedelta
    queueList, names, durations,thumbnails, links, requestors = await accessQueue(ctx.guild.id, "all")
    # nameList = await accessNames(ctx.guild.id)
    # msg=await ctx.send(queueList)
    embed = discord.Embed(title="Queue For "+ctx.guild.name.title(), colour=discord.Color.teal(), timestamp=datetime.utcnow())
    # embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")
    info = await accessPlaying(ctx.guild.id)
    try:
      pass
      embed.set_thumbnail(url=f"{thumbnails[0]}")
    except:
      pass
      # embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    # embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
    fmt=""
    desc=""
    
    try:
      voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
      if voice.is_playing():
        # embed.set_thumbnail(url=f"{thumbnail}")
        # fmt = '\n'.join(f"`{(upcoming.index(_)) + 1}.` [{_['title']}]({_['webpage_url']}) | ` {duration} Requested by: {_['requester']}`\n" for _ in upcoming)
        song=info[0]
        link=info[4]
        duration=info[2]
        thumbnail=info[3]
        setter = info[5]
        memb = client.get_user(setter)
        conversion = timedelta(seconds=int(duration))
        duration = str(conversion)
        desc = f"\n__Now Playing__:\n[{song[:30]}...]({link}) | ` {duration} ` | Requested By: {memb.mention}"
    except:
      pass
    
    i=0
    j=0
    if len(names)>0:
      desc+="\n\n__Up Next:__\n"
    embed = discord.Embed(title="Queue For "+ctx.guild.name.title(),description = desc,colour=discord.Color.teal())
    for element in names:
      i=i+1
      try:
        conversion = timedelta(seconds=int(durations[j]))
        duration = str(conversion)
        memb = client.get_user(requestors[j])
        fmt=f"[{element[:30]}...]({links[j]}) | ` {duration} ` | Requested By: {memb.mention}\n"
        embed.add_field(name=f"`{i}.`", value = fmt, inline=False)
        # embed.add_field(name="Song Number: "+str(i), value="Name: "+"["+element+"]("+queueList[j]+")  | "+duration, inline=False)
      except Exception as e:
        print(e)
      j=j+1
    
    # try:
    await ctx.send(embed=embed)
    # except:
    #   embeda = discord.Embed(title="Queue For "+ctx.guild.name.title(), colour=discord.Color.red(), timestamp=datetime.utcnow())
    #   embeda.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")
    #   try:
    #     embeda.set_thumbnail(url=f"{thumbnails[0]}")
    #   except:
    #     embeda.set_thumbnail(url=f"{ctx.guild.icon_url}")
    #   embeda.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
    #   i=0
    #   j=0
    #   for element in names:
    #     i=i+1
    #     try:
    #       conversion = timedelta(seconds=int(durations[j]))
    #       duration = str(conversion)
    #       embeda.add_field(name="Song Number: "+str(i), value="Name: "+element+" | "+duration, inline=False)
    #     except Exception as e:
    #       print(e)
    #     j=j+1
    #     await ctx.send(embed=embeda)

    # await msg.delete()

@client.command(aliases = ['Percentage','Percent','amount'])
async def _percentage(ctx, member: discord.Member,*, question):
  author = ctx.message.author
  author_name = author.name
  if "?" in question:
    question = question.remove("?")
  # await ctx.send(question.title())
  embed=discord.Embed(title="Percentage " + question.title()+" For "+member.name.title(), description= "Asked By: "+str(author_name).title(), color=discord.Color.gold(), timestamp=datetime.utcnow())

    # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url="https://static.wikia.nocookie.net/fortnite_esports_gamepedia_en/images/f/ff/Onepercent.png/revision/latest?cb=20201110033035")

  embed.add_field(name="Percentage "+ question.title()+":", value = str(rando.randint(1,100))+"%" , inline=False)
  embed.add_field(name="Can I Trust This Answer?", value= "These amounts are 100% correct and are the result of a complex AI algorithm that analyzes your activities on discord." , inline=False)
  # embed.add_field(name="URL:", value = final_url , inline=False) 

  await ctx.send(embed = embed)
@client.command(aliases = ['whencanyoucome','when'])
async def polltimes(ctx, *, question):
  author = ctx.message.author
  author_name = author.name
  if " " not in question and ", " not in question and "," not in question:
    await ctx.send("> You have not included the times. Remember seperate your times like so: 1:30, 1, 2, etc... Make sure to use commas or spaces. ")
    return
  questiona = question
  if "," in question and ", " not in question:
    questiona = question.replace(',', ', ')
  if " " in question and ", " not in question:
    questiona = question.replace(' ', ', ')
  print(questiona)
  questionArr = questiona.split(", ")
  for i in range(len(questionArr)):
    if ":" not in questionArr[i]:
      questionArr[i] = questionArr[i]+":00"
  # questiona = ""
  for i in range(len(questionArr)):
    if i != len(questionArr)-1:
      questiona = questiona + questionArr[i]+", "
    else:
      questiona = questiona + questionArr[i]

  embed=discord.Embed(title="Polling Times: " + questiona.title(), description= "Asked By: "+str(author_name).title(), color=0xFF5733, timestamp=datetime.utcnow())

  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    # Add rs/608778878835621900/76e69643d799ee584dd46afa91127105.webp")

  embed.set_thumbnail(url="https://icons.iconarchive.com/icons/dtafalonso/android-lollipop/512/Clock-icon.png")

  embed.add_field(name="Times:  ", value= questiona.title() , inline=False)
  embed.add_field(name="Remember:", value= "All polling amounts must be subtracted by one for each, since it was reacted to once already by Astro." , inline=False)
  # embed.add_field(name="URL:", value = final_url , inline=False) 

  await ctx.send(embed = embed)
  
  for element in questionArr:
    embed=discord.Embed(title="Time: " + element.title(), color=0xFF5733)
    messageSent = await ctx.send(embed = embed)
    await messageSent.add_reaction("✅")


@client.command()
async def poll(ctx,time,*, question):
  seconds=0
  if time.lower().endswith("d"):
      seconds += int(time[:-1]) * 60 * 60 * 24
      counter = f"{seconds // 60 // 60 // 24} days"
  if time.lower().endswith("h"):
      seconds += int(time[:-1]) * 60 * 60
      counter = f"{seconds // 60 // 60} hours"
  elif time.lower().endswith("m"):
      seconds += int(time[:-1]) * 60
      counter = f"{seconds // 60} minutes"
  elif time.lower().endswith("s"):
      seconds += int(time[:-1])
      counter = f"{seconds} seconds"
  if seconds==0:
    await ctx.send("> Improper Time. Please Specify A Time Ending In s, m, or d.")
    return
  author = ctx.message.author
  author_name = author.name
  if "?" not in question:
    question = question +"?"
  # await ctx.send(question.title())
  embed=discord.Embed(title="Poll: " + question.title(), description= "Asked By: "+str(author_name).title(), color=0xFF5733, timestamp=datetime.utcnow())

    # Add rs/608778878835621900/76e69643d799ee584dd46afa91127105.webp")

  embed.set_thumbnail(url="https://image.flaticon.com/icons/png/512/1946/1946385.png")
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.add_field(name="Question:", value= question.title() , inline=False)
  embed.add_field(name="Remember:", value= "Polling amounts must be subtracted by one for each, since it was reacted to once already by Astro." , inline=False)
  # embed.add_field(name="URL:", value = final_url , inline=False) 

  messageSent = await ctx.send(embed = embed)
  await messageSent.add_reaction("✅")
  await messageSent.add_reaction("❌")
  await asyncio.sleep(seconds)
  msg = await ctx.channel.fetch_message(messageSent.id)

  check_marks = len(await msg.reactions[0].users().flatten())
  x_marks = len(await msg.reactions[1].users().flatten())
  embed=discord.Embed(title="Results For: " + question.title(), description= "Asked By: "+str(author_name).title(), color=0xFF5733, timestamp=datetime.utcnow())

    # Add rs/608778878835621900/76e69643d799ee584dd46afa91127105.webp")

  embed.set_thumbnail(url="https://image.flaticon.com/icons/png/512/1946/1946385.png")
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.add_field(name="✅", value= str(check_marks) , inline=False)
  embed.add_field(name="❌", value= str(x_marks) , inline=False)
  await ctx.send(embed=embed)
  # embed.add_field(name="URL:", value = final_url , inline=False) 


# @client.command(aliases=['radio', 'stream'])
# async def Radio(ctx, url: str = 'http://stream.radioparadise.com/rock-128'):
#   try:
#     voiceChannel = ctx.message.author.voice.channel
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#   except:
#     pass
#   voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#   try:
#     if voice.is_playing() and voiceChannel!=voice.channel:
#       await ctx.send("> "+ctx.author.mention+" Someone Else Is Already Listnening To Music Join That Channel To Listen To Music Too. The Voice Channel is: "+voice.channel.mention)
#       return
      
#   except:
#     pass    # try:
#     #     voice_client = ctx.message.guild.voice_client
#     #     await voice_client.disconnect()
#     # except AttributeError:
#     #     pass

#     if not ctx.message.author.voice:
#         await ctx.send("> You are not connected to a voice channel.".title())
#         return

#     else:
#       try:
#       #   if not voice.is_connected():
#         await voiceChannel.connect()
#       except:
#         pass
#       # try:
#   channel = ctx.author.voice.channel
#   global player
#   try:
#       player = await channel.connect()
#   except:
#       pass
#   voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#   voice.stop()
#   # FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
#   # ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
#   voice.play( await YTDLSource.from_url(url, stream=True))
  
#   # FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'}
#   # video, source = await search(url)

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn, -aq q (low) -acodec copy -vcodec copy -copyts'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):

        data = ytdl.extract_info(url, download=not stream)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        # filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(data['url']), data=data)


@client.command(aliases=['Nameserver'])
@commands.has_permissions(administrator=True)
async def serverName(ctx,*, newname: str=None):
  if newname == None:
    await ctx.send("**Please Provide A Name**")
    return
  else:
    await ctx.guild.edit(name=newname)
    await serverinfo(ctx)


@client.command(aliases=['info','Server'])
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description="Name: "+name+" | Description: "+description,
      color=discord.Color.gold()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.send(embed=embed)

# @client.command()
async def resumeOld(ctx, status=None):
  if status !="silent":
    state = await checkIfPart(ctx)
    if not state:
      return
  try:
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice==None:
      embed=discord.Embed(title="Audio Is Not Playing!".title(), color = discord.Color.red())
      await ctx.send(embed=embed)
    if voice.is_paused():
        voice.resume()
        embed=discord.Embed(title="⏯ Resumed!".title(), color = discord.Color.dark_blue())
        await ctx.send(embed=embed)
        # await ctx.send("> :play_pause: Resumed!")
    else:
      embed=discord.Embed(title="Audio Is Not Paused!".title(), color = discord.Color.red())
      await ctx.send(embed=embed)
  except:
    embed=discord.Embed(title="Audio Is Not Playing!".title(), color = discord.Color.red())
    await ctx.send(embed=embed)


def is_integer(n):
  try:
      int(n)
  except ValueError:
      return False
  else:
      return True

# @client.command(aliases=['vol', 'v'])
async def volumeOld(ctx, volumeAmount: int=None):
  # if is_integer(volumeAmount)==False:
  #   await ctx.send("> Please Type A Number.")
  #   return

  state = await checkIfPart(ctx)
  if not state:
    embed=discord.Embed(title="Start Playing Music, Then Set The Volume!".title(), color = discord.Color.red())
    await ctx.send(embed=embed)
    return
  vol = ctx.voice_client.source.volume
  if volumeAmount==None:
    embed=discord.Embed(title=f"Volume Set At {vol*100}% Currently", color = discord.Color.teal())
    await ctx.send(embed=embed)
    return
  if volumeAmount>100 or volumeAmount<1:
    embed=discord.Embed(title="Please Specify A Volume That Is Between 1 and 100".title(), color = discord.Color.red())
    await ctx.send(embed=embed)
    # await ctx.send("> "+ctx.author.mention+" Please Specify A Volume That Is Between 1 and 100")
    return
  # try:
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice is None:
    embed=discord.Embed(title="Astro Is Not Connected To A Voice Channel".title(), color = discord.Color.red())
    await ctx.send(embed=embed)
    return
  # if VOICESAVE is None:
  #   await ctx.send("> Play Something Before Setting The Volume")
  #   return
  # voice.source.volume = float(volumeAmount/10)
  # print(discord.PCMVolumeTransformer(voice.source))
  vol = ctx.voice_client.source.volume
  ctx.voice_client.source.volume = volumeAmount / 100
  print(volumeAmount)
  await accessVolume(ctx.guild.id, volumeAmount)
  # voice.source = discord.PCMVolumeTransformer(voice.source, volume=float(volumeAmount/100))
  embed=discord.Embed(title=f"Volume Set From {vol*100}% To "+str(volumeAmount)+"% By "+ctx.author.name, color = discord.Color.teal())
  await ctx.send(embed=embed)
  # await ctx.send("> Volume Set To "+str(volumeAmount)+"%")
  # except:
  #   pass
  # discord.PCMVolumeTransformer(voice.source, volume=1.0)

async def accessPlaying(server, link=None,song=None, duration=None, thumbnail=None, weburl=None, requestor=None):
  with open("playing.json","r") as f:
    users = json.load(f)
  if song != None:
    if str(server) in users:
      users[str(server)]["song"]=song
      users[str(server)]["link"]=link
      users[str(server)]["duration"]=duration
      users[str(server)]["thumbnail"]=thumbnail
      users[str(server)]["weburl"]=weburl
      users[str(server)]["requestor"]=requestor
    else:
      users[str(server)]= {}
      users[str(server)]["song"]=song
      users[str(server)]["link"]=link
      users[str(server)]["duration"]=duration
      users[str(server)]["thumbnail"]=thumbnail
      users[str(server)]["weburl"]=weburl
      users[str(server)]["requestor"]=requestor
    with open("playing.json","w") as f:
      json.dump(users,f)
    return
  if str(server) in users:
    return users[str(server)]["song"], users[str(server)]["link"], users[str(server)]["duration"], users[str(server)]["thumbnail"], users[str(server)]["weburl"], users[str(server)]["requestor"]
  else:
    users[str(server)]= {}
    users[str(server)]["song"]=None
    users[str(server)]["link"]=None
    users[str(server)]["duration"]=None
    users[str(server)]["thumbnail"]=None
    users[str(server)]["weburl"]=None
    users[str(server)]["requestor"]=None
  with open("playing.json","w") as f:
    json.dump(users,f)

# @client.command()
async def playingOld(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  try:
    if not voice.is_playing() or voice==None:
      embed=discord.Embed(title="Currently no audio is playing!".title(), color = discord.Color.red())
      await ctx.send(embed=embed)
      return     
  except Exception as e:
    print(e)
    embed=discord.Embed(title="Currently no audio is playing!".title(), color = discord.Color.red())
    await ctx.send(embed=embed)
    return
  info = await accessPlaying(ctx.guild.id)
  song=info[0]
  link=info[1]
  duration=info[2]
  thumbnail=info[3]
  url=info[4]
  requestor=info[5]
  # print(song)
  # print(link)
  # print(duration)
  from datetime import timedelta
  conversion = timedelta(seconds=int(duration))
  duration = str(conversion)
  memb = client.get_user(requestor)
  fmt=f"[{song[:30]}...]({url}) | ` {duration} ` | Requested by: {memb.mention}\n"
  # embed.add_field(name=f"`{i}.`", value = fmt)
  embed=discord.Embed(title="Now Playing",description=fmt, color=0xFF5733)

  # Add author, thumbnail, fields, and footer to the embed


  embed.set_thumbnail(url=thumbnail)

  # embed.add_field(name="Song: ", value="["+ song+"]("+link+")" , inline=False)
  # embed.add_field(name="Duration:", value = duration , inline=False) 
  
  await ctx.send(embed = embed)

# @client.command(aliases=['seek','moveto','Move','wind','Wind','Moveto','rewind','Rewind'])
async def moveOld(ctx, timeSkip:int=0):
  if not isinstance(int(timeSkip), int):
    # await ctx.send("> Please Type A Number Representing The Seconds.")
    embed=discord.Embed(title="Please Type A Number Representing The Seconds!".title(), color = discord.Color.red())
    await ctx.send(embed=embed)
    return
  

  # await play(ctx)
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  try:
    if not voice.is_playing() or voice==None:
      embed=discord.Embed(title="Currently Nothing is Playing!".title(), color = discord.Color.red())
      await ctx.send(embed=embed)
      return     
  except Exception as e:
    print(e)
    
    embed=discord.Embed(title="Currently Nothing is Playing!".title(), color = discord.Color.red())
    await ctx.send(embed=embed)
    return
  info = await accessPlaying(ctx.guild.id)
  final_url= str(info[1])
  title= str(info[0])
  thumbnail = info[3]
  duration = info[2]
  link= info[4]
  requestor=info[5]
  # print(f"MOVE INFO: {title} {final_url}")

  if int(timeSkip)==0:
    voice.stop()
    await queueSong(ctx.guild.id, final_url, title,duration, thumbnail,link, requestor,0)
    embed=discord.Embed(title="⏺ Rewinding!".title(), color = discord.Color.teal())
    await ctx.send(embed=embed)
    await playtheurl(ctx,int(timeSkip))
    return
  try:
    if int(timeSkip)>(int(info[2])-5):
      # await queueSong(ctx.guild.id, final_url, title,duration, thumbnail,0)
      embed=discord.Embed(title="You Cannot Skip To A Time Stamp That Is Longer Than 5 Seconds Before The Song's End!".title(), color = discord.Color.red())
      await ctx.send(embed=embed)
      # await ctx.send("> You Cannot Skip To A Time Stamp That Is Longer Than 5 Seconds Before The Song's End.")
      return
  except:
    video, source = await search(title,ctx, client.loop)

    if int(timeSkip)>(int(video["duration"])-5):
      # await queueSong(ctx.guild.id, final_url, title,duration, thumbnail,0)
      embed=discord.Embed(title="You Cannot Skip To A Time Stamp That Is Longer Than 5 Seconds Before The Song's End!".title(), color = discord.Color.red())
      await ctx.send(embed=embed)
      # await ctx.send("> You Cannot Skip To A Time Stamp That Is Longer Than 5 Seconds Before The Song's End.")
      return
  
  await queueSong(ctx.guild.id, final_url, title, duration, thumbnail,link, requestor,0)
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_playing():
    voice.stop()
  # # await voice.stop()
  # await queueSong(ctx.guild.id, final_url, title,duration, thumbnail,0)
  conversion = timedelta(seconds=int(timeSkip))
  duration = str(conversion)
  embed=discord.Embed(title="⏩ Moving To "+str(duration), color = discord.Color.teal())
  await ctx.send(embed=embed)
  # await ctx.send("Moving To: "+str(timeSkip))
  await playtheurl(ctx,int(timeSkip))

# @client.command()
# async def prefix(ctx, prefix:str):

#   try:
#     with open('prefixes.json', 'r') as f: ##we open and read the prefixes.json, assuming it's in the same file
#       prefixes = json.load(f) #load the json as prefixes
#     prefixes[str(ctx.guild.id)]=prefix
#     with open("prefixes.json","w") as f:
#       json.dump(prefixes,f)
#   except:
#     pass
  
# async def playlist( arg, ctx=None):
#   from youtube_dl import YoutubeDL
#   with YoutubeDL:
#     result = YoutubeDL.extract_info \
#     ("https://www.youtube.com/playlist?list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10",
#     download=False) #We just want to extract the info

#     if 'entries' in result:
#         # Can be a playlist or a list of videos
#         video = result['entries']

#         #loops entries to grab each video_url
#         for i, item in enumerate(video):
#             video = result['entries'][i]
#             print(video)
  # try:
  #   from youtube_dl import YoutubeDL
  #   with YoutubeDL({'format': 'bestaudio',
  #   'noplaylist':'True'
  #   }) as ydl:
  #     try: requests.get(arg)
  #     except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
  #     else: info = ydl.extract_info(arg, download=False)
  #   return (info, info['formats'][0]['url'])
  # except Exception as e:
  #   # print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"+str(e))
  #   try:
  #     if "format not available" in str(e).lower():
  #       await ctx.send("> Live-streams Cannot Be Played.")
  #       with open("queue.json","r") as f:
  #         users = json.load(f)
  #       if str(ctx.guild.id) in users:
  #         try:
  #           users[str(ctx.guild.id)]["queue"].pop(0)
  #           users[str(ctx.guild.id)]["name"].pop(0)
  #         except:
  #           return
  #       else:
  #         pass

  #       with open("queue.json","w") as f:
  #         json.dump(users,f)
  #       return
  #   except:
  #     return
  #   if (ctx!=None):
  #     # await asyncio.sleep(1.5)
  #     await playtheurl(ctx)


# def search(arg):
#   from youtube_dl import YoutubeDL
#   with YoutubeDL({'format': 'bestaudio', 'noplaylist':'True'}) as ydl:
#     try: requests.get(arg)
#     except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
#     else: info = ydl.extract_info(arg, download=False)
#   return (info, info['formats'][0]['url'])




async def previousQueue(server ,url=None, title=None, duration=None, thumbnail=None, weburl=None, requestor=None):
  with open("previous.json","r") as f:
    users = json.load(f)
  if str(server) in users:
    if title!=None:
      users[str(server)]["previous"].insert(0,url)
      users[str(server)]["names"].insert(0,title)
      users[str(server)]["durations"].insert(0,duration)
      users[str(server)]["thumbnails"].insert(0,thumbnail)
      users[str(server)]["links"].insert(0,weburl)
      users[str(server)]["requestors"].insert(0,requestor)
      
  else:
    users[str(server)]= {}
    users[str(server)]["previous"]=[]
    users[str(server)]["names"]=[]
    users[str(server)]["durations"]=[]
    users[str(server)]["thumbnails"]=[]
    users[str(server)]["links"]=[]
    users[str(server)]["requestors"]=[]
    if title !=None:
      users[str(server)]["previous"].insert(0,url)
      users[str(server)]["names"].insert(0,title)
      users[str(server)]["durations"].insert(0,duration)
      users[str(server)]["thumbnails"].insert(0,thumbnail)
      users[str(server)]["links"].insert(0,weburl)
      users[str(server)]["requestors"].insert(0,requestor)
  with open("previous.json","w") as f:
    json.dump(users,f)
  lenght = len(users[str(server)]["previous"])
  try:
    return users[str(server)]["previous"][1], users[str(server)]["names"][1],users[str(server)]["durations"][1], users[str(server)]["thumbnails"][1], users[str(server)]["links"][1], users[str(server)]["requestors"][1]
  except Exception as e:
    print(e)
    try:
      return users[str(server)]["previous"][0], users[str(server)]["names"][0],users[str(server)]["durations"][0], users[str(server)]["thumbnails"][0],  users[str(server)]["links"][0], users[str(server)]["requestors"][0]
    except:
      return -1,-1
  # return True

@client.command()
async def previous(ctx):
  state=False
  try:
    url, title, duration, thumbnail, link, requestor = await previousQueue(ctx.guild.id)
    with open("previous.json","r") as f:
      users = json.load(f)
    server=ctx.guild.id
    if str(server) in users:
      if title!=None:
        users[str(server)]["previous"].pop(0)
        users[str(server)]["names"].pop(0)
        users[str(server)]["durations"].pop(0)
        users[str(server)]["thumbnails"].pop(0)
        users[str(server)]["links"].pop(0)
        users[str(server)]["requestors"].pop(0)
    with open("previous.json","w") as f:
      json.dump(users,f)
    if url ==-1:
      embed=discord.Embed(title="Play Something First", color = discord.Color.red())
      await ctx.send(embed=embed)
      # await ctx.send("> Play Something First.")
      return
    embed=discord.Embed(title="⏩ Going Back!".title(), color = discord.Color.orange())
    await ctx.send(embed=embed)
    await queueSong(ctx.guild.id,url,title,duration,thumbnail,"https://google.com",requestor,0)
    state=True

  except:
    embed=discord.Embed(title="✋ You Cant Go Back Any Further!".title(), color = discord.Color.red())
    await ctx.send(embed=embed)
  if state==True:
    await play(ctx)

# async def playlist():
#   from youtube_dl import YoutubeDL
#   with YoutubeDL({'format': 'bestaudio', 'playlist-end': 20,'yesplaylist':'True'}) as ydl:
#     result = ydl.extract_info(f"https://www.youtube.com/watch?v=oygrmJFKYZY&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=2&ab_channel=DuaLipa", download=False)
#     if 'entries' in result:
#       video = result['entries']
#       #loops entries to grab each video_url
#       for i, item in enumerate(video):
#         video = result['entries'][i]
#         print(video)
    

# async def search( arg, ctx=None,loop=None ):
#   loop = loop or asyncio.get_event_loop()
#   # data = ytdl.extract_info(url, download=not stream)

#   #       if 'entries' in data:
#   #           # take first item from a playlist
#   #           data = data['entries'][0]
#   try:
#     async with ctx.typing():
#       from youtube_dl import YoutubeDL
#       with YoutubeDL({'format': 'bestaudio', 'playlist-end': 20,         
#       # 'noplaylist':'True'
#       }) as ydl:
#         try: requests.get(arg)
#         except: info = await loop.run_in_executor(None, lambda:ytdl.extract_info(arg, download=False, process=True)['entries'][0])
#         # except: info = ytdl.extract_info(arg, download=False)['entries'][0]
#         # except: info = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
#         else: info =  await loop.run_in_executor(None, lambda:ytdl.extract_info(arg, download=False,process=True))
#         # else: info = ydl.extract_info(arg, download=False)
#       # print(info)
#       return (info, info['formats'][0]['url'])
#   except Exception as e:
#     # print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"+str(e))
#     if "unsupported url" in str(e).lower():
#       embed=discord.Embed(title="This Is An Unsupported Audio Source!", color = discord.Color.red())
#       await ctx.send(embed=embed)
#     try:
      
#       if "format not available" in str(e).lower() or "403" in str(e).lower():
#         return
#         # embed=discord.Embed(title="Can!", color = discord.Color.red())
#         # await ctx.send(embed=embed)
#         # with open("queue.json","r") as f:
#         #   users = json.load(f)
#         # if str(ctx.guild.id) in users:
#         #   try:
#         #     users[str(ctx.guild.id)]["queue"].pop(0)
#         #     users[str(ctx.guild.id)]["name"].pop(0)
#         #     users[str(ctx.guild.id)]["thumbnail"].pop(0)
#         #     users[str(ctx.guild.id)]["link"].pop(0)
#         #     users[str(ctx.guild.id)]["requestor"].pop(0)
#         #     users[str(ctx.guild.id)]["duration"].pop(0)
#         #   except:
#         #     return
#         # else:
#         #   pass

#         # with open("queue.json","w") as f:
#         #   json.dump(users,f)
#         # return
#     except:
#       return
#     if (ctx!=None):
#       # await asyncio.sleep(1.5)
#       await playtheurl(ctx)



async def playtheurl(ctx, timestamp=0, query=None):
    # db["ctx"][str(ctx.guild.id)]=json.dumps(ctx)
    mysongSave=None
    nameSave=None
    durationSave=None
    thumbnailSave=None
    weburlSave=None
    requestorSave=None

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if len(await accessQueue(ctx.guild.id)) != 0:
      print("playing")
      mysong,name,duration,thumbnail, urls, requestors =await accessQueue(ctx.guild.id,"all")
      mysong=mysong[0]
      name=name[0]
      duration=duration[0]
      thumbnail=thumbnail[0]
      source=mysong
      weburl=urls[0]
      requestor=requestors[0]

      mysongSave = mysong
      thumbnailSave = thumbnail
      durationSave = duration
      nameSave = name
      requestorSave=requestor
      weburlSave=weburl
      
      server=ctx.guild.id

      # looper = asyncio.get_event_loop()
      # video=None
      # source=None
      # video, source = await search(mysong, ctx)
      
      # video, source = await search(mysong, ctx)
      voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

      # FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      FFMPEG_OPTS = {'before_options': f'-ss {timestamp}  -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': f'-vn'}
      


      await accessPlaying(ctx.guild.id,mysong, name, duration,thumbnail, weburl, requestor)
         

   
      with open("queue.json","r") as f:
        users = json.load(f)
      if str(server) in users:
        try:
          users[str(server)]["queue"].pop(0)
          users[str(server)]["name"].pop(0)
          users[str(server)]["duration"].pop(0)
          users[str(server)]["thumbnail"].pop(0)
          users[str(server)]["link"].pop(0)
          users[str(server)]["requestor"].pop(0)
          # await ctx.send("POPPPED")
          # result = VideosSearch(mysong.replace(' ',''), limit = 1).result()['result']
          # INDEX = 0
          # print(result[INDEX]['link'])
          # final_url = result[INDEX]['link']
          # index = users[str(server)]["queue"].index(final_url)
          # users[str(server)]["name"].pop(index)
          # users[str(server)]["queue"].remove(final_url)
          
        except:
          pass
          # users[str(server)]["queue"].pop(0)
          # users[str(server)]["name"].pop(0)
      else:
        users[str(server)]= {}
        users[str(server)]["queue"]=[]
        users[str(server)]["name"]=[]
        users[str(server)]["duration"]=[]
        users[str(server)]["thumbnail"]=[]
        users[str(server)]["link"]=[]
        users[str(server)]["requestor"]=[]
        
        # users[str(server)]["queue"].append(song)
      with open("queue.json","w") as f:
        json.dump(users,f)
      # def start(ctx):
      #   await playtheurl(ctx)
      def my_after(ctx):
        # time.sleep(1)
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_playing:
          return
        try:
          print('finished', e)
        except:
          pass
        coro = playtheurl(ctx)
        fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
        try:
          fut.result()
        except:
          # an error happened sending the message
          pass

      # voice.play(discord.FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: print('finished', e))
      # try:
      #   pass
      # if voice.is_playing():
      #   voice.stop()
      # player = await YTDLSource.from_url("https://www.youtube.com/watch?v=83xBPCw5hh4&ab_channel=DaBaby", loop=self.client.loop)
      state=False
  
      try:
        # voice.play(discord.FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e:print('finished', e))
        # voice.play(discord.FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e: print("OOGALA"))
        loop = asyncio.get_event_loop()
        # import threading
        # voice.play(discord.FFmpegPCMAudio(source, **FFMPEG_OPTS))
        await loop.run_in_executor(None, lambda:voice.play(discord.FFmpegPCMAudio(source, **FFMPEG_OPTS), after=lambda e:print("OOGALA")))
      except:
        return
      # except:
      #   pass
    
        
      try:
        # pass
        volumeAmount = await accessVolume(ctx.guild.id)
        voice.source = discord.PCMVolumeTransformer(voice.source, volume=volumeAmount/100)
        # ctx.voice_client.source.volume = volumeAmount
      
      except:
        pass
      try:
        # pass
        if str(weburl)!="https://google.com":
          await previousQueue(ctx.guild.id, mysongSave, name, durationSave,thumbnailSave, weburlSave, requestorSave)
        # await previousQueue(ctx.guild.id, mysongSave, name, durationSave,thumbnailSave)
        print("SLEEPING")
        if timestamp==0:
          await playing(ctx)
        await asyncio.sleep(duration-timestamp)
        # await asyncio.sleep((int(video['duration'])-timestamp+2)/3)
        # await previousQueue(ctx.guild.id, mysong, titleSong)
        # print("SLEPT")
        # await asyncio.sleep(((int(video['duration'])-timestamp+2)/3)*2)
      
        print("SLEPT")
        if voice.is_playing() or voice.is_paused():
          print("RETURNING")
          return

        await playtheurl(ctx)
        # return
        
        
        
      except Exception as e:
        print(e)
    else:
      # await ctx.send("> The Queue Is Finished.")
      try:
        if voice.is_playing() or voice.is_paused():
          return
        await stop(ctx, "silent")
        return
      except:
        return
      
    # if len(await accessQueue(ctx.guild.id)) != 0:
    #   await playtheurl(ctx)
    # else:
    #   await stop(ctx, "silent")
    # print("titleeaaa"+video['title'])
    # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    # ydl_opts = {
    #     'format': 'bestaudio/best',
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'mp3',
    #         'preferredquality': '192',
    #     }],
    # }
    # # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    # #     ydl.download([url])
    # # for file in os.listdir("./"):
    # #     if file.endswith(".mp3"):
    # #         os.rename(file, "song.mp3")
    # FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    # await voice.play(discord.FFmpegPCMAudio(source, **FFMPEG_OPTS))
    # , after=lambda e: return
    # voice.play(discord.FFmpegPCMAudio("song.mp3"))


# @client.command()
# async def playurl(ctx, url : str):
#     song_there = os.path.isfile("song.mp3")
#     try:
#         if song_there:
#             os.remove("song.mp3")
#     except PermissionError:
#         await ctx.send("Wait for the current playing music to end or use the 'stop' command")
#         return

#     if not ctx.message.author.voice:
#         await ctx.send("You are not connected to a voice channel")
#         return
    
#     else:
#         await ctx.send("Joining...")
#         voiceChannel = ctx.message.author.voice.channel
#         await voiceChannel.connect()
    
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#     for file in os.listdir("./"):
#         if file.endswith(".mp3"):
#             os.rename(file, "song.mp3")
#     voice.play(discord.FFmpegPCMAudio("song.mp3"))



# @client.command(aliases=['mix','Shuffle','Mix'])
async def shuffleOld(ctx):
  import random

  # c = list(zip(a, b))

  # random.shuffle(c)

  # a, b = zip(*c)

  # [OUTPUT]
  # ['a', 'c', 'b']
  # [1, 3, 2]

  with open("queue.json","r") as f:
    users = json.load(f)
  if str(ctx.guild.id) in users:
    try:
      queue=users[str(ctx.guild.id)]["queue"]
      names= users[str(ctx.guild.id)]["name"]
      thumbnails = users[str(ctx.guild.id)]["thumbnail"]
      links = users[str(ctx.guild.id)]["link"]
      requestors = users[str(ctx.guild.id)]["requestor"]
      durations = users[str(ctx.guild.id)]["duration"]
      c = list(zip(queue, names, thumbnails, links, requestors, durations))
      random.shuffle(c)
      queue, names, thumbnails, links, requestors, durations = zip(*c)
      users[str(ctx.guild.id)]["queue"]=queue
      users[str(ctx.guild.id)]["name"]=names
      users[str(ctx.guild.id)]["thumbnail"]=thumbnails
      users[str(ctx.guild.id)]["link"]=links
      users[str(ctx.guild.id)]["requestor"]=requestors
      users[str(ctx.guild.id)]["duration"]=durations
    except:
      #Play SOMETHING FIRST
      embed=discord.Embed(title="Queue Something Before Shuffling!", color = discord.Color.red())
      await ctx.send(embed=embed)

      return
  else:
    embed=discord.Embed(title="Queue Something Before Shuffling!", color = discord.Color.red())
    await ctx.send(embed=embed)

    return
    #write code here

  with open("queue.json","w") as f:
    json.dump(users,f)
  embed=discord.Embed(title="🔀 Shuffled!", color = discord.Color.blue())
  await ctx.send(embed=embed)


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="b0d1cdbcce274e96905178376add6d61", client_secret="11a204d370c24b79891667ceb6fa5c31"))

async def get_playlist_tracks(playlist_id):
    results = sp.user_playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
      results = sp.next(results)
      tracks.extend(results['items'])
    return tracks

# @client.command(aliases=['q','a','Queue','add','Add'])
async def queueOld(ctx, *, mysong: str=None):
    state = await checkIfPart2(ctx)
    if not state:
      return

    if mysong==None:
      await listqueue(ctx)
      return
    if "spotify" in mysong:
      

      # birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
      

      # results = spotify.artist_albums(birdy_uri, album_type='album')
      # albums = results['items']
      # while results['next']:
      #   results = spotify.next(results)
      #   albums.extend(results['items'])
      albums = await get_playlist_tracks("6A83PFHKOMYMQTV6YwSeNk")

      for album in albums:
        print(album['name'])
        video, source = await search(album["name"], ctx, client.loop)
        title=video["title"]
        final_url=source
        url = video["webpage_url"]
        duration=int(video["duration"])
        thumbnail = video["thumbnail"]
        url = video["webpage_url"]
        await queueSong(ctx.guild.id, final_url, title,duration, thumbnail, url, ctx.author.id)
      return
        
    # msg=await ctx.send("> Searching...")

    # video, source = await search(mysong)
    # title=""
    video, source = await search(mysong,ctx, client.loop)
    title=video["title"]
    final_url=source
    url = video["webpage_url"]
    duration=int(video["duration"])
    thumbnail = video["thumbnail"]
    url = video["webpage_url"]
    # try:
    #   result = VideosSearch(mysong.replace(' ',''), limit = 1).result()['result']
    #   INDEX = 0
    #   print(result[INDEX]['link'])
    #   final_url = result[INDEX]['link']
    #   title = result[INDEX]['title']
    # except:
      
    #   video, info = await search(mysong)
    #   title=video["title"]
      # final_url=video["url"]

    # print(result[INDEX])
    # await ctx.send("URL "+result[INDEX]['link'])
    
    # vidLength = result[INDEX]['seconds']
    # print(vidLength)

    # video = pafy.new(final_url)
    # vidLength = video.length
    # title = video.title

    # print(vidLength)
    # if int(vidLength) > 600:
    #     await ctx.send("This video cannot be added to the queue because it is longer than 10 min.".title())
    #     return
    # if final_url in await accessQueue(ctx.guild.id):
    #   await ctx.send("This song has already been added to the queue, wait for it to be played before adding it again.".title())
    #   return
    # print("hi")
    length=len(await accessQueue(ctx.guild.id)) 
    # print("hi")
    await queueSong(ctx.guild.id, final_url, title,duration, thumbnail, url, ctx.author.id)
    # print("hi")
    # await msg.delete()
    # embed=discord.Embed(title="Track Queued!", url=url, color = 0xFF5733)
    # await ctx.send(embed=embed)
    try:
      voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
      if length ==0 and not voice.is_playing():
        await play(ctx)
      else:
        embed=discord.Embed(title="Track Queued!", url=url, color = 0xFF5733)
        await ctx.send(embed=embed)
        return
    except Exception as e:
      if length>0:
        embed=discord.Embed(title="Track Queued!", url=url, color = 0xFF5733)
        await ctx.send(embed=embed)
      await play(ctx)
      
    # await listqueue(ctx)
    # embed=discord.Embed(title="A New Song Has Been Queued, Use The Play Command To Play!", url=final_url, description= mysong.title() +" Has been Queued!", color=0xFF5733, timestamp=datetime.utcnow())

    # # Add author, thumbnail, fields, and footer to the embed
    # embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    # embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-512/spotify-11-432546.png")

    # embed.add_field(name="Song Name:", value= mysong.title() , inline=False)
    # embed.add_field(name="URL:", value = final_url , inline=False) 
    # await msg.delete()
    # await ctx.send(embed = embed)
    # await ctx.send(final_url)
    # await ctx.send("Qued!\nSong Name: " + mysong.title() + ".\nURL: " + final_url)

@client.command()
async def remove(ctx, *, mysong):
    server=ctx.guild.id
    try:
      if isinstance(int(mysong), int):

        
        with open("queue.json","r") as f:
          users = json.load(f)
        if str(server) in users:
          try:
            users[str(server)]["queue"].pop(int(mysong)-1)
            users[str(server)]["name"].pop(int(mysong)-1)
            users[str(server)]["duration"].pop(int(mysong)-1)
            users[str(server)]["thumbnail"].pop(int(mysong)-1)
            users[str(server)]["link"].pop(int(mysong)-1)
            users[str(server)]["requestor"].pop(int(mysong)-1)
          except:
            embed=discord.Embed(title="That Song Number Does Not Exist In The Queue!".title(), color = discord.Color.light_grey())
            await ctx.send(embed=embed)
            return
            # await ctx.send("> That Song Number Does Not Exist In The Queue.")
            # return
        else:
          pass
        embed=discord.Embed(title="Song ` "+str(mysong) + " ` has been removed!".title(), color = discord.Color.light_grey())
        await ctx.send(embed=embed)
        # await ctx.send("> Song "+str(mysong) + " has been removed!".title())
        with open("queue.json","w") as f:
          json.dump(users,f)
        return
    except:
      mysong=str(mysong)
    # result = VideosSearch(mysong.replace(' ',''), limit = 1).result()['result']
    # INDEX = 0
    # print(result[INDEX]['link'])
    # final_url = result[INDEX]['link']

    # try:
    #   result = VideosSearch(mysong.replace(' ',''), limit = 1).result()['result']
    #   INDEX = 0
    #   print(result[INDEX]['link'])
    #   final_url = result[INDEX]['link']
    #   title = result[INDEX]['title']
    # except:
    #   final_url=mysong
    #   video, info = await search(mysong, loop=client.loop)
    #   title = video['title']
    video, source = await search(mysong,ctx, client.loop)
    final_url=source
    title=video["title"]
    thumbnail=video["thumbnail"]
    print(title)

    server=ctx.guild.id
    with open("queue.json","r") as f:
      users = json.load(f)
    if str(server) in users:
      try:
        index = users[str(server)]["thumbnail"].index(str(thumbnail))
        users[str(server)]["queue"].pop(index)
        users[str(server)]["name"].pop(index)
        users[str(server)]["thumbnail"].pop(index)
        users[str(server)]["duration"].pop(index)
        users[str(server)]["link"].pop(index)
        users[str(server)]["requestor"].pop(index)
      except Exception as e:
        print(e)
        embed=discord.Embed(title="That Song Does Not Exist In The Queue!".title(), color = discord.Color.light_grey())
        await ctx.send(embed=embed)
        return
    else:
      pass
    with open("queue.json","w") as f:
      json.dump(users,f)
    embed=discord.Embed(title="The Song: ` "+title + " ` has been removed".title(), color = discord.Color.light_grey())
    await ctx.send(embed=embed)
    # await ctx.send("> The Song: "+title + " has been removed".title())

@client.command()
async def removeteamtask(ctx, *, mysong: str):
  try:
    TaskList.remove(mysong.title())
  except:
    await ctx.send("> Your task list is either empty, or there is nothing under the name provided.")
    
  await ctx.send("> "+mysong.title() + " has been removed")



# @client.command()
# @commands.has_permissions(administrator = True)
async def clearqueueOld(ctx):
  server=ctx.guild.id
  with open("queue.json","r") as f:
    users = json.load(f)
  if str(server) in users:
    users[str(server)]["queue"].clear()
    users[str(server)]["name"].clear()
    users[str(server)]["duration"].clear()
    users[str(server)]["thumbnail"].clear()
    users[str(server)]["link"].clear()
    users[str(server)]["requestor"].clear()
  else:
    users[str(server)]= {}
    users[str(server)]["queue"]=[]
    users[str(server)]["name"]=[]
    users[str(server)]["duration"]=[]
    users[str(server)]["thumbnail"]=[]
    users[str(server)]["link"]=[]
    users[str(server)]["requestor"]=[]
  with open("queue.json","w") as f:
    json.dump(users,f)
  embed=discord.Embed(title="cleared!".title(), color = discord.Color.teal())
  await ctx.send(embed=embed)
  QueList.clear()

@client.command()
# @commands.has_permissions(ban_members = True)
async def cleartasks(ctx):
    await ctx.send("Cleared!")
    TaskList.clear()

@client.command()
async def will(ctx, *, question: str):
  answers = ['Obviously', 'Yes', 'Most definitely!', 'Not a doubt!']
  await ctx.send(rando.choice(answers))
    
    
# @client.command(aliases=['p','start','track','set'])
async def playOld(ctx, *, mysong: str="queue"):
    listing=False
    try:
      voiceChannel = ctx.message.author.voice.channel
      voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    except:
      pass
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    # if voice==None:
    #   embed=discord.Embed(title="Play Something Before Trying To Play the Queue!"+voice.channel.name, color = discord.Color.red())
    #   await ctx.send(embed=embed)
    try:
      if voice.is_playing() and voiceChannel!=voice.channel:
        embed=discord.Embed(title="Someone Else Is Already Listnening To Music Join That Channel To Listen To Music Too. The Voice Channel Is: "+voice.channel.name, color = discord.Color.red())
        await ctx.send(embed=embed)
        # await ctx.send("> "+ctx.author.mention+" Someone Else Is Already Listnening To Music Join That Channel To Listen To Music Too. The Voice Channel is: "+voice.channel.mention)
        return
      elif  not voice.is_playing() and voiceChannel!=voice.channel:
        
        # try:
        await stop(ctx, "disconnect")
        voiceChannel = ctx.message.author.voice.channel
        await voiceChannel.connect()
        print("connected")
        # except:
        #   pass
        
    except:
      pass
    try:
      if voice==None:
        pass
      elif voice.is_paused():
        await resume(ctx)
        return
    except:
      pass

    # try:
    #     voice_client = ctx.message.guild.voice_client
    #     await voice_client.disconnect()
    # except AttributeError:
    #     pass

    if not ctx.message.author.voice:
        embed=discord.Embed(title="You Are Not Connected To A Voice Channel", color = discord.Color.red())
        await ctx.send(embed=embed)
        return

    else:
      try:
      #   if not voice.is_connected():
        await voiceChannel.connect()
      except:
        pass
      # try:
      # try:
      # if voice==None:
        # msg = await ctx.send("Joining...")
        
      # except:
      #   pass
      # except:
      #   pass
      # except:
      #   await ctx.send("Joining...")
      #   await voiceChannel.connect()

    # song_there = os.path.isfile("song.mp3")
    # ydl_opts = {
    #     'format': 'bestaudio/best',
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'mp3',
    #         'preferredquality': '192',
    #     }],
    # }
    # await msg.delete()
    song_there=False
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Next time, please wait for the current playing music to end or use the 'stop' command")
        # return

    # if len(mysong) < 2:
    #     await ctx.send("> Please include the title of the song after the .play command or a larger length song. -help for more info".title())
    #     return

    if not ctx.message.author.voice:
        embed=discord.Embed(title="You Are Not Connected To A Voice Channel", color = discord.Color.red())
        await ctx.send(embed=embed)
        return

    else:
        pass

    
    # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    # url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
    # msg.delete()
    # msg = await ctx.send("> Searching...")
    if mysong.lower() == "queue" or mysong.lower() =="que" or mysong.lower()=="song":
        if len(await accessQueue(ctx.guild.id))==0:
            embed=discord.Embed(title="🛑 The Queue Is Empty", color = discord.Color.orange())
            await ctx.send(embed=embed)
            await stop(ctx, "silent")
            return
    if mysong != "queue" and mysong != "que":

        INDEX = 0

        # result = VideosSearch(mysong.replace(' ',''), limit = 1).result()['result']

        # print(result[INDEX]['link'])
        # final_url = result[INDEX]['link']
        # title = result[INDEX]['title']
        # try:
        #   result = VideosSearch(mysong.replace(' ',''), limit = 1).result()['result']
        #   INDEX = 0
        #   print(result[INDEX]['link'])
        #   final_url = result[INDEX]['link']
        #   title = result[INDEX]['title']
        # except:
        # final_url=mysong
        video, source = await search(mysong,ctx, loop=client.loop)
        title=video["title"]
        final_url=source
        duration=int(video["duration"])
        thumbnail=video["thumbnail"]
        url = video["webpage_url"]

        print(duration)
        print(thumbnail)
    
        # video = pafy.new(final_url)
        # vidLength =  int(video.length)

        # print(vidLength)
        # if vidLength > 600:
        #     await ctx.send("This song cannot be played because it is longer than 10 min. Select or queue another song...".title())
        #     await stop(ctx, "silent")
        #     return
    # msg.delete()
    if  mysong != "queue" and mysong != "que":
      if (len(await accessQueue(ctx.guild.id)))==0:
        # try:
        #   await stop(ctx)
        #   await voiceChannel.connect()
        # except:
        #   pass
        # embed=discord.Embed(title="A New Song Is Playing!", url=final_url, description= mysong.title() +" Is Playing!", color=0xFF5733, timestamp=datetime.utcnow())

        # # Add author, thumbnail, fields, and footer to the embed
        # embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

        # embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-512/spotify-11-432546.png")

        # embed.add_field(name="Song:", value="["+ video.title+"]("+final_url+")" , inline=False)
        # # embed.add_field(name="URL:", value = final_url , inline=False) 
        
        # await ctx.send(embed = embed)
        # # await ctx.send(final_url)
        # # await ctx.send(final_url)
        # # msg = await ctx.send("> Downloading...")
        # import threading
        
        # th = threading.Thread(target=downloadSong(final_url, ctx))
        # th.start()
        # return
        await queueSong(ctx.guild.id,final_url, title, duration,thumbnail, url, ctx.author.id)
        # embed=discord.Embed(title="Track Queued!", url=final_url,  color = 0xFF5733)
        # await ctx.send(embed=embed)
        try:
          if voice.is_playing():
            await voice.stop()
            # return
        except:
          pass
        # song="song"
        await play(ctx)
        return
        # await downloadSong(final_url)
        # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #     ydl.download([final_url])
        # for file in os.listdir("./"):
        #     if file.endswith(".mp3"):
        #         os.rename(file, "song.mp3")
        # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        # msg.delete()

        # voice.play(discord.FFmpegPCMAudio("song.mp3"))
      elif (len(await accessQueue(ctx.guild.id)))>0 and mysong.lower()!="queue":
        # await ctx.send("> "+ctx.author.mention+" At The Moment, The queue has songs in it already. Astro will add your song to the queue, and then, start playing through the queue.".title())
        await queueSong(ctx.guild.id,final_url, title,duration,thumbnail, url, ctx.author.id)
        embed=discord.Embed(title="Track Queued!", url=final_url,  color = 0xFF5733)
        await ctx.send(embed=embed)
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        # await listqueue(ctx)
        listing=True
        try:
          if voice.is_playing():
            return
        except:
          pass

    if (len(await accessQueue(ctx.guild.id)))!=0:
        try:
          # await stop(ctx, "silent")
          voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
          await voice.stop()
          await voiceChannel.connect()
        except:
          pass
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        embed=discord.Embed(title="Queue!", url= (await accessQueue(ctx.guild.id))[0], description= "Astro is playing songs from the queue, use the skip command to skip songs, and the stop command to stop playing from the queue.", color=0xFF5733, timestamp=datetime.utcnow())

        # Add author, thumbnail, fields, and footer to the embed
        embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

        embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-512/spotify-11-432546.png")

        embed.add_field(name="To See The Queue:", value= "Use the listqueue command." , inline=True)
        embed.add_field(name="To Skip:", value = "Use the Skip Command." , inline=True)
        embed.add_field(name="To Play A New Song:", value = "Use the Play Command." , inline=True)
        embed.add_field(name="To Stop Entirely:", value = "Use the Stop Command." , inline=True) 
        embed.add_field(name="For More Info:", value = "Use the Help Command." , inline=True)   
        if listing==False:
          pass
          # await listqueue(ctx)
        # await ctx.send((await accessQueue(ctx.guild.id))[0])
        # await ctx.send(final_url)
        global ctxSave
        if ctxSave is None:
            ctxSave = ctx
        # await playtheurl(ctx)
        await playtheurl(ctx)
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(await playtheurl(ctx))
        # import threading
        # _thread = threading.Thread(target=asyncio.run, args=(playtheurl(ctx),))
        # _thread.start()
        # isplaying()
                # QueList.pop(0)
                    
                # time.sleep(vidLength)
            
            # time.sleep()
        # await ctx.send("After this song Queue is finished 😢")
# skipCount = 0

# @client.command(aliases=['Restart', 'rewind','Rewind'])
# async def restart(ctx):
#   await stop(ctx, "silent")
#   await play(ctx)

# @client.command(aliases=['Skip', 'forward','Forward', 'fastforward'])
async def skipOld(ctx, status=None):
  # try:
  #   voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if status != None:
    if isinstance(int(status), int):
      await move(ctx, int(status))
      return
  # if isinstance(status, str):

  if status !="silent":
    state = await checkIfPart(ctx)
    if not state:
      return
  if len(await accessQueue(ctx.guild.id)) == 0:
    # await ctx.send("> The Queue Is Empty.")
    embed=discord.Embed(title="🛑 The Queue Is Empty!".title(), color = discord.Color.orange())
    await ctx.send(embed=embed)
    await stop(ctx, "silent")
    return
  # server=ctx.guild.id
  # with open("queue.json","r") as f:
  #   users = json.load(f)
  # if str(server) in users:
  #   users[str(server)]["queue"].pop(0)
  #   users[str(server)]["name"].pop(0)
  # else:
  #   users[str(server)]= {}
  #   users[str(server)]["queue"]=[]
  #   # users[str(server)]["queue"].append(song)
  # with open("queue.json","w") as f:
  #   json.dump(users,f)
  if len(await accessQueue(ctx.guild.id)) == 0:
    embed=discord.Embed(title="🛑 The Queue Is Empty!".title(), color = discord.Color.orange())
    await ctx.send(embed=embed)
    await stop(ctx, "silent")
    return
  # await stop(ctx, "silent")
  embed=discord.Embed(title="⏩ Skipped!".title(), color = discord.Color.orange())
  await ctx.send(embed=embed)
  await play(ctx)
  
  # await ctx.send("> ⏩ Skipped!")
  
    # global skipCount
    # skipCount = skipCount + 1
    # if skipCount % 2 == 0:
    #     print("this time we are running the pop")
    #     QueList.pop(0)

    # # else:
    # #     await ctx.send("Skipping(please type .skip twice to confirm a skip)")
    # #     return
    
    # server = ctx.message.guild
    # voice_channel = server.voice_client
    # voice_channel.stop()
    # voice_client = ctx.message.guild.voice_client
    # await voice_client.disconnect()
    # voiceChannel = ctx.message.author.voice.channel
    # await voiceChannel.connect()
    # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    # print(skipCount)
    
    # if len(QueList) == 0:
    #     await ctx.send("Queue is empty 😢")
    #     server = ctx.message.guild
    #     voice_channel = server.voice_client
    #     voice_channel.stop()
    #     voice_client = ctx.message.guild.voice_client
    #     await voice_client.disconnect()
    #     return
    # else:
    #     global ctxSave
    #     if ctxSave:
    #         ctxSave = ctx
    #     isplaying()
    # # skip2(ctx)

def skip2(ctx):
    # await ctx.send("Skipping(please type .skip twice to confirm a skip)")
    # server = ctx.message.guild
    # voice_channel = server.voice_client
    # voice_channel.stop()
    # voice_client = ctx.message.guild.voice_client
    # await voice_client.disconnect()
    # voiceChannel = ctx.message.author.voice.channel
    # await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    # QueList.pop(0)
    # if len(await queList(ctx.guild.id)) == 0:
        # await ctx.send("Queue is empty 😢")
        # server = ctx.message.guild
        # voice_channel = server.voice_client
        # voice_channel.stop()
        # voice_client = ctx.message.guild.voice_client
        # await voice_client.disconnect()
        
        
    return
    # else:
    #     global ctxSave
    #     if ctxSave is None:
    #         ctxSave = ctx
    #     isplaying()



  # prefixes[str(guild.id)] = ['.']#default prefix

  # with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
  #   json.dump(prefixes, f, indent=4) #the indent is to

class isplaying(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
      loop = asyncio.new_event_loop()
      asyncio.set_event_loop(loop)

      loop.run_until_complete(playtheurl(ctxSave))
      loop.close()
      
        # while len(accessQueueReg(ctxSave.guild.id)) != 0:
        #     mysong=(accessQueueReg(ctxSave.guild.id))[0]
        #     result = VideosSearch(mysong.replace(' ',''), limit = 1).result()['result']
        #     INDEX = 0
        #     print(result[INDEX]['link'])
        #     # final_url = result[INDEX]['link']
        #     duration = str(result[INDEX]['duration'])
        #     # durationa = datetime.strptime(duration, "%H:%M:%S")
        #     # a_timedelta = durationa - datetime.datetime(1900, 1, 1)
        #     # vidLength = a_timedelta.total_seconds()

        #     playtheurl(ctxSave, (accessQueueReg(ctxSave.guild.id))[0])
        #     video = pafy.new((accessQueueReg(ctxSave.guild.id))[0])
        #     vidLength =  int(video.length)
            
        #     voice = discord.utils.get(client.voice_clients, guild=ctxSave.guild)
        #     # while voice.is_playing():
        #     #     voice = discord.utils.get(client.voice_clients, guild=ctxSave.guild)
        #     time.sleep(vidLength)
        #     server=ctxSave.guild.id
        #     with open("queue.json","r") as f:
        #       users = json.load(f)
        #     if str(server) in users:
        #       try:
        #         users[str(server)]["queue"].pop(0)
        #         users[str(server)]["name"].pop(0)
        #       except:
        #         pass
        #     else:
        #       users[str(server)]= {}
        #       users[str(server)]["queue"]=[]
        #       # users[str(server)]["queue"].append(song)
        #     with open("queue.json","w") as f:
        #       json.dump(users,f)
        # return
            # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            # isplaying()
            # QueList.pop(0)

class isplaying2(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while len(accessQueue(ctxSave.guild.id)) != 0:
            playtheurl(ctxSave, accessQueue(ctxSave.guild.id)[0])
            video = pafy.new(accessQueue(ctxSave.guild.id)[0])
            vidLength =  int(video.length)
            voice = discord.utils.get(client.voice_clients, guild=ctxSave.guild)
            while voice.is_playing():
                voice = discord.utils.get(client.voice_clients, guild=ctxSave.guild)
            time.sleep(vidLength)
            server=ctxSave.guild.id
            with open("queue.json","r") as f:
              users = json.load(f)
            if str(server) in users:
              users[str(server)]["queue"].pop(0)
              users[str(server)]["name"].pop(0)
            else:
              users[str(server)]= {}
              users[str(server)]["queue"]=[]
              # users[str(server)]["queue"].append(song)
            with open("queue.json","w") as f:
              json.dump(users,f)
        return
            # voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            # isplaying()
            # QueList.pop(0)
async def queueSong(server, song, name,duration,thumbnail,weburl,requestor, pos=None):
  if pos != None:
    with open("queue.json","r") as f:
      users = json.load(f)
    if str(server) in users:
      users[str(server)]["queue"].insert(pos,song)
      users[str(server)]["name"].insert(pos,name)
      users[str(server)]["thumbnail"].insert(pos, thumbnail)
      users[str(server)]["duration"].insert(pos, duration)
      users[str(server)]["link"].insert(pos, weburl)
      users[str(server)]["requestor"].insert(pos, requestor)
    else:
      users[str(server)]= {}
      users[str(server)]["queue"]=[]
      users[str(server)]["name"]=[]
      users[str(server)]["duration"]=[]
      users[str(server)]["thumbnail"]=[]
      users[str(server)]["link"]=[]
      users[str(server)]["requestor"]=[]
      users[str(server)]["link"].insert(pos, weburl)
      users[str(server)]["requestor"].insert(pos, requestor)
      users[str(server)]["queue"].insert(pos, song)
      users[str(server)]["name"].insert(pos, name)
      users[str(server)]["thumbnail"].insert(pos, thumbnail)
      users[str(server)]["duration"].insert(pos, duration)
    with open("queue.json","w") as f:
      json.dump(users,f)
    return


  with open("queue.json","r") as f:
    users = json.load(f)
  if str(server) in users:
    users[str(server)]["queue"].append(song)
    users[str(server)]["name"].append(name)
    users[str(server)]["duration"].append(duration)
    users[str(server)]["thumbnail"].append(thumbnail)
    users[str(server)]["link"].append( weburl)
    users[str(server)]["requestor"].append( requestor)
  else:
    users[str(server)]= {}
    users[str(server)]["queue"]=[]
    users[str(server)]["name"]=[]
    users[str(server)]["duration"]=[]
    users[str(server)]["thumbnail"]=[]
    users[str(server)]["link"]=[]
    users[str(server)]["requestor"]=[]
    users[str(server)]["link"].append( weburl)
    users[str(server)]["requestor"].append( requestor)
    users[str(server)]["queue"].append( song)
    users[str(server)]["name"].append(name)
    users[str(server)]["thumbnail"].append(thumbnail)
    users[str(server)]["duration"].append( duration)
  with open("queue.json","w") as f:
    json.dump(users,f)

  # return True
def accessQueueReg(server):
  with open("queue.json","r") as f:
    users = json.load(f)
  if str(server) in users:
    return users[str(server)]["queue"]
  else:
    users[str(server)]= {}
    users[str(server)]["queue"]=[]
    users[str(server)]["name"]=[]
  with open("queue.json","w") as f:
    json.dump(users,f)
  return users[str(server)]["queue"]

async def accessNames(server):
  with open("queue.json","r") as f:
    users = json.load(f)
  if str(server) in users:
    return users[str(server)]["name"]
  else:
    users[str(server)]= {}
    users[str(server)]["queue"]=[]
    users[str(server)]["name"]=[]
    users[str(server)]["link"]=[]
    users[str(server)]["requestor"]=[]
    
    users[str(server)]["duration"]=[]
    users[str(server)]["thumbnail"]=[]
  with open("queue.json","w") as f:
    json.dump(users,f)
  return users[str(server)]["name"]

# @client.command()
# async def defean(ctx, memb=None):
#     if memb==None:
#       memb=client
#     await memb.voice.deaf
#     # voice_client = ctx.guild.voice_client
#     # if not voice_client:
#     #     return
#     # channel = voice_client.channel
#     # await voice_client.main_ws.voice_state(ctx.guild.id, channel.id, self_mute=True)

async def accessQueue(server, mode=None):
  with open("queue.json","r") as f:
    users = json.load(f)
  if str(server) in users:
    if mode=="all":
      return users[str(server)]["queue"],  users[str(server)]["name"],  users[str(server)]["duration"],  users[str(server)]["thumbnail"], users[str(server)]["link"], users[str(server)]["requestor"]
    return users[str(server)]["queue"]
  else:
    users[str(server)]= {}
    users[str(server)]["queue"]=[]
    users[str(server)]["name"]=[]
    users[str(server)]["link"]=[]
    users[str(server)]["requestor"]=[]
    
    users[str(server)]["duration"]=[]
    users[str(server)]["thumbnail"]=[]
  with open("queue.json","w") as f:
    json.dump(users,f)
  return users[str(server)]["queue"]
  # return True



async def accessVolume(server, volume=None):
  with open("volumes.json","r") as f:
    users = json.load(f)
  if volume != None:
    if str(server) in users:
      users[str(server)]["volume"]= volume
    else:
      users[str(server)]= {}
      users[str(server)]["volume"]=volume
    with open("volumes.json","w") as f:
      json.dump(users,f)
    return
  if str(server) in users:
    return users[str(server)]["volume"]
  else:
    users[str(server)]= {}
    users[str(server)]["volume"]=100
  with open("volumes.json","w") as f:
    json.dump(users,f)

  # return True

















# @client.command()
async def pauseOld(ctx, status=None):
    if status !="silent":
      state = await checkIfPart(ctx)
      if not state:
        return
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice==None:
      pass
    elif voice.is_playing():
        voice.pause()
        embed=discord.Embed(title="⏸ Paused!".title(), color = discord.Color.dark_blue())
        await ctx.send(embed=embed)
        # await ctx.send("> :pause_button: Paused!")
    else:
      voice.pause()
      embed=discord.Embed(title="Currently no audio is playing!".title(), color = discord.Color.dark_blue())
      await ctx.send(embed=embed)
        # await ctx.send("Currently no audio is playing.")
async def checkIfPart2(ctx):
  if not ctx.message.author.voice:
    embed=discord.Embed(title="You Are Not Connected To A Voice Chanel!".title(), color = discord.Color.red())
    await ctx.send(embed=embed)
    return False
  return True

async def checkIfPart(ctx):
  if not ctx.message.author.voice:
    embed=discord.Embed(title="You Are Not Connected To A Voice Chanel!".title(), color = discord.Color.red())
    await ctx.send(embed=embed)
    return False
  try:
    voiceChannel = ctx.message.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  except:
    return False
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  try:
    if voice.is_playing() and voiceChannel!=voice.channel:
      embed=discord.Embed(title="Someone Else Is Listnening To Music. Join That Channel To Control The Music. The Channel Is: "+voice.channel.name, color = discord.Color.red())
      await ctx.send(embed=embed)
      # await ctx.send("> "+ctx.author.mention+" Someone Else Is Listnening To Music. Join That Channel To Control The Music. The Channel Is: "+voice.channel.mention)
      return False
      
  except:
   return False
  return True

# @client.command(aliases = ['Stop' , 'leave', 'Leave'])
async def stopOld(ctx, status: str=None):
  if status !="silent":
    state = await checkIfPart(ctx)
    if not state:
      return
    

  try:
    if status != "silent":
      embed=discord.Embed(title="🛑 Stopping!".title(), color = discord.Color.orange())
      await ctx.send(embed=embed)
      # await ctx.send("> :octagonal_sign: Stopping...")
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.stop()
    voice_client = ctx.message.guild.voice_client
    if status == "disconnect":
      await voice_client.disconnect()
    if status !="disconnect":
      voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
      await asyncio.sleep(110)
      if voice.is_playing()==False:
        await asyncio.sleep(10)
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        if voice.is_playing()==False:
          await voice_client.disconnect()
          if True:
            embed=discord.Embed(title="✋ Astro Has Disconnected From The Voice Channel. Astro Automatically Disconnects After Two Minutes Of Inactivity!".title(), color = discord.Color.orange())
            await clear(ctx)
            await ctx.send(embed=embed)
            # await ctx.send("Astro Has Disconnected From The Voice Channel.\n\nWhat is this?\nAstro Disconnects After Ten Minutes Of No Music Playing.")
  except:
    pass

# @client.command(aliases = ['Clean'])
# async def clean(ctx):
#     await ctx.send("Since this is hosted on repl.it, files are automatically cleaned!")

# @client.command(aliases=['tracktotal','trackcovidtotal','Covidtotal','Coronatotal','coronatotal','Coronavirustotal','coronavirustotal','Covid19total''trackCovidtotal','CovidTracktotal','covidtotal'])
async def covidTrackertotal(ctx):
  

  # Format: <Data Source>.<Location>.<Statistic>
  # For example to get data from John Hopkins University, review the following example:
  # JHU.China.deaths
  import covid19_data  

  embed=discord.Embed(title="Covid Stats", description= "Covid Statistics Scraped from Johns Hokins Research Center", color=0xFF5733, timestamp=datetime.utcnow())

  # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  embed.set_thumbnail(url="https://www.psycharchives.org/retrieve/096175aa-f7f2-4970-989d-d934c30b5551")

  embed.add_field(name="The Number of COVID-19 Recoveries: ", value="Too Early To Tell" , inline=False)
  embed.add_field(name="The Number of Worldwide COVID-19 Cases: ", value = str(JHU.Total.deaths) , inline=False)
  embed.add_field(name="The Number of Worldwide COVID-19 Deaths: ", value = str(JHU.Total.deaths) , inline=False)

  await ctx.send(embed = embed)

  print("The number of COVID-19 recoveries in the US: " + str(JHU.US.recovered))
  print("The number of confirmed COVID-19 cases in Texas: " + str(JHU.Texas.confirmed))
  print("The number of COVID-19 deaths in California: " + str(JHU.California.deaths))
  print("The number of worldwide COVID-19 deaths: " + str(JHU.Total.deaths))
  print("The number of COVID-19 deaths in China: " + str(JHU.China.deaths))
  print("The number of COVID-19 deaths in UK: " + str(JHU.UnitedKingdom.deaths))





async def create_task_user(user):
  with open("tasks.json","r") as f:
    users = json.load(f)
  if str(user.id) in users:
    return False
  else:
    users[str(user.id)]= {}
    users[str(user.id)]["tasks"]=[]
  with open("tasks.json","w") as f:
    json.dump(users,f)
  return True




@client.command(case_insensitive = True, aliases = ["task"])
async def taskFor(ctx, memb: discord.Member, *, task:str):
  
  await ctx.send("When Is This Task Due?")
  dueDatea = await client.wait_for('message')
  dueDate=dueDatea.content
  taskName="Task: "+task.title()+" | Due: "+dueDate.title()

  embed = discord.Embed(title=memb.name+" Has Been Assigned A New Task!", description = taskName, colour=discord.Color.gold(), timestamp=datetime.utcnow())
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")


  await create_task_user(memb)
  with open("tasks.json","r") as f:
    users = json.load(f)
  users[str(memb.id)]["tasks"].append(taskName)
  with open("tasks.json","w") as f:
    json.dump(users,f)
  
  embed.set_thumbnail(url=f"{memb.avatar_url}")

  embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
  embed.add_field(name="All Of Your Tasks Are Listed Below:", value="Tasks Below", inline=False)
  with open("tasks.json","r") as f:
    users = json.load(f)
  for i in range(len(users[str(memb.id)]["tasks"])):
    embed.add_field(name="Task "+str(int(i)+1), value = str(users[str(memb.id)]["tasks"][i]), inline=False)

  try:
    await memb.send(embed=embed)
  except:
    await ctx.send(memb.mention+" is not accepting dm's, so here is their task.")
    await ctx.send(embed=embed)
    return
  await ctx.send(memb.mention+" has been assigned a new task, check your DM for all your tasks.")

@client.command(case_insensitive = True, aliases = ["removeTask"])
async def deletetask(ctx, memb: discord.Member, taskNum=None):
  if taskNum==None:
    await ctx.send("Specify the task number.")
    return
  await create_task_user(memb)
  with open("tasks.json","r") as f:
    users = json.load(f)
  try:
    users[str(memb.id)]["tasks"].pop(int(int(taskNum)-1))
  except:
    await ctx.send("Name a valid number to remove")
    return
  with open("tasks.json","w") as f:
    json.dump(users,f)
  await ctx.send("Removed task number "+str(int(taskNum))+" for " + memb.mention+"!")
  

@client.command(case_insensitive = True, aliases = [ "listtask", "listTaskfor"])
async def listTasks(ctx, memb: discord.Member):

  embed = discord.Embed(title="Tasks For "+memb.name, description = "Task List Below", colour=discord.Color.gold(), timestamp=datetime.utcnow())
  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

  
  embed.set_thumbnail(url=f"{memb.avatar_url}")

  embed.set_footer(text="Team Astro", icon_url=f"{client.user.avatar_url}")
  embed.add_field(name="All Of "+memb.name+ " Tasks Are Listed Below:", value="Tasks Below", inline=False)
  await create_task_user(memb)
  with open("tasks.json","r") as f:
    users = json.load(f)
  for i in range(len(users[str(memb.id)]["tasks"])):
    embed.add_field(name="Task "+str(int(i)+1), value = str(users[str(memb.id)]["tasks"][i]), inline=False)
  await ctx.send(embed=embed)
  await memb.send(embed=embed)
  























# @client.command(case_insensitive = True, aliases = ["taskList", "teamTask", "teamtasks", 'teamTaskList','teamtasklist','teamTasks'])
# @commands.bot_has_permissions(attach_files = True, embed_links = True)
async def teamtask(ctx,*, question):
  author = ctx.message.author
  author_name = author.name
  print(question)
  if " " not in question and ", " not in question and "," not in question:
    await ctx.send("> You have not included the topics/items for the task board. Remember seperate your topics like so: topic1, topic2, topic3, etc... Make sure to use commas. ")
    return
  questiona = question
  if "," in question and ", " not in question:
    questiona = question.replace(',', ', ')
  # if " " in question and ", " not in question:
  #   questiona = question.replace(' ', ', ')
  questionArr = questiona.split(", ")
  
  questiona = ""
  for i in range(len(questionArr)):
    if i != len(questionArr)-1:
      questiona = questiona + questionArr[i]+", "
    else:
      questiona = questiona + questionArr[i]
  await ctx.send("@everyone")
  embed=discord.Embed(title="Task List Created/Altered By " +author_name.title(), description= "Items", color=0xFF5733, timestamp=datetime.utcnow())

  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")


  embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/meeting-1543488-1305981.png")
  i=0
  for element in questionArr:
    TaskList.append(str(element).title())
  for element in TaskList:
    i=i+1
    embed.add_field(name="Task "+str(i)+":", value= str(element).title() , inline=False)


  await ctx.send(embed = embed)

@client.command()
async def listteamtasks(ctx):
  author = ctx.message.author
  author_name = author.name
  await ctx.send("@everyone")
  embed=discord.Embed(title="Task List Created/Altered By " +author_name.title(), description= "Items", color=0xFF5733, timestamp=datetime.utcnow())

  embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")


  embed.set_thumbnail(url="https://cdn.iconscout.com/icon/free/png-256/meeting-1543488-1305981.png")
  i=0
  for element in TaskList:
    i=i+1
    embed.add_field(name="Task "+str(i)+":", value= str(element).title() , inline=False)

  await ctx.send(embed=embed)
    


# @client.command(aliases=[ 'corona', 'Corona', 'Covid','Covid19','covid19'])
async def covid(ctx, stateName):
  import covid19_data  

  # Format: <Data Source>.<Location>.<Statistic>
  # For example to get data from John Hopkins University, review the following example:
  # JHU.China.deaths

  abrev=False

  try:
    state = covid19_data.dataByName(stateName.replace(' ',''))
  except:
    if True:
      abrev = True
    try:
      state = covid19_data.dataByNameShort(stateName.replace(' ',''))
    except:
      await ctx.send("> State Could Not Be Found")
      return
  if abrev == True:
    embed=discord.Embed(title="Covid Stats For "+stateName.upper(), description= "Covid Statistics Scraped from Johns Hokins Research Center", color=0xFF5733, timestamp=datetime.utcnow())
    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    embed.set_thumbnail(url="https://www.psycharchives.org/retrieve/096175aa-f7f2-4970-989d-d934c30b5551")

    embed.add_field(name="The Number of COVID-19 Recoveries in "+stateName.title()+":", value="Too Early To Tell" , inline=False)
    embed.add_field(name="The Number of Cases in "+stateName.title(), value = str(state.cases) , inline=False)
    embed.add_field(name="The Number of Deaths in "+stateName.title(), value = str(state.deaths) , inline=False)

    await ctx.send(embed = embed)
    return
  if abrev == False:
    embed=discord.Embed(title="Covid Stats For "+stateName.title(), description= "Covid Statistics Scraped from Johns Hokins Research Center", color=0xFF5733, timestamp=datetime.utcnow())
    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="Astro", url="https://teamastro.ml/", icon_url=f"{client.user.avatar_url}")

    embed.set_thumbnail(url="https://www.psycharchives.org/retrieve/096175aa-f7f2-4970-989d-d934c30b5551")

    embed.add_field(name="The Number of COVID-19 Recoveries in "+stateName.title()+":", value=str(state.recovered) , inline=False)
    embed.add_field(name="The Number of Cases in "+stateName.title(), value = str(state.cases) , inline=False)
    embed.add_field(name="The Number of Deaths in "+stateName.title(), value = str(state.deaths) , inline=False)

    await ctx.send(embed = embed)







@client.command(aliases=['8ball','test'])
async def eightball(ctx, *, question):
    responses = ['It is certain.', 'No.', 'No', 'No', 'No' 'Yes.', 'Obviously.', 'Never.', 'Repeat please.'
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')















# keep_alive.keep_alive()

# Lava = Thread(target=os.system("java -jar Lavalink.jar"))
# Lava.start()
import subprocess

client.add_cog(Music(client))
#DEV BOT

# client.run('ODQxNzYwMjk1NDMyODgwMTY4.YJrcXQ.5KWzQuqS7EBdjvN2vK-uwcqKPfc')



#ASTRO REGULAR
client.run('ODA5NjA5ODYxNDU2NzIzOTg4.YCXl8A.FlNO0N79eN0dbsiKlWPnDQTMV2s')




