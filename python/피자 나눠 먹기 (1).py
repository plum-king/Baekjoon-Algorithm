def solution(n):
    answer = 1
    while True:
        if (answer * 7) >= n:
            break
        else:
            answer+=1
    return answer
