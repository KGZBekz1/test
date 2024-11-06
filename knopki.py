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
        InlineKeyboardButton("Наш сайт", url="https://example.com"),
        InlineKeyboardButton("Инстаграм", url="https://instagram.com/example")
    )
    await message.reply(greeting_text, reply_markup=keyboard)
