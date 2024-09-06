from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# Initialize the PyroFork Client
app = Client("my_bot", api_id="20028561", api_hash="0f3793daaf4d3905e55b0e44d8719cad", bot_token="6617412135:AAGu_MBkyufK47iUiUhPCap73z5XkwKH1Nk")

# Start command handler
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    user = message.from_user
    first_name = user.first_name
    
    profile_pic_url = None
    # Iterate over the generator to fetch the first profile photo
    async for photo in client.get_chat_photos(user.id, limit=1):
        # Download the profile photo and obtain the path
        file_path = await app.download_media(photo.file_id)
        profile_pic_url = file_path  # Set the file path as the URL
        break  # Stop after getting the first photo

    # Add first name and profile picture URL as query parameters
    web_app_url = f"https://bad4-178-128-81-202.ngrok-free.app/?first_name={first_name}"
    
    if profile_pic_url:
        web_app_url += f"&profile_pic_url={profile_pic_url}"

    keyboard = [[InlineKeyboardButton("Play Guess the Number", web_app=WebAppInfo(url=web_app_url))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await message.reply_text('Welcome to the Guess the Number game!', reply_markup=reply_markup)

# Start the bot
if __name__ == "__main__":
    app.run()
