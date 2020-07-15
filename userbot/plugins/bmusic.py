import requests
from bs4 import BeautifulSoup
from telethon import events
import subprocess
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
from userbot.utils import admin_cmd , sudo_cmd
import glob
import os  
from userbot import CMD_HELP  , catdef
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo

@borg.on(admin_cmd(pattern="bsong(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("Let me find that Song. :) ")
    elif reply.message:
        query = reply.message
        await event.edit("let me try okay..? ")
    else:
    	await event.edit("`What I am Supposed to find `")
    	return
    
    catdef.catmusic(str(query),"320k")
    l = glob.glob("*.mp3")
    if l:
        await event.edit("Aah.. Somethig there.. ")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
    loa = l[0]    
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=("**Song Name : **" + query + "\n**Uploaded by :** [Kannan](@kannappan04) 👻\n**Channel :** [പാട്ടുപെട്ടി](t.me/puthiyapaattukal) ✅"),
                reply_to=reply_to_id
            )
    await event.delete()
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)		      
    
@borg.on(admin_cmd(pattern="bvideo(?: |$)(.*)"))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("Let me find that video. :) ")
    elif reply.message:
        query = reply.message
        await event.edit("let me try okay..? ")
    else:
        await event.edit("What I am Supposed to find")
        return
    catdef.catmusicvideo(query)
    l = glob.glob(("*.mp4")) + glob.glob(("*.mkv")) + glob.glob(("*.webm")) 
    if l:
        await event.edit("Aah.. Somethig there.. ")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
    loa = l[0]  
    metadata = extractMetadata(createParser(loa))
    duration = 0
    width = 0
    height = 0
    if metadata.has("duration"):
        duration = metadata.get("duration").seconds
    if metadata.has("width"):
        width = metadata.get("width")
    if metadata.has("height"):
        height = metadata.get("height")
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=query,
                supports_streaming=True,
                reply_to=reply_to_id,
                attributes=[DocumentAttributeVideo(
                                duration=duration,
                                w=width,
                                h=height,
                                round_message=False,
                                supports_streaming=True,
                            )],
            )
    await event.delete()
    os.system("rm -rf *.mkv")
    os.system("rm -rf *.mp4")
    os.system("rm -rf *.webm")    
    
@borg.on(sudo_cmd(pattern="bsong(?: |$)(.*)", allow_sudo = True))
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        san = await event.reply("Let me find that Song. :)")
    elif reply.message:
        query = reply.message
        san = await event.reply("let me try okay..?")
    else:
    	san = await event.reply("`What I am Supposed to find `")
    	return
    catdef.catmusic(str(query),"320k")
    l = glob.glob("*.mp3")
    if l:
        await event.edit("Aah.. Somethig there.. ")
    else:
        await event.edit(f"Sorry..! i can't find anything with `{query}`")
    loa = l[0]
    await borg.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=("**Song Name : **" + {query} + "\n**Uploaded by :** [Kannan](@kannappan04) 👻\n**Channel :** [പാട്ടുപെട്ടി](t.me/puthiyapaattukal) ✅"),
                reply_to=reply_to_id
            )
    await san.delete()
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)
    
CMD_HELP.update({"getmusic":
    "`.song` query or `.song` reply to song name :\
    \nUSAGE:finds the song you entered in query and sends it"
})    
