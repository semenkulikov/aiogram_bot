from aiogram.types import Message
from config_data.config import DEFAULT_COMMANDS
from aiogram import F, Router
from aiogram.filters import Command

from loader import app_logger

router = Router()


@router.message(F.text, Command("help"))
async def bot_help(message: Message):
    text = [f'/{command[1]} - {desk[1]}' for command, desk in DEFAULT_COMMANDS]
    app_logger.info(f"Пользователь {message.from_user.full_name} вызвал команду /help")
    await message.answer('Доступные команды:\n{}'.format("\n".join(text)))
