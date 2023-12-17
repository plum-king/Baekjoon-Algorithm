# 부분 문자열
# 2개의 문자열 s와 t가 주어졌을 때 s가 t의 부분 문자열인지 판단하는 프로그램을 작성하라. 
# 부분 문자열을 가지고 있는지 판단하는 방법은 t에서 몇 개의 문자를 제거하고 이를 순서를 바꾸지 않고 합쳤을 경우 s가 되는 경우를 이야기 한다.
import sys
input = sys.stdin.readline

while True:
    ss = input().rstrip() # 
    if not ss: # 만약 입력이 없으면
        break # while문 탈출
    s, t = ss.split() # 아니면 ss를 공백 기준으로 분리 
    str_s = list()
    str_t = list()

    if len(s) > len(t):
        str_long = s 
        str_short = t
    else:
        str_long = t 
        str_short = s

    i = 0
    j = 0
    check = list()

    while i < len(str_long) and j < len(str_short):
        if str_long[i] == str_short[j]:
            check.append(str_long[i])
            i+=1
            j+=1
        else:
            i+=1

    check_str = ""
    for i in range(len(check)):
        check_str += check[i]

    # print(check_str)
    # print(str_short)

    if check_str == str_short:
        print("Yes")
    else:
        print("No")
