# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys
n = int(sys.stdin.readline())
num_list = list()

for i in range(n):
    num_list.append(int(input()))

num_list.sort()

# sorted 사용하려면..
# rev_num_list = sorted(num_list)

for i in range(n):
    print(num_list[i])