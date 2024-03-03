import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P.sort()

answer = 0
for i in range(1, N+1):
    answer += sum(P[:i])

print(answer)