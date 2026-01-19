from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
from models import Publisher, Book, Shop, Stock, Sale
from create_db import engine


def get_publisher_sales():
    # Создание сессии
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Ввод имени или идентификатора издателя
        publisher_input = input("Введите имя или идентификатор издателя: ").strip()

        # Определяем, введено ли число (ID) или строка (имя)
        if publisher_input.isdigit():
            # Поиск по ID
            publisher = session.query(Publisher).filter(Publisher.id == int(publisher_input)).first()
        else:
            # Поиск по имени (регистронезависимый)
            publisher = session.query(Publisher).filter(
                Publisher.name.ilike(f"%{publisher_input}%")
            ).first()

        if not publisher:
            print(f"❌ Издатель '{publisher_input}' не найден.")
            print("\n📋 Доступные издатели:")
            publishers = session.query(Publisher).all()
            for p in publishers:
                print(f"   • {p.id}: {p.name}")
            return

        # Запрос выборки продаж книг издателя
        query = (
            session.query(
                Book.title.label('book_title'),
                Shop.name.label('shop_name'),
                Sale.price,
                Sale.date_sale
            )
            .join(Publisher, Book.publisher_id == Publisher.id)
            .join(Stock, Stock.book_id == Book.id)
            .join(Shop, Shop.id == Stock.shop_id)
            .join(Sale, Sale.stock_id == Stock.id)
            .filter(Publisher.id == publisher.id)
            .order_by(Sale.date_sale.desc())
        )

        # Вывод результатов
        print(f"\n{'=' * 60}")
        print(f"📚 ПРОДАЖИ КНИГ ИЗДАТЕЛЯ: {publisher.name}")
        print(f"{'=' * 60}")
        print(f"{'Название книги':<25} | {'Магазин':<12} | {'Цена':<8} | {'Дата':<10}")
        print(f"{'-' * 25}-+-{'-' * 12}-+-{'-' * 8}-+-{'-' * 10}")

        results = query.all()
        if not results:
            print("ℹ️  Нет данных о продажах.")
        else:
            total_sales = 0
            for book_title, shop_name, price, date_sale in results:
                formatted_date = date_sale.strftime('%d-%m-%Y')
                print(f"{book_title:<25} | {shop_name:<12} | {price:<8} | {formatted_date:<10}")
                total_sales += price

            print(f"{'-' * 60}")
            print(f"📈 Всего продаж: {len(results)} шт.")
            print(f"💰 Общая сумма: {total_sales} руб.")

        # Дополнительная статистика
        print(f"\n📊 Статистика по издателю:")
        books_count = session.query(Book).filter(Book.publisher_id == publisher.id).count()
        print(f"   • Книг в каталоге: {books_count}")

        # Книги издателя
        books = session.query(Book).filter(Book.publisher_id == publisher.id).all()
        print(f"   • Список книг:")
        for book in books:
            print(f"     - {book.title}")

    except Exception as e:
        print(f"❌ Ошибка при выполнении запроса: {e}")
    finally:
        session.close()


def show_all_data():
    """Функция для просмотра всех данных (для отладки)"""
    Session = sessionmaker(bind=engine)
    session = Session()

    print("\n📋 ВСЕ ДАННЫЕ В БАЗЕ:")

    print("\n📚 Издатели:")
    for p in session.query(Publisher).all():
        print(f"   {p.id}: {p.name}")

    print("\n🏪 Магазины:")
    for s in session.query(Shop).all():
        print(f"   {s.id}: {s.name}")

    print("\n📖 Книги:")
    for b in session.query(Book).all():
        publisher = session.query(Publisher).filter(Publisher.id == b.publisher_id).first()
        print(f"   {b.id}: '{b.title}' (Издатель: {publisher.name})")

    session.close()


if __name__ == "__main__":
    # Сначала покажем все данные
    show_all_data()

    # Основной запрос
    while True:
        print(f"\n{'=' * 60}")
        print("🔍 ПОИСК ПРОДАЖ ПО ИЗДАТЕЛЮ")
        print("(для выхода введите 'exit' или 'quit')")
        print(f"{'=' * 60}")

        get_publisher_sales()

        again = input("\nПродолжить поиск? (y/n): ").strip().lower()
        if again not in ['y', 'yes', 'да', 'д']:
            print("\n👋 Завершение работы.")
            break