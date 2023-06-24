from .. import bot
from telethon import events
import asyncio

@bot.on(events.NewMessage(incoming=True,pattern="/start"))
async def start(event):
  await event.reply("Hello This is Dinesh_love_Bot")
  
  
@bot.on(events.NewMessage(incoming=True,pattern="/get"))
async def start(event):
  a=await event.reply("Hello This is get cammand")
  await asyncio.sleep(3)
  await a.edit("this is an edit messages")
  
  
@bot.on(events.NewMessage(incoming=True,pattern="/eval"))
async def start(event):
  await event.reply("Hello This is eval cammand")