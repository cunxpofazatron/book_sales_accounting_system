import json
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Publisher, Book, Shop, Stock, Sale
from create_db import engine

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Чтение JSON-файла
with open('fixtures.json', 'r') as file:
    data = json.load(file)

# Создание экземпляров моделей и сохранение в БД
for publisher_data in data['publishers']:
    publisher = Publisher(name=publisher_data['name'])
    session.add(publisher)

for book_data in data['books']:
    book = Book(title=book_data['title'],
                publisher_id=book_data['publisher_id'])
    session.add(book)

for shop_data in data['shops']:
    shop = Shop(name=shop_data['name'])
    session.add(shop)

for stock_data in data['stocks']:
    stock = Stock(book_id=stock_data['book_id'],
                  shop_id=stock_data['shop_id'], count=stock_data['count'])
    session.add(stock)

for sale_data in data['sales']:
    sale = Sale(price=sale_data['price'], date_sale=datetime.strptime(
        sale_data['date_sale'], '%Y-%m-%d'), stock_id=sale_data['stock_id'])
    session.add(sale)

# Сохранение изменений
session.commit()
