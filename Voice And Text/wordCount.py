# 녹음 후 교정 작업을 끝낸 txt 파일 내에 있는 단어 수를 계산

from voiceToText import *

def fileopen(data):
    with open(data,'r', encoding='UTF-8') as file:
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

print("글자 수 : ", wordCountResult)