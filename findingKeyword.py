text_file = 'myInterview.txt'

def find_most_frequent_keyword(text_file, keyword_list):
    with open(text_file, 'r', encoding='UTF-8') as file:
        found_keyword = {keyword: 0 for keyword in keyword_list}  # 초기값 0으로 설정
        for line in file:
            for keyword in keyword_list:
                if keyword in line:
                    found_keyword[keyword] += 1  # 해당 키워드가 찾아질 때마다 count 증가
                    break

    most_frequent_keyword = max(found_keyword, key=found_keyword.get)
    return most_frequent_keyword

keyword_list = ['자료구조', 'DB']   

result = find_most_frequent_keyword(text_file, keyword_list)
print(result)