cnt = 0 # global로 사용

def dfs(numbers, target, current, idx):
    global cnt
    if idx == len(numbers): # numbers를 모두 거쳤을 때
        if current == target: # target이랑 현재 값이 같으면 
            cnt += 1 # 하나 증가
        return
    
    dfs(numbers, target, current + numbers[idx], idx+1) # 원소가 +인 경우
    dfs(numbers, target, current - numbers[idx], idx+1) # 원소가 -인 경우

def solution(numbers, target):
    dfs(numbers, target, 0, 0) # 배열, 타겟넘버, 현재까지의 합, 인덱스
    return cnt