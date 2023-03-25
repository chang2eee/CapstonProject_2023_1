# 한국어 맞춤법 검사기 API URL
# 인터넷 찾아보니 신뢰성 높은 것 중 하나

import requests
import json

CHECKER_URL = 'http://164.125.7.61/speller/results'

# 입력 파일과 출력 파일의 이름
text_file = 'myInterview.txt'

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

# 교정된 단어로 입력 텍스트 교체
for err in data['errInfo']:
    corrected_text = corrected_text.replace(err['orgStr'], err['candWord'])

# 교정된 텍스트를 출력 파일에 쓰기
with open(text_file, 'w', encoding='UTF-8') as file:
    file.write(corrected_text)