from fastapi import Request

import logging

from i18n.i18n_helper import translations_path

logger = logging.getLogger("request_culture_provider")

class RequestCultureProvider:
    @staticmethod
    async def determine_request_language(request: Request) -> str:
        """Определяет язык из строки запроса или заголовков."""
        lang_query = request.query_params.get("lang")
        if lang_query:
            if RequestCultureProvider.is_valid_culture(lang_query):
                logger.info(f"Выбранный язык из параметров запроса: {lang_query}")
                return lang_query
            else:
                logger.warning(f"Недействительный язык запроса: {lang_query}. Установлен по умолчанию 'ru'.")

        accept_language = request.headers.get("Accept-Language", "en").split(",")[0]
        logger.info(f"Выбранный язык из заголовка: {accept_language}")

        if RequestCultureProvider.is_valid_culture(accept_language):
            return accept_language

        logger.warning("Не удалось определить язык, используется 'ru' по умолчанию")
        return "ru"

    @staticmethod
    def is_valid_culture(language: str) -> bool:
        """Проверяет, является ли язык допустимым."""
        try:
            Translations.load(translations_path, locales=[language])
            return True
        except Exception:
            return False
