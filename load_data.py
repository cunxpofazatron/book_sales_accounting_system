from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Publisher, Book, Shop, Stock, Sale
from create_db import engine


def load_data():
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Очищаем существующие данные (если есть)
        session.query(Sale).delete()
        session.query(Stock).delete()
        session.query(Book).delete()
        session.query(Shop).delete()
        session.query(Publisher).delete()

        # Создаем тестовые данные
        # Издатели
        publisher1 = Publisher(id=1, name="Пушкин")
        publisher2 = Publisher(id=2, name="Толстой")

        # Магазины
        shop1 = Shop(id=1, name="Буквоед")
        shop2 = Shop(id=2, name="Лабиринт")
        shop3 = Shop(id=3, name="Книжный дом")

        # Книги
        book1 = Book(id=1, title="Капитанская дочка", publisher=publisher1)
        book2 = Book(id=2, title="Руслан и Людмила", publisher=publisher1)
        book3 = Book(id=3, title="Евгений Онегин", publisher=publisher1)
        book4 = Book(id=4, title="Война и мир", publisher=publisher2)

        # Запасы в магазинах
        stock1 = Stock(id=1, book=book1, shop=shop1, count=10)
        stock2 = Stock(id=2, book=book2, shop=shop1, count=5)
        stock3 = Stock(id=3, book=book1, shop=shop2, count=8)
        stock4 = Stock(id=4, book=book3, shop=shop3, count=12)

        # Продажи
        sale1 = Sale(id=1, price=600, date_sale=datetime(2022, 11, 9), stock=stock1)
        sale2 = Sale(id=2, price=500, date_sale=datetime(2022, 11, 8), stock=stock2)
        sale3 = Sale(id=3, price=580, date_sale=datetime(2022, 11, 5), stock=stock3)
        sale4 = Sale(id=4, price=490, date_sale=datetime(2022, 11, 2), stock=stock4)
        sale5 = Sale(id=5, price=600, date_sale=datetime(2022, 10, 26), stock=stock1)

        # Добавляем все объекты
        session.add_all([
            publisher1, publisher2,
            shop1, shop2, shop3,
            book1, book2, book3, book4,
            stock1, stock2, stock3, stock4,
            sale1, sale2, sale3, sale4, sale5
        ])

        session.commit()
        print("✅ Тестовые данные успешно загружены!")
        print("\n📊 Загружено:")
        print(f"   • Издателей: {session.query(Publisher).count()}")
        print(f"   • Книг: {session.query(Book).count()}")
        print(f"   • Магазинов: {session.query(Shop).count()}")
        print(f"   • Записей о запасах: {session.query(Stock).count()}")
        print(f"   • Продаж: {session.query(Sale).count()}")

    except Exception as e:
        session.rollback()
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
    finally:
        session.close()


if __name__ == "__main__":
    load_data()