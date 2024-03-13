from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Получить информацию по товару")
    kb.button(text="Остановить уведомления")
    kb.button(text="Получить информацию из БД")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder="Выберите одну из кнопок")
