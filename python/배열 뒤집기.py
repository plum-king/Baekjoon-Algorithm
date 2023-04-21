def solution(num_list):
    answer = []
    i = len(num_list)-1
    while i >= 0:
        answer.append(num_list[i])
        i-=1
    return answer