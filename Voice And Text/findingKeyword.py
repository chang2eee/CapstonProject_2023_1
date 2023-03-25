# 키워드를 찾아서 나오는 횟수를 출력하는 프로그램이다.

text_file = 'myInterview.txt'

# 가장 많이 언급된 keyword 하나 찾아서 반환하는 함수
def find_most_frequent_keyword(text_file, keyword_list):
    with open(text_file, 'r', encoding='UTF-8') as file:
        found_keyword = {keyword: 0 for keyword in keyword_list}  # 초기값 0으로 설정
        for line in file:
            for keyword in keyword_list:
                if keyword in line:
                    found_keyword[keyword] += 1  # 해당 키워드가 찾아질 때마다 count 증가
                    break

    most_frequent_keyword = max(found_keyword, key=found_keyword.get) # 가장 많이 나온 keyword 만 반환한다. 
    return most_frequent_keyword

# keyword_list 안에 우리가 DB 테이블 명을 넣으면 된다.
keyword_list = ['네트워크', '데이터베이스', '딥러닝', '머신러닝', '소프트웨어공학',
                '알고리즘', '운영체제', '지료구조', '정보보안', '코딩', '통계수학']   

result = find_most_frequent_keyword(text_file, keyword_list)
print(result)