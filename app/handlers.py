#imports
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random

import app.keyboards as kb

router = Router()

#command
#/start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! Это бот который вы будете использовать вместо кубика.",
                         reply_markup=kb.main)

@router.message(Command('git'))
async def git_my(message: Message):
    await message.answer(f'Мой гит-хаб: ', reply_markup=kb.git_button)

@router.message(F.text == ("бросить кубик"))
async def cmd_roll(message: Message):
    number = random.randint(1, 6)
    await message.answer(f"🎲 Вам выпало число: {number}")