# KoNLPy는 한국어 자연어 처리를 위한 파이썬 라이브러리이다.
# 형태소 분석기는 [Hannanum, Kkam, Komoran, Mecab, Twitter]가 있다.
from konlpy.tag import Komoran

# 클레스 불러옴 
# 사용자 사전의 내용은 아래 출처에서
# https://kbig.kr/portal/kbig/knowledge/files/bigdata_report.page?bltnNo=10000000016451
Komoran = Komoran(userdic='./NIADic.tsv')

# 텍스트 파일 읽기
def read_corpus_data(filename):
    with open(filename, 'r') as f:
        data = [line for line in f.read().splitlines()]
    return data

# 텍스트 파일의 문장 -> sentence 배열 안에
sentence = read_corpus_data('./sentences.txt')

# 품사의 틀
N = ['NNG', 'NNP', 'NNB', 'NP', 'NR']   # 명사
V = ['VV', 'VA', 'VX', 'VCP', 'VCN']    # 용언
M = ['MM', 'MAG', 'MAJ']    # 수식언
I = ['IC']  # 독립언
J = ['JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JX', 'JC']   # 관계언

# 문장들 안에 들어있는 품사의 종류별 개수
count = [0, 0, 0, 0, 0]
for s in sentence:
    pos = Komoran.pos(s)
    for p in pos:

        if p[1] in N:
            count[0] += 1

        elif p[1] in V:
            count[1] += 1

        elif p[1] in M:
            count[2] += 1

        elif p[1] in I:
            count[3] += 1

        elif p[1] in J:
            count[4] += 1
        

print(count)