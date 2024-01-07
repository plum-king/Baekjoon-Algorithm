# 점수가 가장 높은 k명은 상을 받을 것이다. 이 때, 상을 받는 커트라인이 몇 점인지 구하라.

import sys
n, k = map(int, sys.stdin.readline().split())
# int_list = list()

int_list = list(map(int, sys.stdin.readline().split()))

int_list.sort()

print(int_list[(n-k)])