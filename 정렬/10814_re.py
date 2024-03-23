import sys

N = int(sys.stdin.readline())

mem_list = list()
for i in range(N):
    mem_list.append(sys.stdin.readline().split())
    # ['21 Junkyu', '21 Dohyun', '20 Sunyoung']
    # mem_list.append(sys.stdin.readline().strip())

mem_list = sorted(mem_list, key = lambda x : int(x[0]))

for i in mem_list:
    print(i[0] + ' ' + i[1])
