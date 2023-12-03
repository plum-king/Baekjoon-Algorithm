# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

def prime_fac(m, list):
    if m == 1:
        return list
    for i in range (2, m+1):
        if m % i == 0:
            list.append(i)
            m = int(m/i)
            return prime_fac(m, list)

import sys

n = int(sys.stdin.readline())

n_list = [] # 나눠진 수 목록
prime_fac(n, n_list)

for i in range (len(n_list)):
    print(n_list[i])