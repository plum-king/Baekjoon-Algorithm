# 두 수 a와 b가 주어졌을 때, a와 b의 최소 공배수를 구하는 프로그램을 작성하시오.

import sys
n = int(sys.stdin.readline())
ab_list = []

# 최대공약수 구하기
def gcd(m, n):
    gcd_list = [1]
    p = m
    if m > n:
        p = n
    for i in range(2, p+1):
        if m % i == 0 and n % i == 0:
            gcd_list.append(i)
    return gcd_list[-1] # 가장 마지막에 저장된 숫자가 공약수 중 가장 큰 수

for i in range(0, n):
    a, b = map(int, sys.stdin.readline().split())
    ab_list.append((a, b))

for i in range(0, n):
    print(int((ab_list[i][0] * ab_list[i][1]) / gcd(ab_list[i][0], ab_list[i][1]))) # 최소공배수는 두 수를 곱해서 최대공약수로 나눈 것