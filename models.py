from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'Publisher(id={self.id}, name={self.name})'


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    publisher_id = Column(Integer, ForeignKey('publisher.id'), nullable=False)
    publisher = relationship("Publisher", backref="books")

    def __repr__(self):
        return f'Book(id={self.id}, title={self.title}, publisher_id={self.publisher_id})'


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'Shop(id={self.id}, name={self.name})'


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), nullable=False)
    shop_id = Column(Integer, ForeignKey('shop.id'), nullable=False)
    count = Column(Integer, nullable=False)
    book = relationship("Book", backref="stocks")
    shop = relationship("Shop", backref="stocks")

    def __repr__(self):
        return f'Stock(id={self.id}, book_id={self.book_id}, shop_id={self.shop_id}, count={self.count})'


class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    date_sale = Column(Date, nullable=False)
    stock_id = Column(Integer, ForeignKey('stock.id'), nullable=False)
    stock = relationship("Stock", backref="sales")

    def __repr__(self):
        return f'Sale(id={self.id}, price={self.price}, date_sale={self.date_sale}, stock_id={self.stock_id})'
