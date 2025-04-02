from aiogram.fsm.state import StatesGroup, State


class ProductInfo(StatesGroup):
    """ Состояния для модели продуктов """
    get_article = State()
