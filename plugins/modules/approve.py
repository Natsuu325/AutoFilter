import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import CHAT_ID, APPROVED 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client, message: ChatJoinRequest):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        buttons = [[ 
            InlineKeyboardButton('ᴊᴏɪɴ ᴍʏ channel', url=f'https://t.me/kdrama_time')
            
        ]]
        markup = InlineKeyboardMarkup(buttons)
        caption = f"<b>{message.from_user.mention()},\n\nʀᴇǫᴜᴇsᴛ ʜᴀs ʙᴇᴇɴ ᴀᴄᴄᴇᴘᴛᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {message.chat.title}</b>"
        await client.send_photo(
            message.from_user.id, 
            photo='Nahi Btauga', 
            caption=caption, 
            reply_markup=markup
        )
