import os
from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router

API_TOKEN = "6617412135:AAGu_MBkyufK47iUiUhPCap73z5XkwKH1Nk"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()

# Ensure the 'static' folder exists to store the images
if not os.path.exists("static/profile_pics"):
    os.makedirs("static/profile_pics")

@router.message(Command("start"))
async def start(message):
    user = message.from_user
    first_name = user.first_name
    username = user.username if user.username else "NoUsername"
    user_id = user.id

    profile_pic_url = None
    photos = await bot.get_user_profile_photos(user.id, limit=1)

    # Handle profile picture
    if photos and photos.total_count > 0:
        file_id = photos.photos[0][0].file_id
        file_info = await bot.get_file(file_id)
        file = await bot.download_file(file_info.file_path)

        # Save the downloaded file to the static folder
        static_file_path = f"static/profile_pics/{user.id}.jpg"
        with open(static_file_path, 'wb') as out_file:
            out_file.write(file.getvalue())
        profile_pic_url = f"/static/profile_pics/{user.id}.jpg"

    # Use default image if no profile pic is available
    if not profile_pic_url:
        profile_pic_url = "/static/profile_pics/default.jpg"

    # Add first name, profile picture URL, user ID, and username as query parameters
    web_app_url = (f"https://1dab-178-128-81-202.ngrok-free.app/?first_name={first_name}"
                   f"&profile_pic_url={profile_pic_url}&user_id={user_id}&username={username}")

    # Creating inline button
    keyboard = [[InlineKeyboardButton(text="View Profile", web_app=WebAppInfo(url=web_app_url))]]
    reply_markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    # Send the reply
    await message.answer(f'Hello {first_name}! Click the button below to view your profile.', reply_markup=reply_markup)

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
