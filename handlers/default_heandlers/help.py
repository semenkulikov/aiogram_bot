from aiogram.types import Message
from config_data.config import DEFAULT_COMMANDS
from aiogram import F, Router
from aiogram.filters import Command


router = Router()


@router.message(F.text, Command("help"))
async def bot_help(message: Message):
    text = [f'/{command[1]} - {desk[1]}' for command, desk in DEFAULT_COMMANDS]
    await message.answer('Доступные команды:\n{}'.format("\n".join(text)))
