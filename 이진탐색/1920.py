import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a.sort() # 이분 탐색을 하기 위한 오름차순 정렬

for i in b:
    result = 0
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = (start + end) // 2 
        if a[mid] == i:
            result = 1
            break
        elif a[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    print(result)