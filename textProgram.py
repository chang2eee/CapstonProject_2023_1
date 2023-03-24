import speech_recognition as sr
import os
import time
from hanspell import spell_checker
import kss

# 녹음 시작 함수 
# 녹음이 끝났다고 감지하면, 바로 프로그램이 종료되게 설정

# txt 파일 명칭 지정
text_file = "myInterview.txt"

# startRecord 함수는 runningTime을 반환하는 동시에 녹음의 기능까지 하는 함수
def startRecord():
    # 텍스트 파일 생성   
    
    with open(text_file, 'w', encoding='UTF-8'):
        pass

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("녹음을 시작합니다.")
        start_time = time.time()    
        audio = r.listen(source)
        text = r.recognize_google(audio, language='ko-KR')
        print("인식 결과 : " + text)

        # 텍스트 파일에 결과 추가
        with open(text_file, 'a', encoding='UTF-8') as f:
            f.write(text + "\n")
        
        end_time = time.time()
        runningTime = end_time - start_time
        print("녹음이 끝났습니다.")
        print("총 녹음시간 : {:.2f}초".format(runningTime))

        return runningTime

final_runningTime = startRecord()   

# 띄어쓰기 및 맞춤법 수정 코드

with open(text_file, 'r', encoding='UTF-8') as file:
    lines = file.readlines()    

# 수정된 문장 저장할 리스트 초기화 
new_lines = []

# 오타 수정과 띄어쓰기 교정
for line in lines:
    # 한글 문자 오타 수정
    spelled_sent = spell_checker.check(line.strip())
    corrected_sent = spelled_sent.checked
    # 한글 문장 띄어쓰기 교정
    spacing_sent = kss.split_sentences(corrected_sent)
    # 수정된 문장 저장
    new_lines.extend(spacing_sent)

# 수정된 문장을 파일에 쓰기
with open(text_file, 'w', encoding='UTF-8') as f:
    for line in new_lines:
        f.write(line.strip() + '\n')