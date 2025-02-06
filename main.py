from config_data.config import DEFAULT_COMMANDS
from aiogram import types
from loader import bot, dp, scheduler, app_logger
import asyncio
import handlers
from database.engine import create_db, session_maker
from middlewares.db import DataBaseSession


async def on_startup(bot):

    run_param = False
    if run_param:
        # await drop_db()
        pass
    app_logger.info("Подключение к базе данных...")
    await create_db()


async def on_shutdown(bot):
    app_logger.info('Бот успешно прекратил работу!')


async def main() -> None:
    app_logger.info("Запускаю бота...")
    dp.include_routers(handlers.default_heandlers.start.router,
                       handlers.default_heandlers.help.router,
                       handlers.custom_heandlers.handlers.router,
                       handlers.default_heandlers.echo.router,
                       )
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=DEFAULT_COMMANDS, scope=types.BotCommandScopeAllPrivateChats())
    bot_username = await bot.get_me()
    app_logger.info(f"Бот @{bot_username.username} запущен успешно.")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == '__main__':
    asyncio.run(main())
