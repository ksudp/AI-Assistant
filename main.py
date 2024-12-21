import speech_recognition as sr
import pyttsx3

# 음성 인식과 음성 출력 초기화
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    """사용자의 음성을 인식하여 텍스트로 변환"""
    with sr.Microphone() as source:
        print("말해주세요!")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language="ko-KR")
        except sr.UnknownValueError:
            return "죄송합니다. 음성을 이해하지 못했어요."

def speak(text):
    """텍스트를 음성으로 출력"""
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
            speak(f"당신이 말씀하신 내용은: {user_input}")