from celery import Celery

# Настройка Celery для работы с Redis
celery_app = Celery('tasks', broker='redis://localhost:6379/0')


@celery_app.task
def process_notification(user_id: int, message: str):
    print(f"Sending notification to user {user_id}: {message}")
