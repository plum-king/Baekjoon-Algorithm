# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

import sys
n = int(sys.stdin.readline())
str_list = list()

for i in range(n):
    # str_list.append(input()) #sys.stdin.readline() 사용하면서 '\n' 안나오게 하는 방법 찾아보기
    str_list.append(sys.stdin.readline().strip())

rmv_list=list(set(str_list))
# print(rmv_list)
rmv_list.sort()
rmv_list.sort(key = len)
# print(str_list)
# len_list = len(str_list)

# for i in range(len_list):
#     if(str_list[i] != str_list[i+1]):
        

# for i in range(1, len(rmv_list)):
#     for j in range(i):
#         if(len(rmv_list[j]) > len(rmv_list[i])):
#             tmp = rmv_list[j]
#             rmv_list[j] = rmv_list[i]
#             rmv_list[i] = tmp

for i in rmv_list:
    print(i)