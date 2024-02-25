import sys

n = int(sys.stdin.readline())
rank = []
for i in range(n):
    rank.append(int(sys.stdin.readline()))

rank.sort()

result = 0
for i in range(1, n+1):
    result += abs(i-rank[i-1])
print(result)