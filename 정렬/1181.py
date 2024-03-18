import sys

N = int(sys.stdin.readline()) # 단어 개수
str_list = list()
for i in range(N):
    str_list.append(sys.stdin.readline().strip()) 
    # strip() 사용하여 각 원소의 '\n' 삭제

str_list = set(str_list) # 중복 제거
str_list = sorted(str_list, key = lambda x: (len(x), x)) 
# 길이가 짧은 것부터 정렬하고 만약 길이가 동일하면 x를 기준으로 정렬 = 사전순 정렬

for i in str_list:
    print(i)