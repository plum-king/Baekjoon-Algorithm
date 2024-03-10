# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

import sys
N, K= map(int, sys.stdin.readline().split()) # 동전 종류의 수, 만들 금액
A = list() # 동전 종류

for i in range(N):
    A.append(int(sys.stdin.readline())) # split 안써도 돼(쓰면 int에 안들어가고 "['1'], ['2']" 이런 식으로 저장됨) 

A.sort(reverse = True) # 내림차순 정렬

sum = 0 # 동전 개수

for i in A:
    if K < i: # 동전이 만들 금액보다 크다면 스킵
        continue
    else:
        sum += (K // i)
        K %= i

print(sum)