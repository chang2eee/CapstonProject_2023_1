from konlpy.tag import Okt

okt = Okt()

text ='설치가 잘 되나요? 안되면 댓글 남겨주세용'

print(okt.morphs(text))