# 오타 및 띄어쓰기 교정 프로그램
# hanspell 오류로 더 이상 쓰지 않을 예정

from wordCorrect_hanspell import spell_checker
import kss

text_file = 'Voice And Text\myInterview.txt'

# 파일 읽기
with open(text_file, 'r', encoding='UTF-8') as file:
    lines = file.readlines()

# 수정된 문장 저장할 리스트 초기화
new_lines = []

# 오타 수정과 띄어쓰기 교정
for line in lines:
    # 한글 문장 오타 수정
    spelled_sent = spell_checker.check(line.strip())
    corrected_sent = spelled_sent.checked
    # 한글 문장 띄어쓰기 교정
    spacing_sent = kss.split_sentences(corrected_sent)
    # 수정된 문장 저장
    new_lines.extend(spacing_sent)

# 수정된 문장을 파일에 쓰기
with open(text_file, 'w', encoding='UTF-8') as file:
    for line in new_lines:
        file.write(line.strip() + '\n')