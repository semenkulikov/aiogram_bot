from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_subscribe(product_id):
    """
    Функция для рендеринга inline кнопок
    :param product_id: ID продукта
    :return: набор кнопок
    """
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Подписаться", callback_data=f"subscribe_{product_id}"
    )

    return builder.as_markup()
