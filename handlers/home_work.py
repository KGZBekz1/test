from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from bot_config import database

homework_router = Router()

class Homework(StatesGroup):
    name = State()
    group_name = State()
    number_hw = State()
    link = State()


@homework_router.message(Command("homework"))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Homework.name)
    await message.answer("Как вас зовут?")


@homework_router.message(Homework.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Homework.group_name)
    await message.answer("Укажите свою группу: ")

@homework_router.message(Homework.group_name)
async def process_group(message: types.Message, state: FSMContext):
    await state.update_data(group_name=message.text)
    await state.set_state(Homework.number_hw)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="1"),
                types.KeyboardButton(text="2"),
                types.KeyboardButton(text="3"),
                types.KeyboardButton(text="4"),
                types.KeyboardButton(text="5"),
                types.KeyboardButton(text="6"),
                types.KeyboardButton(text="7"),
                types.KeyboardButton(text="8")
            ]
        ]
    )
    await message.answer("Укажите номер домашнего задания: ", reply_markup=kb)

@homework_router.message(Homework.number_hw,  F.text.in_(("1", "2", "3", "4", "5", "6", "7", "8")))
async def process_number_hw(message: types.Message, state: FSMContext):
    await state.update_data(number_hw=message.text)
    await state.set_state(Homework.link)
    await message.answer("Пожалуйста, прикрепите ссылку на свой проект: ")

@homework_router.message(Homework.link)
async def process_link(message: types.Message, state: FSMContext):
    await state.update_data(link=message.text)
    await message.answer("Домашка записана")
    data = await state.get_data()
    print(data)

    database.execute(
        query="""
        INSERT INTO homeworks (name, group_name, number_hw, link)
        VALUES (?, ?, ?, ?)
        """,
        params=(data["name"], data["group_name"], data["number_hw"], data["link"]),
    )

    await state.clear()
