from aiogram import types, Router

router = Router()


@router.message()
async def echo_handler(message: types.Message) -> None:
    await message.reply(f"Введите любую команду из меню, чтобы я начал работать\n"
                        f"Либо выберите одну из кнопок, которые я вам прислал")
