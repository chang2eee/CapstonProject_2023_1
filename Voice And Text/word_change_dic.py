import pandas as pd

text_file = 'Voice And Text\myInterview.txt' # txt 파일 이름
excel_file = 'Voice And Text\data_dictionary.xlsx' # Excel 파일 이름

df = pd.read_excel(excel_file, header=0) # 엑셀 파일 읽어오기
target_words = df.iloc[:, 0].tolist() # 첫 번째 열 읽어오기 : 첫 번째 열에는 고칠 단어들이 들어있다.
corrected_words = df.iloc[:, 1].tolist() # 두 번째 열 읽어오기 : 첫 번째 열에 있는 단어들들 두 번째 열에 있는 단어들로 고쳐야 한다

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
