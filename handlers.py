from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import Dispatcher

unique_users = set()

async def start_command(message: types.Message):
    unique_users.add(message.from_user.id)
    user_count = len(unique_users)
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Наш сайт", url="https://example.com"),
        InlineKeyboardButton("Инстаграм", url="https://instagram.com/example")
    )
    await message.reply(
        f"Привет, {message.from_user.first_name}!\n"
        f"Бот обслуживает уже {user_count} пользователей.",
        reply_markup=keyboard
    )

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
