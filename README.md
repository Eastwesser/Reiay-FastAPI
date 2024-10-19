# Reiai-FastAPI

## Описание

Это проект на FastAPI для создания мессенджера с использованием SQLAlchemy 2.0, Alembic и Redis.

### Основные технологии:

- **FastAPI** — для создания асинхронного API.
- **SQLAlchemy 2.0** — ORM для работы с базами данных.
- **Alembic** — для управления миграциями базы данных.
- **Redis** — для кэширования и брокера сообщений Celery.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Eastwesser/Reiai-FastAPI.git
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Настройте переменные окружения в файле .env:

```bash
DB_LOGIN=<ваш логин>
DB_PASS=<ваш пароль>
DB_HOST=localhost:5432
DB_NAME=reiay
```

4. Запустите Alembic для миграций:

```bash
alembic upgrade head
```

5. Запустите приложение:

```bash
uvicorn api.main:app --reload
```

6. Доступ к Swagger:

```bash
http://127.0.0.1:8000/docs

```
