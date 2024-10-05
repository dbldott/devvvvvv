from youtube_dl import YoutubeDL
from asyncio import sleep
import discord
from discord.ext import commands

#ВРОДЕ ДАЖЕ РАБОТАЕТ!

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'False'}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

client = commands.Bot(command_prefix="/")

catalog_url = []



def playurl(ctx, arg):
if vc.is_playing() :
with YoutubeDL(YDL_OPTIONS) as ydl :
info = ydl.extract_info(arg, download=False)
URL = info['formats'][0]['url']


catalog_url.append(URL)
else :
with YoutubeDL(YDL_OPTIONS) as ydl :
info = ydl.extract_info(arg, download=False)
URL = info['formats'][0]['url']


catalog_url.append(URL)
for i in range(len(catalog_url)) :
vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\ffmpeg.exe", source = catalog_url[i], FFMPEG_OPTIONS))
global loop_url
loop_url = catalog_url[i]
catalog_url.pop(i)

async def vcplay(ctx) :
if vc.is_playing :
vc.play(discord.FFmpegPCMAudio(executable="ffmpeg\ffmpeg.exe", source = loop_url, FFMPEG_OPTIONS))
await loop(ctx)

@client.command()
async def play(ctx, arg) :
global vc
try:
voice_channel = ctx.message.author.voice.channel
vc = await voice_channel.connect()
except:
print('Уже подключен или не удалось подключиться')

playurl(ctx, arg)
while vc.is_playing() :
await sleep(1)
if not vc.is_paused() and len(catalog_url) != 0 :
playurl(ctx, arg)

@client.command()
async def loop(ctx) :
while vc.is_playing() :
await sleep(1)
if not vc.is_paused() and loop_url != None :
await vcplay(ctx)

@client.command()
async def stop(ctx) :
vc.stop()
vc.disconnect()
