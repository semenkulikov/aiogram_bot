from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from config_data.config import DATABASE_URL
from database.models import Base


engine = create_async_engine(DATABASE_URL)
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    """ Функция для создания базы данных """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    """ Функция для удаления базы данных """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
