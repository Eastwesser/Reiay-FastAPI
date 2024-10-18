# Модуль для хеширования паролей

import bcrypt


# Функция для хеширования пароля
def hash_password(password: str) -> bytes:
    """Хеширование пароля с использованием bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


# Функция для проверки пароля
def verify_password(password: str, hashed: str) -> bool:
    """Проверка пароля на соответствие хешу."""
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    except ValueError:
        return False
