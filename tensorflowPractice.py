import re
from nltk.tokenize import word_tokenize
import gensim
import nltk 

data_file = 'example.txt'
with open(data_file, 'r', encoding='UTF-8') as file:
    text = file.read()

def preprocess_text(text):
    #특수문자 제거
    text = re.sub(r'[^\w\s]','',text)
    #소문자로 변환
    text = text.lower() 
    # 텍스트 토큰화
    tokens = word_tokenize(text)
    # 불용어(stopwords) 제거
    stopwords = set(nltk.corpus.stopwords.words('english'))
    
    tokens = [token for token in tokens if not token in stopwords]
    # 길이가 1인 단어 제거
    tokens = [token for token in tokens if len(token) > 1]
    return tokens

tokens = preprocess_text(text)



# Word2Vec 모델 학습
model = gensim.models.Word2Vec(sentences=[tokens], size=100, window=5, min_count=5, workers=4, sg=1)

def find_similar_words(model, word, n):
    similar_words = model.wv.most_similar(word, topn=n)
    return [word[0] for word in similar_words]

word = "speling" # 예시로 오타인 "speling"을 사용합니다.
similar_words = find_similar_words(model, word, 5)
print(similar_words)