# PNU 에서 제공해주는 맞춤법 교정기 사용하면, 스페이스 공백 뿐 만 아니라, '자료구조|자로구조' 와 같이 나오는 경우도 존재한다.
# 스페이스 공백을 기준으로 먼저 list에 정렬한 후, 해당 list의 요소를 순회하여 '|'가 존재하면 '|'를 기준으로 또 나누는 프로그램
# 정확한 keyword 추출을 위해서 조사를 모두 제거하는 방향으로 프로그래밍 수행

text_file = 'Voice And Text\myInterview.txt'

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

    if '으로' in word:
        # '으로' 기준
        sub_list = word.split('으로') 
        word_list[i:i+1] = sub_list
    else:
        pass

# 출력 파일 열기 (덮어쓰기 모드)
with open(text_file, 'w', encoding='UTF-8') as file:
    # 리스트 요소를 문자열로 결합하여 파일에 쓰기
    file.write(' '.join(word_list))