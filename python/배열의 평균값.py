def solution(numbers):
    answer = 0
    for n in numbers:
        answer+=n
    answer/=len(numbers)
    return answer
