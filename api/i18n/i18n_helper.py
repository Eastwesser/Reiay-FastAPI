import os
from babel.support import Translations

# Устанавливаем путь к файлам переводов
translations_path = os.path.join(os.path.dirname(__file__), 'translations')

# Загрузка переводов для конкретного языка
def load_translation(language: str) -> Translations:
    """Загружает переводы для заданного языка."""
    translation_dir = os.path.join(translations_path, language, 'LC_MESSAGES')
    if os.path.exists(os.path.join(translation_dir, 'messages.mo')):
        return Translations.load(translation_dir, locales=[language])
    return Translations.load(translation_dir, locales=['en'])

# Текущий язык (можно менять во время запроса)
_current_language = 'en'

def set_language(language: str):
    """Устанавливает текущий язык для перевода."""
    global _current_language
    _current_language = language

def translate(key: str) -> str:
    """Перевод строки по ключу."""
    translations = load_translation(_current_language)
    return translations.gettext(key)
