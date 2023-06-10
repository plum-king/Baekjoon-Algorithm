import sys

input = sys.stdin.readline

n = [list(map(int, input().split())) for _ in range(5)]
m = []

for i in range(5):
    m += list(map(int, input().split()))

#하나씩 돌면서 확인
def check(n):
    check_num = 0

    #가로
    for i in n:
        if i.count(0) == 5:
            check_num+=1

    #세로
    for i in range(5):
        num = 0
        for j in range(5):
            if n[j][i] == 0:
                num +=1
        if num == 5:
            check_num+=1

    #왼쪽 대각선
    num = 0
    for i in range(5):
        if n[i][i] == 0:
            num+=1
    if num == 5:
        check_num+=1

    #오른쪽 대각선
    num = 0
    for i in range(5):
        if n[i][4-i] == 0:
            num+=1
    if num == 5:
        check_num+=1

    return check_num

count = 0

for i in range(25):
    for j in range(5):
        for k in range(5):
            if m[i] == n[j][k]:
                n[j][k] = 0
                count+=1

    if count >= 12:
        if check(n) >= 3:
            print(count)
            break