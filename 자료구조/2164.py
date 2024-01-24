import sys
from collections import deque
n = int(sys.stdin.readline())

# 첫 번째꺼를 버리고 맨 위에 있던 걸 아래로 보내니까 스택이 아니라 큐
queue = deque()

for i in range(1, n+1):
    queue.append(i) # 1~N까지 완성 #여기서 시간초과인듯..

# for i in range(n):
#     if len(queue) == 1:
#         print(queue[0])
#         break
#     else:
#         queue.pop(0)
#         # print(queue) # 가장 위에 있는 숫자 지워지는지 확인
#         queue.append(queue.pop(0)) # 두 번째 숫자 마지막에 추가 후 두 번째 있던 숫자 지우기
#         # print(queue)

for i in range(n-1):
    queue.popleft()
        # print(queue) # 가장 왼쪽에 있는 숫자 지워지는지 확인
    queue.append(queue.popleft()) # 두 번째 숫자 마지막에 추가 후 두 번째 있던 숫자 지우기
        # print(queue)

print(queue[0])