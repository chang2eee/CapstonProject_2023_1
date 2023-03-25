import speech_recognition as sr

#*.mp3 -> *.txt
def convertToText(audio_file):
    r = sr.Recognizer()
    audio = sr.AudioFile(audio_file)
    
    with audio as source:
        audio_data = r.record(source)
    
    text = r.recognize_google(audio_data, language="ko-KR")

    return text