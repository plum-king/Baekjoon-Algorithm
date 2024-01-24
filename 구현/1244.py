# ## 인덱스 에러
# import sys

# def switch(x): # 1과 0으로 바꾸는 함수 만들기
#     if x == 1:
#         x = 0
#     else:
#         x = 1
#     return x

# n = int(sys.stdin.readline()) # 스위치 개수
# swi = list(map(int, sys.stdin.readline().split())) # 스위치 상태 입력 받기

# k = int(sys.stdin.readline()) # 사람 수

# stat = []
# for i in range(k):
#     stat.append(list(map(int, sys.stdin.readline().split()))) # 성별, 받은 스위치 카드 번호

# for i in range(k):
#     if stat[i][0] == 1: # 남자라면
#         for j in range(1, len(swi)+1):
#             if j % stat[i][1] == 0: # 나머지가 0이어야 배순데 ..
#                 swi[j-1] = switch(swi[j-1]) # 자기가 받은 수의 배수는 모두 상태를 바꿔
#         # print(swi)            
#     else:
#         swi[stat[i][1]-1] = switch(swi[stat[i][1]-1])
#         # print(swi)
#         for j in range(1, n//2):
#             if (stat[i][1]-1)-j == -1:
#                 break
#             elif swi[(stat[i][1]-1)-j] == swi[(stat[i][1]-1)+j]: # 상태 같으면
#                 swi[(stat[i][1]-1)-j] = switch(swi[(stat[i][1]-1)-j])
#                 swi[(stat[i][1]-1)+j] = switch(swi[(stat[i][1]-1)+j])

# if len(swi) > 20:
#     for i in range(0,len(swi),20):
#         print(swi[i:i+20], end = ' ')
# else:
#     for i in range(0, len(swi)):
#         print(swi[i], end = ' ')
# print()

import sys

def change(x): # 1과 0으로 바꾸는 함수 만들기
    if switch[x] == 1:
        switch[x] = 0
    else:
        switch[x] = 1
    return

n = int(sys.stdin.readline()) # 스위치 개수
# 인덱스 헷갈리니까 앞에 원소 하나 넣기
switch = [0] + list(map(int, sys.stdin.readline().split())) # 스위치 상태 입력 받기

k = int(sys.stdin.readline()) # 사람 수

# 한 번 더 for문 돌릴 필요 없이 입력 받자마자 바로 성별과 스위치 카드 번호 확인

for i in range(k):
    gender, num = map(int, sys.stdin.readline().split())
    if gender == 1: # 이렇게 바로 성별 확인 -> 남자
        for j in range(1, n+1):
            if j % num == 0: #나머지 사용하지 않고 스위치 개수인 n까지 num씩 더한 원소의 상태를 바꾸면 됨
                # ex. n = 8, num = 3이니까 for i in range(num, n+1, num) 로 하면 switch[num] -> switch[num*2]인 경우만 change()에 넣으면 됨
                change(j)
    else: #여자
        change(num)
        for j in range(1, n//2):
            if num + j > n or num - j < 1: 
                break
            if switch[num-j] == switch[num+j]:
                change(num-j)
                change(num+j)
            else:
                break #break 안하면 틀림

for i in range(1, n+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()