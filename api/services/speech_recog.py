import speech_recognition as sr


def transcribe_audio(file_path: str):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(file_path)
    with audio_file as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)
