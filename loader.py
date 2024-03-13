from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config_data import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler


scheduler = AsyncIOScheduler()
dp = Dispatcher()
bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML)
