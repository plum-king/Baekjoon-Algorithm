def solution(array):
    answer = 0
    num = 0
    array.sort()
    for arr in array:
        num += 1
    answer = array[num//2]
        
    return answer
