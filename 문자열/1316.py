# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오

import sys
n = int(sys.stdin.readline())
str_list = list()
for i in range(n):
    str_list.append(sys.stdin.readline().strip())

# 생각한 풀이 방법
# 단어에서 중복 제거 후 남은 문자 - 1 = 다른 문자로 바뀌는 횟수 => 이 공식에 맞지 않으면 count에서 제거
# ex1) aaabbb => ab => 1번 바뀜
# ex2) ababab => ababab => 5번 바뀜 

cnt = 0 # 그룹 단어 개수
set_cnt_list = list() # 중복 제거 후, 단어당 바뀐 횟수
for i in range(len(str_list)):
    set_cnt_list.append(len(set(str_list[i]))-1)

overlap_cnt_list = list() # 단어당 바뀐 횟수

for i in range(len(str_list)):
    overlap_cnt_list.append(0)
    for j in range(len(str_list[i])-1):
        if(str_list[i][j] != str_list[i][j+1]):
            overlap_cnt_list[i]+=1

for i in range(len(str_list)):
    if(set_cnt_list[i] == overlap_cnt_list[i]):
        cnt+=1

print(cnt)