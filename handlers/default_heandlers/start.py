from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart
from keyboards.reply.reply_keyboards import get_menu


router = Router()


@router.message(CommandStart())
async def bot_start(message: Message):
    await message.answer(f"""
    Здравствуйте, {message.from_user.full_name}! Я - телеграм бот.
Чтобы узнать все мои команды, введите /help
    """, reply_markup=get_menu())
