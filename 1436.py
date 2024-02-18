import sys
input = sys.stdin.readline

n = int(input())

value = 666
cnt = 0
while True:
    if '666' in str(value):
        cnt += 1
    if cnt == n:
        print(value)
        break
    value += 1