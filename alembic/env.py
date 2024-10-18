from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from core.database.db_configs import Base  # Импортируем метаданные

# Настройка логирования для Alembic
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Указываем метаданные для автоматической генерации миграций
target_metadata = Base.metadata


# Функция для оффлайн миграции
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


# Функция для онлайн миграции
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
