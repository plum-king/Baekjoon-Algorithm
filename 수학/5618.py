# 자연수 n개가 주어진다. 이 자연수의 공약수를 모두 구하는 프로그램을 작성하시오.
import sys

def gcd(a, b):
    if(a == 0):
        return b
    return gcd(b % a, a)

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

g = gcd(m[0], gcd(m[1], m[-1]))
for i in range(1, (g // 2) + 1):
    if g % i == 0:
        print(i)
print(g)
 