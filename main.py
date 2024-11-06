import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values


token = dotenv_values(".env")["TELEGRAM_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()


unique_users = set()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    user_id = message.from_user.id

    unique_users.add(user_id)
    user_count = len(unique_users)

    msg = f"Привет, {name}, наш бот обслуживает уже {user_count} пользователя."
    await message.answer(msg)


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    unique_users.add(message.from_user.id)
    user_count = len(unique_users)
    greeting_text = (
        f"Привет, {message.from_user.first_name}!\n"
        f"Бот обслуживает уже {user_count} пользователей."
    )

    # Кнопки
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Model Overview | Porsche Car Configurator", url="https://configurator.porsche.com/model-start/pictures/718/extcam01.webp"),
        InlineKeyboardButton("Porsche Cayenne 2023", url="https://www.ixbt.com/img/x780/n1/news/2023/3/2/it-4YkUkw-1681753319%20copy_large.jpg")
    )
    await message.reply(greeting_text, reply_markup=keyboard)


@dp.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username or "Не указан"

    msg = f"Ваш id: {user_id}\nВаше имя: {first_name}\nВаш юзернейм: {username}"
    await message.answer(msg)

@dp.message(Command("random"))
async def random_name_handler(message: types.Message):
    names = ("Игорь", "Анастасия", "Владимир", "Екатерина", "Сергей")
    random_name = random.choice(names)
    await message.answer(f"Случайное имя: {random_name}")

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(message.text)

async def main():

    await dp.start_polling(bot)

if __name__ == 'main':
    asyncio.run(main())