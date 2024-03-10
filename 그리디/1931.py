# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
# 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
# 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

import sys

N = int(sys.stdin.readline()) # 회의 수
N_list = list() # 회의 정보

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    N_list.append((a, b))

# 끝나는 시간 순서대로 오름차순 정렬 후, 시작하는 시간 순서대로 오름차순 정렬
N_list = sorted(N_list, key = lambda x: (x[1], x[0]))

cnt = 1 # 회의 개수
end_time = N_list[0][1] # 항상 가장 앞에 오는 회의가 회의실을 사용할 첫 번째 회의이므로, 끝나는 시간을 지정

# 끝나는 시간이 이를 수록 좋은 거니까 끝나는 시간 기준으로 정렬하고, 시작하는 시간은 다음 회의 중 가장 빠르게 끝나는 회의
for i in N_list[1:]:
    if end_time <= i[0]: # 지정한 회의가 끝나는 시간보다 크거나 같은 경우 해당 회의 선택
        cnt += 1
        end_time = i[1] # 해당 회의의 끝나는 시간으로 업데이트

print(cnt)
