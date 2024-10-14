from api.redis import Redis

# Настройка подключения к Redis
redis_client = Redis(host='localhost', port=6379, db=0)


# Пример использования Redis
def save_message_in_cache(user_id: int, message: str):
    redis_client.set(f"user:{user_id}:last_message", message)
