import bcrypt


def hash_password(password: str) -> bytes:
    """Хеширование пароля."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def verify_password(password: str, hashed: str) -> bool:
    """Проверка пароля."""
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    except ValueError:
        return False
