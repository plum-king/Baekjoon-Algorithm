# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 첫 재출 => 답은 제대로 나오는데 시간초과
# import sys
# n = int(sys.stdin.readline())
# str_list = list()

# for i in range(0, n):
#     str_list.append(input()) #sys.stdin.readline() 사용하면서 '\n' 안나오게 하는 방법 찾아보기

# str_list.sort()
# rmv_list = list()

# for i in range(1, len(str_list)):
#     if(str_list[i-1] != str_list[i]):
#         rmv_list.append(str_list[i-1])

# for i in range(1, len(rmv_list)):
#     for j in range(i):
#         if(len(rmv_list[j]) > len(rmv_list[i])):
#             tmp = rmv_list[j]
#             rmv_list[j] = rmv_list[i]
#             rmv_list[i] = tmp

# print(rmv_list)

# 두 번째 제출 => 틀림
# 이유 1. 출력되는 결과를 보니까 마지막 문자가 안나옴 => i번째 리스트를 출력하려고 했더니 첫 문자가 안나옴
# 이유 2. 출력 형식이 잘못되었음
# import sys
# n = int(sys.stdin.readline())
# str_list = list()

# for i in range(0, n):
#     # str_list.append(input()) #sys.stdin.readline() 사용하면서 '\n' 안나오게 하는 방법 찾아보기
#     str_list.append(sys.stdin.readline().strip())

# str_list.sort()
# str_list.sort(key = len)
# # print(str_list)
# rmv_list = list()

# for i in range(1, len(str_list)):
#     if(str_list[i-1] != str_list[i]):
#         rmv_list.append(str_list[i-1])

# # for i in range(1, len(rmv_list)):
# #     for j in range(i):
# #         if(len(rmv_list[j]) > len(rmv_list[i])):
# #             tmp = rmv_list[j]
# #             rmv_list[j] = rmv_list[i]
# #             rmv_list[i] = tmp

# print(rmv_list)

# 세 번째 제출 => 성공
import sys
n = int(sys.stdin.readline())
str_list = list()

for i in range(n):
    str_list.append(sys.stdin.readline().strip())

print(set(str_list))
rmv_list=list(set(str_list))
rmv_list.sort()
rmv_list.sort(key = len)

for i in rmv_list:
    print(i)