import sys

s, c = map(int, sys.stdin.readline().split())
pa_list = list()
for i in range(s):
    pa_list.append(int(sys.stdin.readline().strip()))

result = 0 # 최대한 크게 넣는 파의 길이
start = 1
end = max(pa_list)

while start <= end:
    mid = (start + end) // 2
    new_pa_list = list(map(lambda x: x // mid, pa_list)) # 넣은 파 개수 구하기
    total = sum(new_pa_list)

    if total >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(sum(pa_list) - result*c)