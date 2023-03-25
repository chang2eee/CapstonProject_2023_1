# PNU 에서 제공해주는 맞춤법 교정기 사용하면, 스페이스 공백 뿐 만 아니라, '자료구조|자로구조' 와 같이 나오는 경우도 존재한다.
# 스페이스 공백을 기준으로 먼저 list에 정렬한 후, 해당 list의 요소를 순회하여 '|'가 존재하면 '|'를 기준으로 또 나누는 프로그램

text_file = 'Code\myInterview.txt'

# 입력 파일 열기
with open(text_file, 'r', encoding='UTF-8') as file:
    # 파일 내용을 문자열로 읽기
    contents = file.read()

# 문자열을 띄어쓰기 단위로 분리하여 리스트에 저장
word_list = contents.split()

# 리스트 요소를 순회하면서 | 가 있는 요소를 처리
for i, word in enumerate(word_list):
    if '|' in word:
        # |를 기준으로 요소를 분리하여 새로운 리스트에 저장
        sub_list = word.split('|')
        # 분리된 요소를 기존 리스트에 덮어쓰기
        word_list[i:i+1] = sub_list

# 출력 파일 열기 (덮어쓰기 모드)
with open(text_file, 'w', encoding='UTF-8') as file:
    # 리스트 요소를 문자열로 결합하여 파일에 쓰기
    file.write(' '.join(word_list))
