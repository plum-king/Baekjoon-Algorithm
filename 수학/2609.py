# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
import sys

n, m = map(int, sys.stdin.readline().split())

lcm = 0 # 최소공배수
gcd = [1] # 최대공약수
por = 0 # 나뉘어질 수

if n > m:
    por = m
else:
    por = n

for i in range(2, por+1):
    if n % i == 0 and m % i == 0:
        gcd.append(i)

lcm = (n * m) // gcd[-1] # 두 수를 곱한 뒤 최대공약수로 나누면 최소공배수

print(gcd[-1])
print(lcm)
