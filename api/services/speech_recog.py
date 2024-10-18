# Распознавание речи
import speech_recognition as sr


# Функция для преобразования аудио в текст
def transcribe_audio(file_path: str) -> str:
    """Использует Google API для преобразования аудио в текст."""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results; {e}"
