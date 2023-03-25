# 가장 많이 언급되는 keyword를 내림차순으로 반환한다.

text_file = 'Code\Voice And Text\myInterview.txt'

# 파일 읽어오기
with open(text_file, 'r', encoding='UTF-8') as f:
    interview_text = f.read()

# interview_words 리스트 생성 : 띄어쓰기 기준으로 list화 한다.
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