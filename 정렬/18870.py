import sys
N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

x_list = sorted(list(set(x))) # 중복 제거 후, 정렬하고 새로운 리스트에 저장

x_dict = dict() # 딕셔너리 생성
for i in range(len(x_list)): # x_list를 돌면서
    x_dict[x_list[i]] = i # x_list에 정렬된 순서대로 인덱스 값을 부여하여 딕셔너리에 저장 

for i in x: # 입력받았던 x 리스트의 원소 순서대로 돌면서
    print(x_dict[i], end= ' ') # 딕셔너리의 키 값에 x 리스트의 원소가 들어가면서 딕셔너리의 키에 해당하는 값이 결과로 나옴