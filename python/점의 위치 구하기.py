def solution(dot):
    answer = 3
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2
    elif dot[0] > 0 and dot[1] < 0:
        answer = 4
        
    return answer