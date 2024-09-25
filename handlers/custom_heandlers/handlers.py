import sqlalchemy.exc
from aiogram.types import Message, CallbackQuery
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from states.states import ProductInfo
from database.models import Product
from sqlalchemy.ext.asyncio import AsyncSession
from aiohttp import ClientSession
from keyboards.inline.inline_keyboards import get_inline_subscribe
from loader import scheduler
from sqlalchemy import select, desc
from utils.funcs import get_text_for_product


router = Router()
ARTICLES = []


@router.message(
    F.text.lower() == "получить информацию по товару")
async def get_article_product(message: Message, state: FSMContext):
    # Это функция для получения артиклей продуктов
    await message.reply("Хорошо, введите артикул товара")
    await state.set_state(ProductInfo.get_article)


@router.message(ProductInfo.get_article)
async def get_info_product(message: Message, state: FSMContext, session: AsyncSession):
    """
    Функция для получения информации о продукте
    :param message: объект Message
    :param state: состояние
    :param session: сессия
    :return: None
    """
    try:
        article = int(message.text)
    except ValueError:
        await message.answer("Введите корректный артикул!")
        return
    path = f"https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={article}"
    async with ClientSession() as http_session:
        async with http_session.get(path) as response:
            data = await response.json()
    try:
        product_data: dict = data.get("data").get("products")[0]
    except IndexError:
        await message.answer("Товар с таким артикулом не найден")
        await state.set_state(None)
        return
    name = product_data.get("name")
    price = product_data.get("salePriceU") // 100
    rating = product_data.get("reviewRating")
    count = sum([len(seller.get("stocks")) for seller in product_data.get("sizes")])

    new_product = Product(
        name=name,
        article=article,
        price=price,
        rating=rating,
        count=count,
    )
    session.add(new_product)

    try:
        await session.commit()
    except sqlalchemy.exc.IntegrityError:
        pass

    result_text = (f"Вот информация по товару с артикулом {article}:\n"
                   f"Название: {name}\n"
                   f"Артикул: {article}\n"
                   f"Цена: {price}\n"
                   f"Рейтинг товара: {rating}\n"
                   f"Количество товара на всех складах: {count}")
    await message.answer(result_text, reply_markup=get_inline_subscribe(article))
    await state.set_state(None)


@router.callback_query(F.data.startswith("subscribe_"))
async def send_random_value(callback: CallbackQuery, session: AsyncSession):
    """
    Функция для установки рандомного значения
    :param callback: объект Collback
    :param session: объект сессии
    :return: None
    """
    product_article = callback.data.split("_")[1]
    query = select(Product).where(Product.article == product_article)
    result = await session.execute(query)
    product = result.scalar()
    result_text = get_text_for_product(product)
    scheduler.add_job(callback.bot.send_message, "interval", minutes=5, args=(callback.from_user.id, result_text))
    await callback.answer(
        "Вы подписались на уведомления!",
        show_alert=True
    )


@router.message(F.text.lower() == "остановить уведомления")
async def stopping_notifications(message: Message):
    for job in scheduler.get_jobs():
        job.remove()
    await message.reply("Получение уведомлений прекращено!")


@router.message(F.text.lower() == "получить информацию из бд")
async def get_products(message: Message, session: AsyncSession):
    query = select(Product).order_by(desc(Product.created_at)).limit(5)
    result = await session.execute(query)
    products = result.scalars()
    await message.reply("Вот последние 5 записей из БД:")
    for product in products:
        await message.answer(get_text_for_product(product))
