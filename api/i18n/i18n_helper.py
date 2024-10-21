import os

from babel.support import Translations

# Устанавливаем путь к переводам
translations_path = os.path.join(os.path.dirname(__file__), 'translations')


# Загружаем переводы для нужного языка
def set_language(language: str) -> Translations:
    """Устанавливает текущий язык для перевода."""
    translation_dir = os.path.join(translations_path, language, 'LC_MESSAGES')
    if os.path.exists(os.path.join(translation_dir, 'messages.mo')):
        translations = Translations.load(translation_dir, locales=[language])
    else:
        translations = Translations.load(translation_dir, locales=['en'])
    return translations


def translate(key: str) -> str:
    """Перевод строки по ключу."""
    translations = set_language('ru')  # Здесь можно использовать текущий язык
    return translations.gettext(key)
