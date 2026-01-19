from sqlalchemy import create_engine
from models import Base

# Используем SQLite для выполнения задания
engine = create_engine('sqlite:///book_sales.db', echo=False)

def create_tables():
    Base.metadata.create_all(engine)
    print("✅ Таблицы успешно созданы в book_sales.db")
    print("📊 Созданные таблицы:")
    for table_name in Base.metadata.tables.keys():
        print(f"   • {table_name}")

if __name__ == "__main__":
    create_tables()