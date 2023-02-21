import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from pyrogram.errors import MediaCaptionTooLong
from transcripts import *


sudo_users = [1953040213, 5144980226, 874964742,839221827, 5294965763, 5317652430, 5141357700]

# BOT INFO
TOKEN = os.environ.get("BOT_TOKEN", "133:sdsdsd")
API_HASH = os.environ.get("HASH", "ghghghghgh")
API_ID = int(os.environ.get("ID", "123456"))


app = Client("Url-Short-app", api_id=API_ID,
             api_hash=API_HASH, bot_token=TOKEN, workers=50)


# Start Button
start_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("❓ HELP", callback_data="help_data"),
     InlineKeyboardButton("About me 🤖", callback_data="about_data"),
     ],
    [InlineKeyboardButton("Connect Your API 🔗", callback_data="connect_api"
                          ), ]
])


# Back Button
about_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("◀️ Back️", callback_data="back_data"), ],
])


# Connect button
connect_btns = InlineKeyboardMarkup([
    [InlineKeyboardButton("GET API TOKEN 🔑", url="https://oggyLink.com/member/tools/api")],
    [InlineKeyboardButton("❓ HELP", callback_data="help_data"), InlineKeyboardButton("◀️ Back️", callback_data="back_data")]
])
