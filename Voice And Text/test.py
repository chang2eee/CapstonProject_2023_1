# 통합코드 작성 요청으로 작성

# 순서 : 녹음 -> 글자 수 계산 -> 말하기 속도 비교 
# -> 오타 교정 -> 문장 나누기(띄어쓰기, 조사)
# -> (필요시) 사용자사전 이용  -> 키워드 찾기

# 경로 설정은 스스로 환경에 맞게 설정
# 녹음과 오타 교정 시 인터넷 연결이 필요하니 연결 상태를 확인 요망


# 녹음 시작 함수 (Line 11 ~ Line 57)
# 녹음의 끝남을 감지하면(더 이상 소리가 들리지 않는다면) 프로그램이 종료
import speech_recognition as sr
import os
import time

# txt 파일 경로 지정 : test.py 가 실행된 폴더 내에 txt 파일 생성
text_file = 'myInterview.txt'

# 녹음을 시작하는 함수 : startRecord()
# 말하기 속도를 계산하기 위해서 실행시간을 구해야해서, startRecord()는 
# 실행시간 값을 반환하는 형식으로 작성
def startRecord():
    # txt 파일 생성
    with open(text_file, 'w', encoding='UTF-8') as file:
        pass

    r = sr.Recognizer()

    # 마이크 사용
    with sr.Microphone() as source:
        print("간단한 자기소개와 자신이 지원한 계열에 관한 자신의 경험을 말씀해주세요")
        
        # 녹음이 시작됨과 동시에 시간 측정
        start_time = time.time()    
        audio = r.listen(source)
        text = r.recognize_google(audio, language='ko-KR')
        
        # Line 35 : 잘 동작하는지만 확인 후 삭제 예정
        print("사용자의 답변 : " + text)

        #텍스트 파일에 결과 추가
        with open(text_file, 'a', encoding='UTF-8') as file:
            file.write(text + "\n")

        # 녹음 종료 시간 측정
        end_time = time.time()

        # 실행시간 = 종료시 - 시작시
        runningTime = end_time - start_time

        print("녹음이 끝났습니다.")
        print("총 녹음시간 : {:.2f}초".format(runningTime))

        return runningTime
    
final_runningTime = startRecord() # 실행시간을 저장시킬 변수 선언


# 글자 수를 계산해야지 말하기 속도 구하기 가능 (Line 62 ~ Line 77)
# startRecord() 반환값 이용
def fileopen(data):
    with open(data, 'r', encoding='UTF-8') as file:
        text = file.read()
        splitdata = text.split()
 
    return splitdata, len(splitdata)
 
def count_character(data):
    count = 0  
    for i in data :  
        count += len(i)
 
    return  count
 
data, count = fileopen(text_file)
wordCountResult = count_character(data) + count-1

# Line 80 : 글자 수 계산이 잘 되는지 확인 후 삭제예정
print("글자 수 : ", wordCountResult)


# 말하기 빠르기 비교 함수 (Line 84 ~ Line 97)
def compareSpeakingVel():
    calResult_min = 0.2 * wordCountResult 
    calResult_max = 0.3 * wordCountResult 

    #비교 시작
    #startRecord 함수를 보면, runningTime을 반환하게 만들어둠
    if calResult_min > final_runningTime:
        print("말하는 속도가 너무 빠릅니다.")
    elif calResult_max < final_runningTime:
        print("말하는 속도가 너무 느립니다.")
    else:
        print("적당한 속도로 말했습니댜.")

compareSpeakingVel()

# 오타 교정 (Line 101 ~ Line 137)
# 부산대학교 연구실에서 웹으로 작성한 프로그램 이용
import requests
import json

# 한국어 맞춤법 검사기 API URL
CHECKER_URL = 'http://164.125.7.61/speller/results'

# 입력 파일과 출력 파일의 이름
text_file = 'Voice And Text\myInterview.txt'

# 입력 파일에서 텍스트 읽기
with open(text_file, 'r', encoding='UTF-8') as file:
    text = file.read()

# 개행 문자를 \r\n으로 변환
text = text.replace('\n', '\r\n')

# 맞춤법 검사기 API에 텍스트 전송
response = requests.post(CHECKER_URL, data={'text1': text})

# API 응답에서 교정된 단어 추출
data = response.text.split('data = [', 1)[-1].rsplit('];', 1)[0]
data = json.loads(data)
corrected_text = text

# for err in data['errInfo']:
#     print(f"입력 내용 : {err['orgStr']}")
#     print(f"대치어 : {err['candWord']}")
#     print(f"도움말 : {err['help']}")
#     print("\n")

# 교정된 단어로 입력 텍스트 교체
for err in data['errInfo']:
    corrected_text = corrected_text.replace(err['orgStr'], err['candWord'])

# 교정된 텍스트를 출력 파일에 쓰기
with open(text_file, 'w', encoding='UTF-8') as file:
    file.write(corrected_text)


# 부산대학교에서 제공해주는 맞춤법 교정기 사용하면, 스페이스 공백 뿐 만 아닌
# '자료구조|자로구조' 와 같이 나오는 경우 존재
# 스페이스 공백을 기준으로 먼저 list에 정렬한 후, 해당 list의 요소를 순회하여 '|'가 존재하면 '|'를 기준으로 또 나누는 프로그램
# 정확한 keyword 추출을 위해서 동일한 방법으로 조사를 모두 제거하는 방향으로 프로그래밍 수행 (Line 146 ~ Line 218)

# 입력 파일 열기
with open(text_file, 'r', encoding='UTF-8') as file:
    # 파일 내용을 문자열로 읽기
    contents = file.read()

# 문자열을 띄어쓰기 단위로 분리하여 리스트에 저장
word_list = contents.split()

# 리스트 요소를 순회하면서 | 가 있는 요소를 처리
for i, word in enumerate(word_list):

    if '|' in word:
        # '|'를 기준으로 요소를 분리하여 새로운 리스트에 저장
        sub_list = word.split('|')
        # 분리된 요소를 기존 리스트에 덮어쓰기
        word_list[i:i+1] = sub_list
    else:
        pass

    if '을' in word:
        # '을' 기준
        sub_list = word.split('을')
        word_list[i:i+1] = sub_list
    else:
        pass
    
    if '를' in word:
        # '를' 기준
        sub_list = word.split('를')
        word_list[i:i+1] = sub_list
    else:
        pass

    # '이'의 경우 : '데이터베이스'에서 이가 모두 사라지게 되어 '데터베스'로 변환
    # 사용자사전을 이용하여 다시 '데터베스'를 '데이터베이스'로 변환할 예정
    if '이' in word:
        # '이' 기준
        sub_list = word.split('이') 
        word_list[i:i+1] = sub_list
    else:
        pass

    if '가' in word:
        # '가' 기준
        sub_list = word.split('가') 
        word_list[i:i+1] = sub_list
    else:
        pass

    if '로' in word:
        # '로' 기준
        sub_list = word.split('로') 
        word_list[i:i+1] = sub_list
    else:
        pass

    if '의' in word:
        # '의' 기준
        sub_list = word.split('의') 
        word_list[i:i+1] = sub_list
    else:
        pass
    
    if '와' in word:
        # '와' 기준
        sub_list = word.split('와') 
        word_list[i:i+1] = sub_list
    else:
        pass

# 출력 파일 열기 (덮어쓰기 모드)
with open(text_file, 'w', encoding='UTF-8') as file:
    # 리스트 요소를 문자열로 결합하여 파일에 쓰기
    file.write(' '.join(word_list))


# 사용자사전 이용 : '데터베스' -> '데이터베이스'로 변환 예정 (Line 222 ~ Line 247)
import pandas as pd

excel_file = 'data_dictionary.xlsx' # Excel 파일 이름 : 사용자사전 파일 이름

df = pd.read_excel(excel_file, header=0) # 엑셀 파일 읽어오기
target_words = df.iloc[:, 0].tolist() # 첫 번째 열 읽어오기 : 첫 번째 열에 고칠 단어 위치
corrected_words = df.iloc[:, 1].tolist() # 두 번째 열 읽어오기 : 첫 번째 열에 있는 단어들을 두 번째 열에 있는 단어들로 고침

# txt 파일 읽기
with open(text_file, "r", encoding="UTF-8") as file:
    lines = file.readlines()

# 저장한 새로운 list 만들기
new_lines = []

# txt 파일 수정
for line in lines:
    for i, target in enumerate(target_words):
        corrected_target = corrected_words[i].strip()
        line = line.replace(target, corrected_target)
    new_lines.append(line)

# txt 파일 다시 쓰기
with open(text_file, 'w', encoding='UTF-8') as file:
    for line in new_lines:
        file.write(line)


# 가장 많이 언급되는 keyword를 내림차순으로 반환 (Line 252 ~ Line 277)

# 파일 읽어오기
with open(text_file, 'r', encoding='UTF-8') as file:
    interview_text = file.read()

# interview_words 리스트 생성 : 띄어쓰기 기준으로 list화 
interview_words = interview_text.split()

# 키워드와 카운트 값을 저장할 딕셔너리 생성
keyword_list = {'네트워크': 0, '데이터베이스': 0, '딥러닝': 0, 
                '머신러닝': 0, '소프트웨어공학': 0, '알고리즘': 0, 
                '운영체제': 0, '자료구조': 0, '정보보안': 0, 
                '코딩': 0, '통계수학': 0}

# 키워드 리스트 생성
keywords = list(keyword_list.keys())

# 텍스트 파일 내의 단어들과 키워드 리스트를 비교하여 키워드 카운트
for word in interview_words:
    if word in keywords:
        keyword_list[word] += 1

# 키워드 리스트를 해당 키워드의 카운트 값에 따라 내림차순으로 정렬하여 반환
sorted_index = sorted(range(len(keyword_list)), key=lambda k: keyword_list[keywords[k]], reverse=True)
sorted_keywords = [keywords[i] for i in sorted_index]

print(sorted_keywords)

# 작성해야 하는 것 
# 내림차순으로 정렬한 키워드의 값 연결
# 영상처리 프로그램