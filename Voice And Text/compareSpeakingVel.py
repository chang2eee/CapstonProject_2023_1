# 말하기 속도를 비교하는 프로그램이다.

from voiceToText import *
from wordCount import *

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