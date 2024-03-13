from aiogram.fsm.state import StatesGroup, State


class ProductInfo(StatesGroup):
    get_article = State()
