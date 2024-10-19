from celery import Celery

# Создаем приложение Celery
celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",  # URL брокера, например Redis
    backend="redis://localhost:6379/0",  # URL для результата задач
)

# Настройки для Celery
celery_app.conf.update(
    result_expires=3600,  # Время жизни результата задач
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
)


@celery_app.task
def add(x, y):
    return x + y
