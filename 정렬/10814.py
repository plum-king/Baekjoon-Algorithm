# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

import sys
n = int(sys.stdin.readline())
people_list = list()

for i in range(n):
    age, name = map(str, input().split())
    people_list.append((int(age), name))

people_list.sort(key = lambda x:x[0]) # sort 기준

for i in people_list:
    print(i[0], i[1])