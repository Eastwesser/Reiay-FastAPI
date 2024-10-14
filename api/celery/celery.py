from celery import Celery

# Создаем объект приложения Celery с указанием брокера сообщений (Redis)
celery_app = Celery('tasks', broker='redis://localhost:6379/0')


# Пример задачи для отправки уведомления
@celery_app.task
def process_notification(user_id: int, message: str):
    print(f"Sending notification to user {user_id}: {message}")
