import sys
N, M = map(int, sys.stdin.readline().split())
tree_list = list(map(int, sys.stdin.readline().split()))

result = 0
start = 1
end = max(tree_list)

while start <= end:
    mid = (start + end) // 2
    new_tree_list = list(map(lambda x: x-mid if x-mid>0 else 0, tree_list))
    sum_tree = sum(new_tree_list)
    if sum_tree >= M: # 나무의 합이 지정된 값보다 큰 경우 mid 값을 result에 저장
       result = mid 
       start = mid + 1
    else:
        end = mid - 1

print(result)