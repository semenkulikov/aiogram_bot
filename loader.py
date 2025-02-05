import os
from logging.handlers import RotatingFileHandler

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config_data import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging

from config_data.config import BASE_DIR

scheduler = AsyncIOScheduler()
dp = Dispatcher()
bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML)

log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s - %(message)s')
logs_path = os.path.join(BASE_DIR, "logs")

if not os.path.exists(logs_path):
    os.makedirs(logs_path)

file_handler = RotatingFileHandler(
    os.path.join(logs_path, "bot.log"),
    mode='a', maxBytes=2*1024*1024, backupCount=1, encoding="utf8"
)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
stream_handler.setLevel(logging.INFO)

app_logger = logging.getLogger("app_logger")
app_logger.setLevel(logging.INFO)
app_logger.addHandler(file_handler)
app_logger.addHandler(stream_handler)

