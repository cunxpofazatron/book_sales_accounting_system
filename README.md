echo "# Book Sales Accounting System

## Описание проекта
Система учёта продаж книг с использованием SQLAlchemy ORM.

## Установка и запуск
\`\`\`bash
# 1. Установите зависимости
pip install -r requirements.txt

# 2. Создайте базу данных
python create_db.py

# 3. Загрузите тестовые данные
python load_data.py

# 4. Запустите основной скрипт
python query_publisher.py
\`\`\`

## Использование
После запуска \`query_publisher.py\` введите имя или ID издателя для просмотра продаж.

## Структура проекта
- \`models.py\` - модели SQLAlchemy
- \`create_db.py\` - создание таблиц БД
- \`load_data.py\` - загрузка тестовых данных
- \`query_publisher.py\` - основной скрипт запросов

## Технологии
- Python 3.12
- SQLAlchemy 2.0
- SQLite (для разработки)
- PostgreSQL (опционально для продакшена)

## Автор
[Ваше имя]" > README.md