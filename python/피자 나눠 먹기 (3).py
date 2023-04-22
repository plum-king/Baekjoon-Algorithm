def solution(slice, n):
    answer = 1
    #slice * result 가 n보다 크거나 같아야돼
    while True:
        if answer * slice >= n:
            break
        answer+=1
    return answer