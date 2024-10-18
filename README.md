# Reiai-FastAPI

## Описание

Это проект на FastAPI для создания мессенджера с использованием SQLAlchemy 2.0, Celery и Redis.

### Основные технологии:
- **FastAPI** — для создания асинхронного API.
- **SQLAlchemy 2.0** — ORM для работы с базами данных.
- **Alembic** — для управления миграциями базы данных.
- **Redis** — для кэширования и брокера сообщений Celery.
- **Celery** — для фоновых задач и уведомлений.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/<your-repo>/Reiai-FastAPI.git
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Настройте переменные окружения в файле .env:
```bash
DB_LOGIN=<ваш логин>
DB_PASS=<ваш пароль>
DB_HOST=localhost
DB_NAME=reiay_main
SECRET_KEY=<ваш секретный ключ>
```

4. Запустите Alembic для миграций:
```bash
alembic upgrade head
```

5. Запустите приложение:
```bash
uvicorn main:app --reload
```
