import os
from dotenv import load_dotenv, find_dotenv
from aiogram.types import BotCommand

if not find_dotenv():
    exit('Переменные окружения не загружены, т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
DEFAULT_COMMANDS = (
    BotCommand(command='start', description='Запустить бота'),
    BotCommand(command='help', description='Вывести справку'),
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_TO_PYTHON = os.path.normpath(os.path.join(BASE_DIR, "venv/Scripts/python.exe"))


HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
USERNAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
DB_NAME = os.getenv('DB_NAME')

DATABASE_URL = f"postgresql+asyncpg://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

# DATABASE_URL = "sqlite+aiosqlite:///my_base.db"
