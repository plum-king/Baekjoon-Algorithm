import sys

k, n = map(int, sys.stdin.readline().split())
array = list()

for i in range(k):
    array.append(int(sys.stdin.readline().strip()))

start = 1
end = max(array)
result = 0

while start <= end:
    mid = (start + end) // 2 # mid는 최대 길이가 될 값

    # mid에 해당하는 값으로 리스트의 모든 원소에서 나올 수 있는 랜선의 개수를 구해서 새로운 배열에 저장
    new_array = list(map(lambda x: x // mid, array))

    # 만들어진 리스트의 모든 원소에 대한 합 => n과 비교를 통해 조건을 충족하는지 확인
    total = sum(new_array)

    if total < n: # 랜선의 총 개수가 n보다 작으면 
        end = mid - 1 # mid가 더 작아져야 더 많이 잘릴 수 있음
    else:
        result = mid # n개보다 많이 만들어도 n개를 만드는 것에 포함되므로 저장
        start = mid + 1 # 최적의 값을 찾을 떄까지 반복하므로 start 값을 현재 mid보다 큰 값으로 수정

print(result)