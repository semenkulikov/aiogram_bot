from sqlalchemy import ForeignKey, Column, Integer, String, DateTime, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime


Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    article = Column('article', Integer, unique=True, nullable=False)
    price = Column('price', Float, nullable=False)
    rating = Column('rating', Integer)
    count = Column('count', Integer)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "<Product(name='{name}', article='{article}', price='{price}')>".format(
            name=self.name, article=self.article, price=self.price)
