import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Silakan mulai berbicara...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language='id-ID')
        except sr.UnknownValueError:
            return "Maaf, suara tidak dikenali."
        except sr.RequestError:
            return "Terjadi kesalahan pada layanan Speech-to-Text."
