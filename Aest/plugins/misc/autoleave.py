import asyncio
from datetime import datetime

from pyrogram.enums import ChatType

import config
from pyrogram.errors import FloodWait
from Aest import app
from Aest.core.call import Anony, autoend
from Aest.utils.database import get_client, is_active_chat, is_autoend


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT:
        while not await asyncio.sleep(900):
            from Aest.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for i in client.get_dialogs():
                        if i.chat.type in [
                            ChatType.SUPERGROUP,
                            ChatType.GROUP,
                            ChatType.CHANNEL,
                        ]:
                            if (
                                i.chat.id != config.LOGGER_ID
                            ):
                                if left == 20:
                                    continue
                                if not await is_active_chat(i.chat.id):
                                    try:
                                        await client.leave_chat(i.chat.id)
                                        left += 1
                                    except:
                                        continue
                except FloodWait as aes:
                    flood_time = int(aes.value)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
                except:
                    continue


asyncio.create_task(auto_leave())


async def auto_end():
    while not await asyncio.sleep(5):
        ender = await is_autoend()
        if not ender:
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await Anony.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "» ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
                    )
                except:
                    continue


asyncio.create_task(auto_end())
