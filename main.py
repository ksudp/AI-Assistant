import speech_recognition as sr
import pyttsx3

# 음성 인식과 음성 합성을 위한 설정
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("말해주세요!")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "죄송합니다. 잘 못 들었어요."

def speak(text):
    print(f"AI 비서: {text}")
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("안녕하세요! 무엇을 도와드릴까요?")
    while True:
        user_input = listen()
        if "종료" in user_input:
            speak("안녕히 가세요!")
            break
        else:
            speak(f"당신이 말한 것은: {user_input}")
