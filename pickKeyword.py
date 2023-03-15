from voiceToText import *
import string

keywordList = ['자료구조', '자로', '쟈로', '쟈료', '자요', '구죠']
returnValue = []
splitter = [' ', '를', '으로', '로', '을']

with open(text_file, "r", encoding='UTF-8') as file:
    # 파일 내용 읽기
    contents = file.read()
    # 단어 추출하기
    words = []
    start = 0
    while start < len(contents):
        end = None
        for s in splitter:
            idx = contents.find(s, start)
            if idx != -1 and (end is None or idx < end):
                end = idx
        if end is None:
            end = len(contents)
        words.append(contents[start:end])
        start = end + 1
    # 각 단어별로 키워드가 있는지 확인하기
    for keyword in keywordList:
        count = 0
        for word in words:
            if keyword == word.strip(): # 단어 양쪽의 공백 제거
                count += 1
        print(f"'{keyword}'는 {count}번 발견되었습니다.")