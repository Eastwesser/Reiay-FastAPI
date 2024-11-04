from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from api.i18n.i18n_helper import set_language
from api.i18n.request_culture_provider import RequestCultureProvider
import logging

logger = logging.getLogger("locale_middleware")


class LocaleMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Определение языка через RequestCultureProvider
        language = await RequestCultureProvider.determine_request_language(request)

        # Установка языка в текущем контексте
        set_language(language)

        logger.info(f"Культура запроса установлена: {language}")

        # Выполнение следующего middleware или обработчика
        response = await call_next(request)
        return response
