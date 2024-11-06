from aiogram import types, Router, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Application
from aiogram.filters import Command

# Уникальные пользователи
unique_users = set()

# Создаем маршрутизатор и приложение
router = Router()


@router.message(Command("start"))
async def start_command(message: types.Message):
    unique_users.add(message.from_user.id)
    user_count = len(unique_users)

    # Создаем клавиатуру
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Model Overview | Porsche Car Configurator",
                              url="https://configurator.porsche.com")],
        [InlineKeyboardButton(text="Porsche Cayenne 2023", url="https://www.ixbt.com/img/x780/n1/news/2023")],
    ])

    await message.reply(
        text=f"Привет, {message.from_user.first_name}!\n"
             f"Бот обслуживает уже {user_count} пользователей!",
        reply_markup=keyboard
    )


# Создаем экземпляр приложения и запускаем его
app = Application(token="TELEGRAM_TOKEN")
app.include_router(router)

if __name__ == "main":
    app.run_polling()
