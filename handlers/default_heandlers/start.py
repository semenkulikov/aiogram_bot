from aiogram.types import Message
from aiogram import Router
from aiogram.filters import CommandStart
from keyboards.reply.reply_keyboards import get_menu
from loader import app_logger

router = Router()


@router.message(CommandStart())
async def bot_start(message: Message):
    app_logger.info(f"Пользователь {message.from_user.full_name} запустил бота!")
    await message.answer(f"""
    Здравствуйте, {message.from_user.full_name}! Я - телеграм бот.
Чтобы узнать все мои команды, введите /help
    """, reply_markup=get_menu())
