from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

API_ID = 39088914
API_HASH = '1d6dcd6f0574fdf5c75ed727f3ec87c8'
BOT_TOKEN = '8943342705:AAEMFghzDO8z_dITc_QIX9Et3p2MIYTR8E4'

app = Client("vc_music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message: Message):
    # Yahan inline buttons diye gaye hain
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎵 Play Song", callback_data="play_song")],
        [InlineKeyboardButton("🛑 Stop Song", callback_data="stop_song")]
    ])
    await message.reply(
        "👋 **Bot online hai!**\n\nVoice chat mein music play karne ke liye neeche diye gaye buttons ka use karein:", 
        reply_markup=keyboard
    )

@app.on_callback_query()
async def callback_handler(client, callback_query):
    if callback_query.data == "play_song":
        await callback_query.answer("▶️ Play button dabaya gaya!", show_alert=True)
    elif callback_query.data == "stop_song":
        await callback_query.answer("⏹️ Stop button dabaya gaya.", show_alert=True)

app.run()
