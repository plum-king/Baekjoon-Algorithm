def solution(array, n):
    answer = 0
    for arr in array:
        if n == arr:
            answer+=1
    return answer