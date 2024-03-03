import sys

N, K = map(int, sys.stdin.readline().split()) 
coin_lst = list()
for i in range(N):
    coin_lst.append(int(sys.stdin.readline()))

count = 0
for i in reversed(range(N)):
    count += K // coin_lst[i]
    K = K % coin_lst[i] 

print(count)